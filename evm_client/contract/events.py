from hexbytes import HexBytes
from eth_hash import Keccak256
from eth_hash.backends.pycryptodome import CryptodomeBackend
from eth_abi import decode
from evm_client.types import EthFilter

class Event:

    def __init__(self, address, anonymous, inputs, name, _hasher=None):
        self.address = address
        self.anonymous = anonymous
        self.inputs = inputs
        self.name = name
       
        #TODO: lot of list comps over the same lists here... should probably test efficieny but I think this looks nicer
        self.input_types = [i['type'] for i in self.inputs]
        self.indexed_inputs = [i for i in self.inputs if i['indexed']]
        self.unindexed_inputs = [i for i in self.inputs if not i['indexed']]
        
        self.signature = "{}({})".format(self.name, ",".join(self.input_types))
        self.unindexed_types = [u['type'] for u in self.unindexed_inputs]
        self.unindexed_names = [u['name'] for u in self.unindexed_inputs]
        self.indexed_types = [i['type'] for i in self.indexed_inputs]
        self.indexed_names = [i['name'] for i in self.indexed_inputs]

        _hasher = _hasher or Keccak256(CryptodomeBackend())
        self.hash = '0x' + HexBytes(_hasher(self.signature.encode('utf-8'))).hex() 

    @classmethod
    def from_abi_part(cls, part, address, _hasher=None):
        return cls(
            address,
            part['anonymous'],
            part['inputs'],
            part['name'],
            _hasher=_hasher
        )

    #NOTE: currently does not support adding additional topics. Users can append to EthFilter.topics as needed
    def build_filter(self, from_block=None, to_block=None, block_hash=None):
        return EthFilter(
            address=self.address,
            from_block=from_block,
            to_block=to_block,
            topics=[self.hash],
            block_hash=block_hash
        )
    
    #TY Banteg for the idea: https://codeburst.io/deep-dive-into-ethereum-logs-a8d2047c7371
    def decode_result(self, result):
        unindexed_values = decode(self.unindexed_types, HexBytes(result['data']))
        unindexed_map = dict(zip(self.unindexed_names, unindexed_values))

        indexed_values = [decode([t], HexBytes(v))[0] for t, v in zip(self.indexed_types, result['topics'][1:])]
        indexed_map = dict(zip(self.indexed_names, indexed_values))
        
        res = {k: v for k, v in result.items() if k not in ['topics', 'data']}
        res['data'] = {**indexed_map, **unindexed_map}
        return res

    def decode_results(self, results):
        return [self.decode_result(r) for r in results]


class Events:
    
    def __init__(self, address, events, _hasher=None):
        _hasher = _hasher or Keccak256(CryptodomeBackend())
        _events = []
        for event in events:
            e = Event.from_abi_part(event, address, _hasher=_hasher)
            setattr(self, event['name'], e)
            _events.append(e)
        self.signatures = [e.signature for e in _events]
        self.hashes = [e.hash for e in _events]
        self.signature_hash_map = dict(zip(self.signatures, self.hashes))
