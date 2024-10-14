from typing import Union
from evm_client.core import EthCore
from evm_client.sync_client.client_core import SyncClientCore
from evm_client.crypto_utils import hex_to_int
from evm_client.sync_client.utils import process_http_response

#probably best to parse the json and get the result from these?
class SyncEthClient(SyncClientCore, EthCore):

    def protocol_version(self, request_id: int=1):
        body = self.get_eth_protocol_version_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def syncing(self, request_id: int=1):
        body = self.get_eth_syncing_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def coinbase(self, request_id: int=1):
        body = self.get_eth_coinbase_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def chain_id(self, request_id: int=1):
        body = self.get_eth_chain_id_body(request_id=request_id)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

    def block_number(self, request_id: int=1):
        body = self.get_eth_block_number_body(request_id=request_id)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

    def mining(self, request_id: int=1):
        body = self.get_eth_mining_body(request_id=request_id)
        res =  self.make_post_request(body)
        return process_http_response(res)

    def hashrate(self, request_id: int=1):
        body = self.get_eth_hashrate_body(request_id=request_id)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

    def gas_price(self, request_id: int=1):
        body = self.get_eth_gas_price_body(request_id=request_id)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

    #mostly expect this to not work on public nodes
    def accounts(self, request_id: int=1):
        body = self.get_eth_accounts_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def get_balance(self, address: str, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_get_balance_body(address, block_number=block_number, request_id=request_id)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

    def get_storage_at(self, address: str, storage_position:int, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_get_storage_at_body(address, storage_position, block_number=block_number, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def get_transaction_count(self, address: str, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_get_transaction_count_body(address)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

