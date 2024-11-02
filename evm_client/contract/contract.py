from eth_hash import Keccak256
from eth_hash.backends.pycryptodome import CryptodomeBackend
from evm_client.contract.methods import Methods
from evm_client.contract.events import Events

class Contract:

    def __init__(self, address, abi):
        self.address = address
        self.abi = abi
        self._functions = [part for part in abi if part['type'] == 'function']
        self._events = [part for part in abi if part['type'] == 'event']
        
        _hasher = Keccak256(CryptodomeBackend())
        self.functions = Methods()
        self.functions.build_methods(self.address, self._functions, _hasher)
        self.events = Events()
        self.events.build_events(self.address, self._events, _hasher)
