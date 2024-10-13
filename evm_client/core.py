from typing import List, Union
from evm_client.types import Transaction, EthFilter

def get_request_body(method: str, params: List[Union[int, str]], request_id: int=1):
    return {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': request_id,
    }

#focus on namespaces/methods that are useful to average user... lots of these are rarely used

class AdminNamespaceCore:

    @staticmethod
    def get_admin_add_peer_body(peer_url: str, request_id: int=1):
        return get_request_body("admin_adPeer", [peer_url], request_id=request_id)

    @staticmethod
    def get_admin_add_trusted_peer_body(peer_url: str, request_id: int=1):
        return get_request_body("admine_addTrustedPeer", [peer_url], request_id=request_id)

    @staticmethod
    def get_admin_datadir_body(request_id: int=1):
        return get_request_body("admin_datadir", [], request_id=request_id)

    @staticmethod
    def get_admin_export_chain_body(fname: str, from_block: int, to_block: int, request_id: int=1):
        params = [fname, hex(from_block), hex(to_block)]
        return get_request_body("admin_exportChain", params, request_id=request_id)

    @staticmethod
    def get_admin_import_chain_body(fname: str, request_id: int=1):
        return get_request_body("admin_importChain", [fname], request_id=request_id)

    @staticmethod
    def get_admin_node_info_body(request_id: int=1):
        return get_request_body("admin_nodeInfo", [], request_id=request_id)

    @staticmethod
    def get_admin_peer_events_body(request_id: int=1):
        return get_request_body("admin_peerEvents", [], request_id=request_id)

    @staticmethod
    def get_admin_peers_body(request_id: int=1):
        return get_request_body("admin_peers", [], request_id=request_id)

    @staticmethod
    def get_admin_remove_peer_body(peer_url: str, request_id: int=1):
        return get_request_body("admin_removePeer", [peer_url], request_id=request_id)

    @staticmethod
    def get_admin_remove_trusted_peer_body(peer_url: str, request_id: int=1):
        return get_request_body("admin_removeTrustedPeer", [peer_url], request_id=request_id)

    @staticmethod
    def get_admin_start_http_body(host: str="localhost", port: int=8545, cors: str="", apis: str="eth,net,web3", request_id: int=1):
        params = [host, str(hex(port)), cors, apis]
        return get_request_body("admin_startHTTP", params, request_id=request_id)

    @staticmethod
    def get_admin_start_ws_body(host: str="localhost", port: int=8545, cors: str="", apis: str="eth,net,web3", request_id: int=1):
        params = [host, str(hex(port)), cors, apis]
        return get_request_body("admin_startWS", params, request_id=request_id)

    @staticmethod
    def get_admin_stop_http_body(request_id: int=1):
        return get_request_body("admin_stopHTTP", [], request_id=request_id)

    @staticmethod
    def get_admin_stop_ws_body(request_id: int=1):
        return get_request_body("admin_stopWS", [], request_id=request_id)


