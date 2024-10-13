from typing import Union
from evm_client.core import EthCore
from evm_client.sync_client.client_core import SyncClientCore

#probably best to parse the json and get the result from these?
class SyncEthClient(SyncClientCore, EthCore):

    def protocol_version(self, request_id: int=1):
        body = self.get_eth_protocol_version_body(request_id=request_id)
        return self.make_post_request(body)

    def syncing(self, request_id: int=1):
        body = self.get_eth_syncing_body(request_id=request_id)
        return self.make_post_request(body)

    def coinbase(self, request_id: int=1):
        body = self.get_eth_coinbase_body(request_id=request_id)
        return self.make_post_request(body)

    def chain_id(self, request_id: int=1):
        body = self.get_eth_chain_id_body(request_id=request_id)
        return self.make_post_request(body)

    def block_number(self, request_id: int=1):
        body = self.get_eth_block_number_body(request_id=request_id)
        return self.make_post_request(body)

    def mining(self, request_id: int=1):
        body = self.get_eth_mining_body(request_id=request_id)
        return self.make_post_request(body)

    def hashrate(self, request_id: int=1):
        body = self.get_eth_hashrate_body(request_id=request_id)
        return self.make_post_request(body)

    def gas_price(self, request_id: int=1):
        body = self.get_eth_gas_price_body(request_id=request_id)
        return self.make_post_request(body)

    def accounts(self, request_id: int=1):
        body = self.get_eth_accounts_body(request_id=request_id)
        return self.make_post_request(body)

    def get_balance(self, address: str, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_get_balance_body(address, block_number, request_id=request_id)
        return self.make_post_request(body)



