from typing import List, Union, Optional
from evm_client.types import Transaction, EthFilter

def generate_json_rpc(method: str, params: List[Union[int, str]], request_id: int=1):
    return {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': request_id,
    }

class AdminNamespaceCore:

    @staticmethod
    def get_admin_add_peer_body(peer_url: str, request_id: int=1):
        return generate_json_rpc("admin_adPeer", [peer_url], request_id=request_id)

    @staticmethod
    def get_admin_add_trusted_peer_body(peer_url: str, request_id: int=1):
        return generate_json_rpc("admine_addTrustedPeer", [peer_url], request_id=request_id)

    @staticmethod
    def get_admin_datadir_body(request_id: int=1):
        return generate_json_rpc("admin_datadir", [], request_id=request_id)

    @staticmethod
    def get_admin_export_chain_body(fname: str, from_block: int, to_block: int, request_id: int=1):
        params = [fname, hex(from_block), hex(to_block)]
        return generate_json_rpc("admin_exportChain", params, request_id=request_id)

    @staticmethod
    def get_admin_import_chain_body(fname: str, request_id: int=1):
        return generate_json_rpc("admin_importChain", [fname], request_id=request_id)

    @staticmethod
    def get_admin_node_info_body(request_id: int=1):
        return generate_json_rpc("admin_nodeInfo", [], request_id=request_id)


class Web3NamespaceCore:
    
    @staticmethod
    def get_web3_client_version_body(request_id: int=1):
        return generate_json_rpc("web3_clientVersion", [], request_id=request_id)

    @staticmethod
    def get_web3_sha3_body(data: str, request_id: int=1):
        return generate_json_rpc("web3_sha3", [data], request_id=request_id)


class NetNamespaceCore:

    @staticmethod
    def get_net_version_body(request_id: int=1):
        return generate_json_rpc("net_version", [], request_id=request_id)

    @staticmethod
    def get_net_listening_body(request_id: int=1):
        return generate_json_rpc("net_listening", [], request_id=request_id)

    @staticmethod
    def get_net_peer_count_body(request_id: int=1):
        return generate_json_rpc("net_peerCount", [], request_id=request_id)