class DebugNamespaceCore:

    #TODO: determine input types
    @staticmethod
    def get_debug_account_range_body():
        pass

    @staticmethod
    def get_debug_backtrace_at_body(fname: str, line: int, request_id: int=1):
        return get_request_body("debug_backtraceAt", [f"{fname}:{line}"], request_id=request_id)

    @staticmethod
    def get_debug_block_profile_body(fname: str, duration: int, request_id: int=1):
        params = [fname, str(hex(duration))]
        return get_request_body("debug_blockProfile", params, request_id=request_id)

    @staticmethod
    def get_debug_chaindb_compact_body(request_id: int=1):
        return get_request_body("debug_chaindbCompact", [], request_id=request_id)

    @staticmethod
    def get_debug_chaindb_property_body(property: str, request_id: int=1):
        return get_request_body("debug_chaindbProperty", [property], request_id=request_id)

    @staticmethod
    def get_debug_cpu_profile_body(fname: str, duration: int, request_id: int=1):
        return get_request_body("debug_cpuProfile", [fname, str(hex(duration))], request_id=request_id)

    @staticmethod
    def get_debug_db_ancient_body(kind: str, n: int, request_id: int=1):
        return get_request_body("debug_dbAncient", [kind, str(hex(n))], request_id=request_id)

    @staticmethod
    def get_debug_db_ancients_body(request_id: int=1):
        return get_request_body("debug_dbAncients", [], request_id=request_id)

    @staticmethod
    def get_debug_db_get_body(key: str, request_id: int=1):
        return get_request_body("debug_dbGet", [key], request_id=request_id)

    @staticmethod
    def get_debug_dump_block_body(block_number: Union[int, str], request_id: int=1):
        params = [str(hex(block_number)) if isinstance(block_number, int) else block_number]
        return get_request_body("debug_dumpBlock", params, request_id=request_id)

    @staticmethod
    def get_debug_free_os_memory_body(request_id: int=1):
        return get_request_body("debug_freeOSMemory", [], request_id=request_id)

    @staticmethod
    def get_debug_freeze_client_body(node: str, request_id: int=1):
        return get_request_body("debug_freezeClient", [node], request_id=request_id)

    @staticmethod
    def get_debug_gc_stats_body(request_id: int=1):
        return get_request_body("debug_gcStats", [], request_id=request_id)

    @staticmethod
    def get_debug_get_accessible_state_body(from_: int, to: int, request_id: int=1):
        return get_request_body("debug_getAccessibleState", [str(hex(from_)), str(hex(to))], request_id=request_id)

    @staticmethod
    def get_debug_get_bad_blocks_body(request_id: int=1):
        return get_request_body("debug_getBadBlocks", [], request_id=request_id)

    @staticmethod
    def get_debug_get_raw_block_body(block_n_or_hash: Union[int, str], request_id: int=1):
        params = [str(hex(block_n_or_hash)) if isinstance(block_n_or_hash, int) else block_n_or_hash]
        return get_request_body("debug_getRawBlock", params, request_id=request_id)

    @staticmethod
    def get_debug_get_raw_header_body(block_n_or_hash: Union[int, str], request_id: int=1):
        params = [str(hex(block_n_or_hash)) if isinstance(block_n_or_hash, int) else block_n_or_hash]
        return get_request_body("debug_getRawHeader", params, request_id=request_id)

    @staticmethod
    def get_debug_get_raw_transaction_body(transaction_hash: str, request_id: int=1):
        return get_request_body("debug_getRawTransaction", [transaction_hash], request_id=request_id)

    @staticmethod
    def get_debug_get_modified_accounts_by_hash_body(from_block_hash: str, to_block_hash: str, request_id: int=1):
        return get_request_body("debug_getModifiedAccountsByHash", [from_block_hash, to_block_hash], request_id=request_id)

    @staticmethod
    def get_debug_get_modified_accounts_by_number_body(from_block_n: Union[int, str], to_block_n: Union[int, str], request_id: int=1):
        params = [str(hex(from_block_n)) if isinstance(from_block_n, int) else from_block_n, str(hex(to_block_n)) if isinstance(to_block_n, int) else to_block_n]
        return get_request_body("debug_getModifiedAccountsByNumber", params, request_id=request_id)

    @staticmethod
    def get_debug_get_raw_receipts_body(block_n_or_hash: Union[int, str], request_id: int=1):
        params = [str(hex(block_n_or_hash)) if isinstance(block_n_or_hash, int) else block_n_or_hash]
        return get_request_body("debug_getRawReceipts", params, request_id=request_id)

    @staticmethod
    def get_debug_go_trace_body(fname: str, duration: int, request_id: int=1):
        return get_request_body("debug_goTrace", [fname, str(hex(duration))], request_id=request_id)




class Web3NamespaceCore:
    
    @staticmethod
    def get_web3_client_version_body(request_id: int=1):
        return get_request_body("web3_clientVersion", [], request_id=request_id)

    @staticmethod
    def get_web3_sha3_body(data: str, request_id: int=1):
        return get_request_body("web3_sha3", [data], request_id=request_id)


class NetNamespaceCore:

    @staticmethod
    def get_net_version_body(request_id: int=1):
        return get_request_body("net_version", [], request_id=request_id)

    @staticmethod
    def get_net_listening_body(request_id: int=1):
        return get_request_body("net_listening", [], request_id=request_id)

    @staticmethod
    def get_net_peer_count_body(request_id: int=1):
        return get_request_body("net_peerCount", [], request_id=request_id)

class EthNamespaceCore:

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
    def get_eth_block_transaction_count_by_number_body(block_number: Union[int, str]="latest", request_id: int=1):
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
        params = [address, str(hex(block_number)) if isinstance(block_number) else block_number]
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
    def get_eth_get_block_by_hash_body(block_hash: str, request_id: int=1):
        return get_request_body("eth_getBlockByHash", [block_hash], request_id=request_id)

    @staticmethod
    def get_eth_get_block_by_number_body(block_number: Union[int, str], request_id: int=1):
        params = [str(hex(block_number)) if isinstance(block_number, int) else block_number]
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
