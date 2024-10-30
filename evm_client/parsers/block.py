from evm_client.parsers import parse_raw_transactions, TransactionParserConfig
from evm_client.converters import convert_hex_to_int, do_not_convert, convert_hex_to_datetime
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

class BlockParserConfig:

    def __init__(
            self,
            base_fee_per_gas_converter=convert_hex_to_int,
            blob_gas_used_converter=convert_hex_to_int,
            difficulty_converter=convert_hex_to_int,
            excess_blob_gas_converter=convert_hex_to_int,
            extra_data_converter=do_not_convert,
            gas_limit_converter=convert_hex_to_int,
            gas_used_converter=convert_hex_to_int,
            hash_converter=do_not_convert,
            logs_bloom_converter=do_not_convert,
            miner_converter=do_not_convert,
            mix_hash_converter=do_not_convert,
            nonce_converter=convert_hex_to_int,
            number_converter=convert_hex_to_int,
            parent_beacon_block_root_converter=do_not_convert,
            parent_hash_converter=do_not_convert,
            receipts_root_converter=do_not_convert,
            sha3_uncles_converter=do_not_convert,
            size_converter=convert_hex_to_int,
            state_root_converter=do_not_convert,
            timestamp_converter=convert_hex_to_datetime,
            total_difficulty_converter=convert_hex_to_int,
            #NOTE: must handle for list of transactions, not just single tx
            transaction_parser=parse_raw_transactions,
            transaction_parser_config=TransactionParserConfig()
    ):
        self.base_fee_per_gas_converter = base_fee_per_gas_converter
        self.blob_gas_used_converter = blob_gas_used_converter
        self.difficulty_converter = difficulty_converter
        self.excess_blob_gas_converter = excess_blob_gas_converter
        self.extra_data_converter = extra_data_converter
        self.gas_limit_converter = gas_limit_converter
        self.gas_used_converter = gas_used_converter
        self.hash_converter = hash_converter
        self.log_bloom_converter = logs_bloom_converter
        self.miner_converter = miner_converter
        self.mix_hash_converter = mix_hash_converter
        self.nonce_converter = nonce_converter
        self.number_converter = number_converter
        self.parent_beacon_block_root_converter = parent_beacon_block_root_converter
        self.parent_hash_converter = parent_hash_converter
        self.receipts_root_converter = receipts_root_converter
        self.sha3_uncles_converter = sha3_uncles_converter
        self.size_converter = size_converter
        self.state_root_converter = state_root_converter
        self.timestamp_converter = timestamp_converter
        self.total_dfifficulty_converter = total_difficulty_converter
        self.transaction_parser = transactions_parser
        self.transaction_parser_config = transactions_parser_config

#TODO: may be missing fields from other networks we'll have to fill as we test through
def parse_raw_block(block_dict, block_cfg=BlockParserConfig()):
    return ParsedBlock(
        base_fee_per_gas=block_cfg.base_fee_per_gas_converter(block_dict.get('baseFeePerGas')),
        blob_gas_used=block_cfg.blob_gas_used_converter(block_dict.get('blobGasUsed')),
        difficulty=block_cfg.difficulty_converter(block_dict.get('difficulty')),
        excess_blob_gas=block_cfg.excess_blob_gas_converter(block_dict.get('excessBlobGas')),
        extra_data=block_cfg.extra_data_converter(block_dict.get('extraData')),
        gas_limit=block_cfg.gas_limit_converter(block_dict.get('gasLimit')),
        gas_used=block_cfg.gas_used_converter(block_dict.get('gasUsed')),
        hash_=block_cfg.hash_converter(block_dict.get('hash')),
        logs_bloom=block_cfg.logs_bloom_converter(block_dict.get('logsBloom')),
        miner=block_cfg.miner_converter(block_dict.get('miner')),
        mix_hash=block_cfg.mix_hash_converter(block_dict.get('mixHash')),
        nonce=block_cfg.nonce_converter(block_dict.get('nonce')),
        number=block_cfg.number_converter(block_dict.get('number')),
        parent_beacon_block_root=block_cfg.parent_beacon_block_root_converter(block_dict.get('parentBeaconBlockRoot')),
        parent_hash=block_cfg.parent_hash_converter(block_dict.get('parentHash')),
        receipts_root=block_cfg.receipts_root_converter(block_dict.get('receiptsRoot')),
        sha3_uncles=block_cfg.sha3_uncles_converter(block_dict.get('sha3Uncles')),
        size=block_cfg.size_converter(block_dict.get('size')),
        state_root=block_cfg.state_root_converter(block_dict.get('stateRoot')),
        timestamp=block_cfg.timestamp_converter(block_dict.get('timestamp')),
        total_difficulty=block_cfg.total_difficulty_converter(block_dict.get('totalDifficulty')),
        #TODO: handle for case where only tx hashes are returned
        transactions=transactions_parser(block_dict.get('transactions'), tx_cfg=block_cfg.transaction_parser_config)
    ).to_dict()

def parse_raw_blocks(block_dict_list, block_cfg=BlockParserConfig()):
    if not block_dict_list:
        return []
    return [parse_raw_block(b, block_cfg=block_cfg) for b in block_dict_list]


