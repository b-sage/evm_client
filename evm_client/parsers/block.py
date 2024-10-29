from evm_client.parsers import parse_raw_transactions, parse_raw_hex_to_int, parse_null
from evm_client.parsers.base import ParsedObject

class ParsedBlock(ParsedObject):

    def __init__(
        self,
        base_fee_per_gas=None,
        blob_gas_used=None,
        difficulty=None,
        excess_blob_gas=None,
        extra_data=None,
        gas_limit=None,
        gas_used=None,
        hash_=None,
        logs_bloom=None,
        miner=None,
        mix_hash=None,
        nonce=None,
        number=None,
        parent_beacon_block_root=None,
        parent_hash=None,
        receipts_root=None,
        sha3_uncles=None,
        size=None,
        state_root=None,
        timestamp=None,
        total_difficulty=None,
        transactions=None
    ):
        self.base_fee_per_gas = base_fee_per_gas
        self.blob_gas_used = blob_gas_used
        self.difficulty = difficulty
        self.excess_blob_gas = excess_blob_gas
        self.extra_data = extra_data
        self.gas_limit = gas_limit
        self.gas_used = gas_used
        self.hash = hash_
        self.logs_bloom = logs_bloom
        self.miner = miner
        self.mix_hash = mix_hash
        self.nonce = nonce
        self.number = number
        self.parent_beacon_block_root = parent_beacon_block_root
        self.parent_hash = parent_hash
        self.receipts_root = receipts_root
        self.sha3_uncles = sha3_uncles
        self.size = size
        self.state_root = state_root
        self.timestamp = timestamp
        self.total_difficulty = total_difficulty
        self.transactions = transactions

#TODO: may be missing fields from other networks we'll have to fill as we test through
def parse_raw_block(
        block_dict,
        base_fee_per_gas_parser=parse_raw_hex_to_int,
        blob_gas_used_parser=parse_raw_hex_to_int,
        difficulty_parser=parse_raw_hex_to_int,
        excess_blob_gas_parser=parse_raw_hex_to_int,
        extra_data_parser=parse_null,
        gas_limit_parser=parse_raw_hex_to_int,
        gas_used_parser=parse_raw_hex_to_int,
        hash_parser=parse_null,
        logs_bloom_parser=parse_null,
        miner_parser=parse_null,
        mix_hash_parser=parse_null,
        nonce_parser=parse_raw_hex_to_int,
        number_parser=parse_raw_hex_to_int,
        parent_beacon_block_root_parser=parse_null,
        parent_hash_parser=parse_null,
        receipts_root_parser=parse_null,
        sha3_uncles_parser=parse_null,
        size_parser=parse_raw_hex_to_int,
        state_root_parser=parse_null,
        timestamp_parser=parse_raw_hex_to_int,
        total_difficulty_parser=parse_raw_hex_to_int,
        #NOTE: must handle for list of transactions, not just single tx
        transactions_parser=parse_raw_transactions
):
    return ParsedBlock(
        base_fee_per_gas=base_fee_per_gas_parser(block_dict.get('baseFeePerGas')),
        blob_gas_used=blob_gas_used_parser(block_dict.get('blobGasUsed')),
        difficulty=difficulty_parser(block_dict.get('difficulty')),
        excess_blob_gas=excess_blob_gas_parser(block_dict.get('excessBlobGas')),
        extra_data=extra_data_parser(block_dict.get('extraData')),
        gas_limit=gas_limit_parser(block_dict.get('gasLimit')),
        gas_used=gas_used_parser(block_dict.get('gasUsed')),
        hash_=hash_parser(block_dict.get('hash')),
        logs_bloom=logs_bloom_parser(block_dict.get('logsBloom')),
        miner=miner_parser(block_dict.get('miner')),
        mix_hash=mix_hash_parser(block_dict.get('mixHash')),
        nonce=nonce_parser(block_dict.get('nonce')),
        number=number_parser(block_dict.get('number')),
        parent_beacon_block_root=parent_beacon_block_root_parser(block_dict.get('parentBeaconBlockRoot')),
        parent_hash=parent_hash_parser(block_dict.get('parentHash')),
        receipts_root=receipts_root_parser(block_dict.get('receiptsRoot')),
        sha3_uncles=sha3_uncles_parser(block_dict.get('sha3Uncles')),
        size=size_parser(block_dict.get('size')),
        state_root=state_root_parser(block_dict.get('stateRoot')),
        timestamp=timestamp_parser(block_dict.get('timestamp')),
        total_difficulty=total_difficulty_parser(block_dict.get('totalDifficulty')),
        #TODO: handle for case where only tx hashes are returned
        transactions=transactions_parser(block_dict.get('transactions'))
    ).to_dict()

def parse_raw_blocks(block_dict_list):
    if not block_dict_list:
        return []
    return [parse_raw_block(b) for b in block_dict_list]


