from typing import Union
from evm_client.core.utils import get_request_body
from evm_client.types import Transaction, EthFilter

class EthCore:

    @staticmethod
    def get_eth_protocol_version_body(request_id: int=1):
        return get_request_body("eth_protocolVersion", [], request_id=request_id)

    @staticmethod
    def get_eth_syncing_body(request_id: int=1):
        return get_request_body("eth_syncing", [], request_id=request_id)

    @staticmethod
    def get_eth_coinbase_body(request_id: int=1):
        return get_request_body("eth_coinbase", [], request_id=request_id)

    @staticmethod
    def get_eth_chain_id_body(request_id: int=1):
        return get_request_body("eth_chainId", [], request_id=request_id)

    @staticmethod
    def get_eth_mining_body(request_id: int=1):
        return get_request_body("eth_mining", [], request_id=request_id)

    @staticmethod
    def get_eth_hashrate_body(request_id: int=1):
        return get_request_body("eth_hashrate", [], request_id=request_id)

    @staticmethod
    def get_eth_gas_price_body(request_id: int=1):
        return get_request_body("eth_gasPrice", [], request_id=request_id)

    @staticmethod
    def get_eth_accounts_body(request_id: int=1):
        return get_request_body("eth_accounts", [], request_id=request_id)

    @staticmethod
    def get_eth_block_number_body(request_id: int=1):
        return get_request_body("eth_blockNumber", [], request_id=request_id)

    @staticmethod
    def get_eth_get_balance_body(address: str, block_number: Union[int, str]="latest", request_id: int=1):
        params = [address, str(hex(block_number)) if isinstance(block_number, int) else block_number]
        return get_request_body("eth_getBalance", params, request_id=request_id)

    @staticmethod
    def get_eth_get_storage_at_body(address: str, storage_position: int, block_number: Union[int, str]="latest", request_id: int=1):
        params = [address, str(hex(storage_position)), str(hex(block_number)) if isinstance(block_number, int) else block_number]
        return get_request_body("eth_getStorageAt", params, request_id=request_id)

    @staticmethod
    def get_eth_get_transaction_count_body(address: str, block_number: Union[int, str]="latest", request_id: int=1):
        params = [address, str(hex(block_number)) if isinstance(block_number, int) else block_number]
        return get_request_body("eth_getTransactionCount", params, request_id=request_id)

    @staticmethod
    def get_eth_get_block_transaction_count_by_hash_body(block_hash: str, request_id: int=1):
        return get_request_body("eth_getBlockTransactionCountByHash", [block_hash], request_id=request_id)

    @staticmethod
    def get_eth_get_block_transaction_count_by_number_body(block_number: Union[int, str]="latest", request_id: int=1):
        params = [str(hex(block_number)) if isinstance(block_number, int) else block_number]
        return get_request_body("eth_getBlockTransactionCountByNumber", params, request_id=request_id)

    @staticmethod
    def get_eth_get_uncle_count_by_block_hash_body(block_hash: str, request_id: int=1):
        return get_request_body("eth_getUncleCountByBlockHash", [block_hash], request_id=request_id)

    @staticmethod
    def get_eth_get_uncle_count_by_block_number_body(block_number: Union[int, str]="latest", request_id: int=1):
        params = [str(hex(block_number)) if isinstance(block_number, int) else block_number]
        return get_request_body("eth_getUncleCountByBlockNumber", params, request_id=request_id)

    @staticmethod
    def get_eth_get_code_body(address: str, block_number: Union[int, str]="latest", request_id: int=1):
        params = [address, str(hex(block_number)) if isinstance(block_number, int) else block_number]
        return get_request_body("eth_getCode", params, request_id=request_id)

    @staticmethod
    def get_eth_sign_body(address: str, data: str, request_id: int=1):
        return get_request_body("eth_sign", [address, data], request_id=request_id)

    @staticmethod
    def get_eth_sign_transaction_body(transaction: Transaction, request_id: int=1):
        return get_request_body("eth_signTransaction", [transaction.to_json()], request_id=request_id)

    @staticmethod
    def get_eth_send_transaction_body(transaction: Transaction, request_id: int=1):
        return get_request_body("eth_sendTransaction", [transaction.to_json()], request_id=request_id)

    @staticmethod
    def get_eth_send_raw_transaction_body(raw_transaction: str, request_id: int=1):
        return get_request_body("eth_sendRawTransaction", [raw_transaction], request_id=request_id)

    @staticmethod
    def get_eth_call_body(transaction: Transaction, request_id: int=1):
        return get_request_body("eth_call", [transaction.to_json()], request_id=request_id)

    @staticmethod
    def get_eth_estimate_gas_body(transaction: Transaction, request_id: int=1):
        return get_request_body("eth_estimateGas", [transaction.to_json()], request_id=request_id)

    @staticmethod
    def get_eth_get_block_by_hash_body(block_hash: str, include_transaction_detail: bool=True, request_id: int=1):
        return get_request_body("eth_getBlockByHash", [block_hash, include_transaction_detail], request_id=request_id)

    @staticmethod
    def get_eth_get_block_by_number_body(block_number: Union[int, str], include_transaction_detail: bool=True, request_id: int=1):
        params = [str(hex(block_number)) if isinstance(block_number, int) else block_number, include_transaction_detail]
        return get_request_body("eth_getBlockByNumber", params, request_id=request_id)

    @staticmethod
    def get_eth_get_transaction_by_hash_body(transaction_hash: str, request_id: int=1):
        return get_request_body("eth_getTransactionByHash", [transaction_hash], request_id=request_id)

    @staticmethod
    def get_eth_get_transaction_by_block_hash_and_index_body(block_hash: str, idx: int, request_id: int=1):
        return get_request_body("eth_getTransactionByBlockHashAndIndex", [block_hash, str(hex(idx))], request_id=request_id)

    @staticmethod
    def get_eth_get_transaction_by_block_number_and_index_body(block_number: Union[int, str], idx: int, request_id: int=1):
        params = [str(hex(block_number)) if isinstance(block_number, int) else block_number, hex(idx)]
        return get_request_body("eth_getTransactionByBlockNumberAndIndex", params, request_id=request_id)

    @staticmethod
    def get_eth_get_transaction_receipt_body(transaction_hash: str, request_id: int=1):
        return get_request_body("eth_getTransactionReceipt", [transaction_hash], request_id=request_id)

    @staticmethod
    def get_eth_get_uncle_by_block_hash_and_index_body(block_hash: str, idx: int, request_id: int=1):
        return get_request_body("eth_getUncleByBlockHashAndIndex", [block_hash, str(hex(idx))], request_id=request_id)

    @staticmethod
    def get_eth_get_uncle_by_block_number_and_index_body(block_number: Union[int, str], idx: int, request_id: int=1):
        params = [str(hex(block_number)) if isinstance(block_number, int) else block_number, hex(idx)]
        return get_request_body("eth_getUncleByBlockNumberAndIndex", params, request_id=request_id)

    @staticmethod
    def get_eth_new_filter_body(filter_: EthFilter, request_id: int=1):
        return get_request_body("eth_newFilter", [filter_.to_json()], request_id=request_id)

    @staticmethod
    def get_eth_new_block_filter_body(request_id: int=1):
        return get_request_body("eth_newBlockFilter", [], request_id=request_id)

    @staticmethod
    def get_eth_new_pending_transaction_filter_body(request_id: int=1):
        return get_request_body("eth_newPendingTransactionFilter", [], request_id=request_id)

    @staticmethod
    def get_eth_uninstall_filter_body(filter_id: str, request_id: int=1):
        return get_request_body("eth_uninstallFilter", [filter_id], request_id=request_id)

    @staticmethod
    def get_eth_get_filter_changes_body(filter_id: str, request_id: int=1):
        return get_request_body("eth_getFilterChanges", [filter_id], request_id=request_id)

    @staticmethod
    def get_eth_get_filter_logs_body(filter_id: str, request_id: int=1):
        return get_request_body("eth_getFilterLogs", [filter_id], request_id=request_id)

    @staticmethod
    def get_eth_get_logs_body(filter_: EthFilter, request_id: int=1):
        return get_request_body("eth_getLogs", [filter_.to_json()], request_id=request_id)
    
#    @staticmethod
#    def get_eth_simulate_v1_body(simulation: EthSimulation, block_number: Union[int, str], request_id: int=1):
#        pass
