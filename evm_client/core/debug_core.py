from typing import Union
from evm_client.core.utils import get_request_body

#TODO: lot of methods to cover here...

class DebugCore:

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

