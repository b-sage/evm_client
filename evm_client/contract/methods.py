from eth_abi import encode, decode
from hexbytes import HexBytes
from eth_hash import Keccak256
from eth_hash.backends.pycryptodome import CryptodomeBackend
from evm_client.types import Transaction

class Method:

    def __init__(self, address, name, inputs, outputs, payable, state_mutability, _hasher=None):
        self.address = address
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.payable = payable
        self.state_mutability = state_mutability
       
        self.input_types = self._build_types(self.inputs)
        self.output_types = self._build_types(self.outputs)
        self.signature = "{}({})".format(self.name, ",".join(self.input_types))

        _hasher = _hasher = Keccak256(CryptodomeBackend())
        self.selector = '0x' + HexBytes(_hasher(self.signature.encode('utf-8')))[0:4].hex() 
   
    def _build_type_from_component(self, part):
        result = ''
        if part.get('components'):
            for component in part['components']:
                result += '{},'.format(self._build_type_from_component(component))
            result = result.rstrip(',')
            result = '(' + result + ')'
        else:
            result += '{},'.format(part['type'])
        result = result.rstrip(',')
        return result

    def _build_types(self, io):
        types_ = []
        for part in io:
            if part.get('components') is None:
                types_.append(part['type'])
            else:
                types_.append(self._build_type_from_component(part))
        return types_
 
    @classmethod
    def from_abi_part(cls, part, address, _hasher=None):
        return cls(
            address,
            part['name'],
            part['inputs'],
            part['outputs'],
            part.get('payable'),
            part['stateMutability'],
            _hasher=_hasher
        )

    def build_transaction(self, *args, from_=None, gas=None, gas_price=None, value=None, nonce=None):
        return Transaction(
            self.selector + self.encode_args(*args),
            to=self.address,
            from_=from_,
            gas=gas,
            gas_price=gas_price,
            value=value,
            nonce=nonce
        )

    def encode_args(self, *args):
        #TODO: better input validation
        assert len(args) == len(self.inputs), "msimatch between expected inputs length and actual inputs length"
        if self.inputs:
            return HexBytes(encode(self.input_types, args)).hex()
        return ''

    #NOTE: unless we use the client directly in the contract object the user will have to do the decoding. Fortunately,
    #this is actually pretty simple as we can just have the user pass the "decode_result/decode_results" method to the desired
    #client method as a 'decoder' arg, E.x. 
    #client.call(contract.functions.balanceOf.build_transaction('0x....'), decoder=contract.functions.balanceOf.decode_result)
    def decode_result(self, result):
        decoded = decode(self.output_types, HexBytes(result))
        if len(decoded) == 1:
            return decoded[0]
        return [item for item in decoded]

    def decode_results(self, results):
        return [self.decode_result(r) for r in results]


class Methods:

    #should we make methods accessible by ['']?
    def __init__(self, address, functions, _hasher=None):
        #just save a bit of time instantiating one hasher for all methods vs one per method
        _hasher = _hasher or Keccak256(CryptodomeBackend())
        methods = []
        for function in functions:
            method = Method.from_abi_part(function, address, _hasher=_hasher)
            #TODO: overloaded functions break, Vyper contracts namely. not sure of any work around other than appending the name somehow
            setattr(self, function['name'], method)
            methods.append(method)
        self.signatures = [m.signature for m in methods]
        self.selectors = [m.selector for m in methods]
        self.signature_selector_map = dict(zip(self.signatures, self.selectors))

