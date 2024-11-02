from hexbytes import HexBytes
from eth_hash import Keccak256
from eth_hash.backends.pycryptodome import CryptodomeBackend
from eth_abi import decode
from evm_client.types import EthFilter

class EventInfo:

    def __init__(self, anonymous, inputs, name, _hasher=None):
        self.anonymous = anonymous
        self.inputs = inputs
        self.name = name
       
        self.input_types = []
        self.indexed_inputs = []
        self.unindexed_inputs = []
        for i in self.inputs:
            self.input_types.append(i['type'])
            if i['indexed']:
                self.indexed_inputs.append(i)
            else:
                self.unindexed_inputs.append(i)
        self.signature = "{}({})".format(self.name, ",".join(self.input_types))
        self.unindexed_types = [u['type'] for u in self.unindexed_inputs]
        self.unindexed_names = [u['name'] for u in self.unindexed_inputs]
        self.indexed_types = [i['type'] for i in self.indexed_inputs]
        self.indexed_names = [i['name'] for i in self.indexed_inputs]

        _hasher = _hasher or Keccak256(CryptodomeBackend())
        self.hash = '0x' + HexBytes(_hasher(self.signature.encode('utf-8'))).hex() 

    @classmethod
    def from_abi_part(cls, part, _hasher=None):
        return cls(
            part['anonymous'],
            part['inputs'],
            part['name'],
            _hasher=_hasher
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


class Event:

    def __init__(self, address, abi_part, _hasher=None):
        self.address = address
        self.info = EventInfo.from_abi_part(abi_part, _hasher=_hasher)
        self.hash = self.info.hash

    #NOTE: currently does not support adding additional topics. Users can append to EthFilter.topics as needed
    def get_filter(self, from_block=None, to_block=None, block_hash=None):
        return EthFilter(
            address=self.address,
            from_block=from_block,
            to_block=to_block,
            topics=[self.info.hash],
            block_hash=block_hash
        )
    
    def decode_result(self, result):
        return self.info.decode_result(result)

    def decode_results(self, results):
        return self.info.decode_results(results)


class Events:
    
    def build_events(self, address, events, _hasher=None):
        _hasher = _hasher or Keccak256(CryptodomeBackend())
        for event in events:
            setattr(self, event['name'], Event(address, event, _hasher=_hasher))
