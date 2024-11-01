from evm_client.contract.methods import Methods

class Contract:

    def __init__(self, address, abi):
        self.address = address
        self.abi = abi
        self._functions = [part for part in abi if part['type'] == 'function']
        self.functions = Methods()
        self.functions.build_methods(self.address, self._functions)
        self._events = [part for part in abi if part['type'] == 'event']

