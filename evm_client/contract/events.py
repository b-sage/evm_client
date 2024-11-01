from eth_hash import Keccak256
from eth_hash.backends.pycryptodome import CryptodomeBackend
from evm_client.types import EthFilter

class EventInfo:

    def __init__(self, anonymous, inputs, name, _hasher=None):
        self.anonymous = anonymous
        self.inputs = inputs
        self.input_types = [i['type'] for i in self.inputs]
        self.name = name
        self._hasher = hasher or Keccak256(CryptodomeBackend())
        self.event_hash = self.get_event_hash()

    @classmethod
    def from_abi_part(cls, part, _hasher=None):
        return cls(
            part['anonymous'],
            part['inputs'],
            part['name'],
            _hasher=_hasher
        )

    def _build_event_sig(self):
        return "{}({})".format(self.name, ",".join(self.input_types))

    def get_event_hash(self):
        sig = self._build_event_sig()
        return '0x' + HexBytes(self._hasher(sig)).hex()

    #decoding events is a bit more involved. If a topic is indexed, it needs to be decoded individually
    #the non indexed topics get decoded as one

class Event:

    def __init__(self, address, abi_part, _hasher=None):
        self.address = address
        self.event_info = EventInfo.from_abi_part(abi_part, _hasher=_hasher)
        self.event_hash = self.event_info.event_hash