class EthNamespaceCore:

    @staticmethod
    def get_eth_protocol_version_body(request_id: int=1):
        method = "eth_protocolVersion"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_syncing_body(request_id: int=1):
        method = "eth_syncing"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_coinbase_body(request_id: int=1):
        method = "eth_coinbase"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_chain_id_body(request_id: int=1):
        method = "eth_chainId"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_mining_body(request_id: int=1):
        method = "eth_mining"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_hashrate_body(request_id: int=1):
        method = "eth_hashrate"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_gas_price_body(request_id: int=1):
        method = "eth_gasPrice"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_accounts_body(request_id: int=1):
        method = "eth_accounts"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_block_number_body(request_id: int=1):
        method = "eth_blockNumber"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_get_balance_body(address: str, block_number: Union[int, str]="latest", request_id: int=1):
        method = "eth_getBalance"
        params = [address, hex(block_number) if isinstance(block_number, int) else block_number]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_storage_at_body(address: str, storage_position: int, block_number: Union[int, str]="latest", request_id: int=1):
        method = "eth_getStorageAt"
        params = [address, storage_position, hex(block_number) if isinstance(block_number, int) else block_number]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_transaction_count_body(address: str, block_number: Union[int, str]="latest", request_id: int=1):
        method = "eth_getTransactionCount"
        params = [address, hex(block_number) if isinstance(block_number, int) else block_number]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_block_transaction_count_by_hash_body(block_hash: str, request_id: int=1):
        method = "eth_getBlockTransactionCountByHash"
        params = [block_hash]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_block_transaction_count_by_number_body(block_number: Union[int, str]="latest", request_id: int=1):
        method = "eth_getBlockTransactionCountByNumber"
        params = [hex(block_number) if isinstance(block_number, int) else block_number]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_uncle_count_by_block_hash_body(block_hash: str, request_id: int=1):
        method = "eth_getUncleCountByBlockHash"
        params = [block_hash]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_uncle_count_by_block_number_body(block_number: Union[int, str]="latest", request_id: int=1):
        method = "eth_getUncleCountByBlockNumber"
        params = [hex(block_number) if isinstance(block_number, int) else block_number]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_code_body(address: str, block_number: Union[int, str]="latest", request_id: int=1):
        method = "eth_getCode"
        params = [address, hex(block_number) if isinstance(block_number) else block_number]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_sign_body(address: str, data: str, request_id: int=1):
        method = "eth_sign"
        params = [address, data]
        return generate_json_rpc(address, data, request_id=request_id)

    @staticmethod
    def get_eth_sign_transaction_body(transaction: Transaction, request_id: int=1):
        method = "eth_signTransaction"
        params = [transaction.to_json()]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_send_transaction_body(transaction: Transaction, request_id: int=1):
        method = "eth_sendTransaction"
        params = [transaction.to_json()]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_send_raw_transaction_body(raw_transaction: str, request_id: int=1):
        method = "eth_sendRawTransaction"
        params = [raw_transaction]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_call_body(transaction: Transaction, request_id: int=1):
        method = "eth_call"
        params = [transaction.to_json()]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_estimate_gas_body(transaction: Transaction, request_id: int=1):
        method = "eth_estimateGas"
        params = [transaction.to_json()]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_block_by_hash_body(block_hash: str, request_id: int=1):
        method = "eth_getBlockByHash"
        params = [block_hash]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_block_by_number_body(block_number: Union[int, str], request_id: int=1):
        method = "eth_getBlockByNumber"
        params = [hex(block_number) if isinstance(block_number, int) else block_number]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_transaction_by_hash_body(transaction_hash: str, request_id: int=1):
        method = "eth_getTransactionByHash"
        params = [transaction_hash]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_transaction_by_block_hash_and_index_body(block_hash: str, idx: int, request_id: int=1):
        method = "eth_getTransactionByBlockHashAndIndex"
        params = [block_hash, hex(idx)]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_transaction_by_block_number_and_index_body(block_number: Union[int, str], idx: int, request_id: int=1):
        method = "eth_getTransactionByBlockNumberAndIndex"
        params = [hex(block_number) if isinstance(block_number, int) else block_number, hex(idx)]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_transaction_receipt_body(transaction_hash: str, request_id: int=1):
        method = "eth_getTransactionReceipt"
        params = [transaction_hash]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_uncle_by_block_hash_and_index_body(block_hash: str, idx: int, request_id: int=1):
        method = "eth_getUncleByBlockHashAndIndex"
        params = [block_hash, hex(idx)]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_uncle_by_block_number_and_index_body(block_number: Union[int, str], idx: int, request_id: int=1):
        method = "eth_getUncleByBlockNumberAndIndex"
        params = [hex(block_number) if isinstance(block_number, int) else block_number, hex(idx)]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_new_filter_body(filter_: EthFilter, request_id: int=1):
        method = "eth_newFilter"
        params = [filter_.to_json()]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_new_block_filter_body(request_id: int=1):
        method = "eth_newBlockFilter"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_new_pending_transaction_filter_body(request_id: int=1):
        method = "eth_newPendingTransactionFilter"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_uninstall_filter_body(filter_id: str, request_id: int=1):
        method = "eth_uninstallFilter"
        params = [filter_id]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_filter_changes_body(filter_id: str, request_id: int=1):
        method = "eth_getFilterChanges"
        params = [filter_id]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_filter_logs_body(filter_id: str, request_id: int=1):
        method = "eth_getFilterLogs"
        params = [filter_id]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_logs_body(filter_: EthFilter, request_id: int=1):
        method = "eth_getLogs"
        params = [filter_.to_json()]
        return generate_json_rpc(method, params, request_id=request_id)
