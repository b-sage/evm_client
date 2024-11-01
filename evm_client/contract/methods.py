from eth_abi import encode, decode
from hexbytes import HexBytes
from eth_hash import Keccak256
from eth_hash.backends.pycryptodome import CryptodomeBackend
from evm_client.types import Transaction

class MethodInfo:

    def __init__(self, name, inputs, outputs, payable, state_mutability, _hasher=None):
        self.name = name
        self.inputs = inputs
        self.input_types = [i['type'] for i in self.inputs]
        self.outputs = outputs
        self.output_types = [o['type'] for o in self.outputs]
        self.payable = payable
        self.state_mutability = state_mutability
        self._hasher = _hasher or Keccak256(CryptodomeBackend())
        self.selector = self.get_selector()

    @classmethod
    def from_abi_part(cls, part, _hasher=None):
        return cls(
            part['name'],
            part['inputs'],
            part['outputs'],
            part['payable'],
            part['stateMutability'],
            _hasher=_hasher
        )

    def _build_signature(self):
        return "{}({})".format(self.name, ",".join(self.input_types))

    def _build_selector(self, signature):
        return HexBytes(self._hasher(signature.encode('utf-8')))[0:4].hex()

    def get_selector(self):
        sig = self._build_signature()
        return '0x' + self._build_selector(sig)

    def __call__(self, *args):
        assert len(args) == len(self.inputs), "msimatched between expected inputs length and actual inputs length"
        if self.inputs:
            return HexBytes(encode(self.input_types, args)).hex()
        return ''

    #NOTE: unless we use the client directly in the contract object the user will have to do the decoding
    #I do not like the idea of using client directly here, as it limits the potential of batch requesting
    def decode_result(self, result):
        decoded = decode(self.output_types, HexBytes(result))
        if len(decoded) == 1:
            return decoded[0]
        return [item for item in decoded]


class Method:

    def __init__(self, address, abi_part, _hasher=None):
        self.address = address
        self.method_info = MethodInfo.from_abi_part(abi_part, _hasher)
        self.selector = self.method_info.selector

    def __call__(self, *args, from_=None, gas=None, gas_price=None, value=None, nonce=None):
        return Transaction(
            self.selector + self.method_info(*args),
            to=self.address,
            from_=from_,
            gas=gas,
            gas_price=gas_price,
            value=value,
            nonce=nonce
        )

    def decode_result(self, result):
        return self.method_info.decode_result(result)


class Methods:

    def build_methods(self, address, functions, _hasher=None):
        #just save a bit of time instantiating one hasher for all methods vs one per method
        _hasher = _hasher or Keccak256(CryptodomeBackend())
        for function in functions:
            setattr(self, function['name'], Method(address, function, _hasher))

