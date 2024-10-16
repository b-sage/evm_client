from typing import Union
from evm_client.core import EthCore
from evm_client.sync_client.client_core import SyncClientCore
from evm_client.crypto_utils import hex_to_int
from evm_client.sync_client.utils import process_http_response
from evm_client.parsers.transaction import TransactionParser
from evm_client.types.transaction import Transaction

#TODO: some methods block number is more of an optional arg where others it makes more sense to require it's passed, review these

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
        body = self.get_eth_get_transaction_count_body(address, request_id=request_id)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

    def get_transaction(self, transaction_hash: str, request_id: int=1):
        body = self.get_eth_get_transaction_by_hash_body(transaction_hash, request_id=request_id)
        res = self.make_post_request(body)
        return TransactionParser.from_raw_json(process_http_response(res)).to_json()

    def get_block_transaction_count_by_hash(self, block_hash: str, request_id: int=1):
        body = self.get_eth_get_block_transaction_count_by_hash_body(block_hash, request_id=request_id)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

    def get_block_transaction_count_by_number(self, block_number: Union[int, str], request_id: int=1):
        body = self.get_eth_get_block_transaction_count_by_number_body(block_number, request_id=request_id)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

    #NOTE: return 0 instead of None? bit more predictable this way
    def get_uncle_count_by_block_hash(self, block_hash: str, request_id: int=1):
        body = self.get_eth_get_uncle_count_by_block_hash_body(block_hash, request_id=request_id)
        res = self.make_post_request(body)
        result = process_http_response(res)
        if result:
            return hex_to_int(result)
        return result

    #NOTE: return 0 instead of None? bit more predictable this way
    def get_uncle_count_by_block_number(self, block_number: Union[int, str], request_id: int=1):
        body = self.get_eth_get_uncle_count_by_block_number_body(block_number, request_id=request_id)
        res = self.make_post_request(body)
        result = process_http_response(res)
        if result:
            return hex_to_int(result)
        return result

    def get_code(self, address: str, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_get_code_body(address, block_number=block_number, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def sign(self, address: str, data: str, request_id: int=1):
        body = self.get_eth_sign_body(address, data, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def sign_transaction(self, transaction: Transaction, request_id: int=1):
        body = self.get_eth_sign_transaction_body(transaction, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def send_transaction(self, transaction: Transaction, request_id: int=1):
        body = self.get_eth_send_transaction_body(transaction, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def send_raw_transaction(self, raw_transaction: str, request_id: int=1):
        body = self.get_eth_send_raw_transaction_body(raw_transaction, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def call(self, transaction: Transaction, request_id: int=1):
        body = self.get_eth_call_body(transaction, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def estimate_gas(self, transaction: Transaction, request_id: int=1):
        body = self.get_eth_estimate_gas_body(transaction, request_id=request_id)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

    #TODO: block parsers
    def get_block_by_number(self, block_number: Union[int, str], include_transaction_detail: bool=True, request_id: int=1):
        body = self.get_eth_get_block_by_number_body(block_number, include_transaction_detail=include_transaction_detail, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def get_block_by_hash(self, block_hash: str, include_transaction_detail: bool=True, request_id: int=1):
        body = self.get_eth_get_block_by_hash_body(block_hash, include_transaction_detail=include_transaction_detail, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def get_transaction_by_block_hash_and_index(self, block_hash: str, idx: int, request_id: int=1):
        body = self.get_eth_get_transaction_by_block_hash_and_index_body(block_hash, idx, request_id=request_id)
        res = self.make_post_request(body)
        return TransactionParser.from_raw_json(process_http_response(res)).to_json()

    def get_transaction_by_block_number_and_index(self, block_number: Union[int, str], idx: int, request_id: int=1):
        body = self.get_eth_get_transaction_by_block_number_and_index_body(block_number, idx, request_id=request_id)
        res = self.make_post_request(body)
        return TransactionParser.from_raw_json(process_http_response(res)).to_json()

    #TODO: receipt parser
    def get_transaction_receipt(self, transaction_hash: str, request_id: int=1):
        body = self.get_eth_get_transaction_receipt_body(transaction_hash, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)
