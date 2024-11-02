from typing import Union
from evm_client.core import EthCore
from evm_client.sync_client.client_core import SyncClientCore
from evm_client.sync_client.utils import process_http_response
from evm_client.parsers import BlockParser, TransactionParser, ReceiptParser, LogParser
from evm_client.converters import convert_hex_to_int
from evm_client.types import Transaction, EthFilter

#TODO: some methods it makes sense to allow parser while other we should just force to a type and let the user deal with converting after
class SyncEthClient(SyncClientCore, EthCore):

    def __init__(
            self, 
            node_url,
            transaction_parser=TransactionParser(),
            block_parser=BlockParser(),
            receipt_parser=ReceiptParser(),
            log_parser=LogParser()
    ):
        super().__init__(node_url)
        self.default_transaction_parser = transaction_parser
        self.default_block_parser = block_parser
        self.default_receipt_parser = receipt_parser
        self.default_log_parser = log_parser

    def protocol_version(self, request_id: int=1):
        body = self.get_eth_protocol_version_body(request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

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
        return convert_hex_to_int(process_http_response(res))

    def block_number(self, request_id: int=1):
        body = self.get_eth_block_number_body(request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    def mining(self, request_id: int=1):
        body = self.get_eth_mining_body(request_id=request_id)
        res =  self.make_post_request(body)
        return process_http_response(res)

    def hashrate(self, request_id: int=1):
        body = self.get_eth_hashrate_body(request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    def gas_price(self, request_id: int=1):
        body = self.get_eth_gas_price_body(request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    #mostly expect this to not work on public nodes
    def accounts(self, request_id: int=1):
        body = self.get_eth_accounts_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def get_balance(self, address: str, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_get_balance_body(address, block_number=block_number, request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    def get_storage_at(self, address: str, storage_position:int, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_get_storage_at_body(address, storage_position, block_number=block_number, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def get_transaction_count(self, address: str, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_get_transaction_count_body(address, request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    def get_transaction(self, transaction_hash: str, request_id: int=1, parser=None):
        parser = parser or self.default_transaction_parser
        body = self.get_eth_get_transaction_by_hash_body(transaction_hash, request_id=request_id)
        res = self.make_post_request(body)
        return parser.parse(process_http_response(res))

    def get_block_transaction_count_by_hash(self, block_hash: str, request_id: int=1):
        body = self.get_eth_get_block_transaction_count_by_hash_body(block_hash, request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    def get_block_transaction_count_by_number(self, block_number: Union[int, str], request_id: int=1):
        body = self.get_eth_get_block_transaction_count_by_number_body(block_number, request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    def get_uncle_count_by_block_hash(self, block_hash: str, request_id: int=1):
        body = self.get_eth_get_uncle_count_by_block_hash_body(block_hash, request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    def get_uncle_count_by_block_number(self, block_number: Union[int, str], request_id: int=1):
        body = self.get_eth_get_uncle_count_by_block_number_body(block_number, request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

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

    def call(self, transaction: Transaction, decoder=None, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_call_body(transaction, block_number=block_number, request_id=request_id)
        res = self.make_post_request(body)
        result = process_http_response(res)
        return result if not decoder else decoder(result)

    def estimate_gas(self, transaction: Transaction, request_id: int=1):
        body = self.get_eth_estimate_gas_body(transaction, request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    def get_block_by_number(self, block_number: Union[int, str], include_transaction_detail: bool=True, request_id: int=1, parser=None):
        parser = parser or self.default_block_parser
        body = self.get_eth_get_block_by_number_body(block_number, include_transaction_detail=include_transaction_detail, request_id=request_id)
        res = self.make_post_request(body)
        return parser.parse(process_http_response(res))

    def get_block_by_hash(self, block_hash: str, include_transaction_detail: bool=True, request_id: int=1, parser=None):
        parser = parser or self.default_block_parser
        body = self.get_eth_get_block_by_hash_body(block_hash, include_transaction_detail=include_transaction_detail, request_id=request_id)
        res = self.make_post_request(body)
        return parser.parse(process_http_response(res))

    def get_transaction_by_block_hash_and_index(self, block_hash: str, idx: int, request_id: int=1, parser=None):
        parser = parser or self.default_transaction_parser
        body = self.get_eth_get_transaction_by_block_hash_and_index_body(block_hash, idx, request_id=request_id)
        res = self.make_post_request(body)
        return parser.parse(process_http_response(res))

    def get_transaction_by_block_number_and_index(self, block_number: Union[int, str], idx: int, request_id: int=1, parser=None):
        parser = parser or self.default_transaction_parser
        body = self.get_eth_get_transaction_by_block_number_and_index_body(block_number, idx, request_id=request_id)
        res = self.make_post_request(body)
        return parser.parse(process_http_response(res))

    def get_transaction_receipt(self, transaction_hash: str, request_id: int=1, parser=None):
        parser = parser or self.default_receipt_parser
        body = self.get_eth_get_transaction_receipt_body(transaction_hash, request_id=request_id)
        res = self.make_post_request(body)
        return parser.parse(process_http_response(res))

    def get_uncle_by_block_hash_and_index(self, block_hash: str, idx: int, request_id: int=1):
        body = self.get_eth_get_uncle_by_block_hash_and_index_body(block_hash, idx, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def get_uncle_by_block_number_and_index(self, block_number: Union[int, str], idx: int, request_id: int=1):
        body = self.get_eth_get_uncle_by_block_number_and_index_body(block_number, idx, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def blob_base_fee(self, request_id: int=1):
        body = self.get_eth_blob_base_fee_body(request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    def new_filter(self, filter_: EthFilter, request_id: int=1):
        body = self.get_eth_new_filter_body(filter_, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def new_block_filter(self, request_id: int=1):
        body = self.get_eth_new_block_filter_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def new_pending_transaction_filter(self, request_id: int=1):
        body = self.get_eth_new_pending_transaction_filter_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def uninstall_filter(self, filter_id: str, request_id: int=1):
        body = self.get_eth_uninstall_filter_body(filter_id, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def get_filter_changes(self, filter_id: str, request_id: int=1):
        body = self.get_eth_get_filter_changes_body(filter_id, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def get_filter_logs(self, filter_id: str, request_id: int=1, parser=None):
        parser = parser or self.default_log_parser
        body = self.get_eth_get_filter_logs_body(filter_id, request_id=request_id)
        res = self.make_post_request(body)
        return parser.parse_multiple(process_http_response(res))

    def get_logs(self, filter_: EthFilter, request_id: int=1, parser=None, decoder=None):
        parser = parser or self.default_log_parser
        body = self.get_eth_get_logs_body(filter_, request_id=request_id)
        res = self.make_post_request(body)
        parsed = parser.parse_multiple(process_http_response(res))
        return decoder(parsed) if decoder else parsed

    def get_account(self, address: str, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_get_account_body(address, block_number, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def get_block_receipts(self, block_number: Union[int, str]="latest", request_id: int=1, parser=None):
        parser = parser or self.default_receipt_parser
        body = self.get_eth_get_block_receipts_body(block_number, request_id=request_id)
        res = self.make_post_request(body)
        return parser.parse_multiple(process_http_response(res))

    def max_priority_fee_per_gas(self, request_id: int=1):
        body = self.get_eth_max_priority_fee_per_gas_body(request_id=request_id)
        res = self.make_post_request(body)
        return convert_hex_to_int(process_http_response(res))

    def subscribe(self, subscription_name: str, include_transaction_detail: bool=True, data: Union[list, str]=None, request_id: int=1):
        body = self.get_eth_subscribe_body(subscription_name, include_transaction_detail, data=data, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def unsubscribe(self, subscription_id: str, request_id: int=1):
        body = self.get_eth_unsubscribe_body(subscription_id, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def create_access_list(self, transaction: Transaction, block_number: Union[int, str]="latest", request_id: int=1):
        body = self.get_eth_create_access_list_body(transaction, block_number, request_id=request_id)
        res = self.make_post_request(body)
        result = process_http_response(res)
        #NOTE: do not love doing this type conversion in this method directly, but it's a bit weird as the access list in the transaction is a subset of the access list returned here
        result['gasUsed'] = convert_hex_to_int(result['gasUsed'])
        return result
