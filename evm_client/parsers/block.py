from evm_client.parsers.base import ParsedObject, Parser
from evm_client.parsers import TransactionParser
from evm_client.converters import convert_hex_to_int, do_not_convert, convert_hex_to_datetime

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
            transaction_parser=TransactionParser()
    ):
        self.base_fee_per_gas_converter = base_fee_per_gas_converter
        self.blob_gas_used_converter = blob_gas_used_converter
        self.difficulty_converter = difficulty_converter
        self.excess_blob_gas_converter = excess_blob_gas_converter
        self.extra_data_converter = extra_data_converter
        self.gas_limit_converter = gas_limit_converter
        self.gas_used_converter = gas_used_converter
        self.hash_converter = hash_converter
        self.logs_bloom_converter = logs_bloom_converter
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
        self.total_difficulty_converter = total_difficulty_converter
        self.transaction_parser = transaction_parser

class BlockParser(Parser):

    def __init__(self, cfg: BlockParserConfig=BlockParserConfig()):
        self.cfg = cfg

    def parse(self, block_dict):
        return ParsedBlock(
            base_fee_per_gas=self.cfg.base_fee_per_gas_converter(block_dict.get('baseFeePerGas')),
            blob_gas_used=self.cfg.blob_gas_used_converter(block_dict.get('blobGasUsed')),
            difficulty=self.cfg.difficulty_converter(block_dict.get('difficulty')),
            excess_blob_gas=self.cfg.excess_blob_gas_converter(block_dict.get('excessBlobGas')),
            extra_data=self.cfg.extra_data_converter(block_dict.get('extraData')),
            gas_limit=self.cfg.gas_limit_converter(block_dict.get('gasLimit')),
            gas_used=self.cfg.gas_used_converter(block_dict.get('gasUsed')),
            hash_=self.cfg.hash_converter(block_dict.get('hash')),
            logs_bloom=self.cfg.logs_bloom_converter(block_dict.get('logsBloom')),
            miner=self.cfg.miner_converter(block_dict.get('miner')),
            mix_hash=self.cfg.mix_hash_converter(block_dict.get('mixHash')),
            nonce=self.cfg.nonce_converter(block_dict.get('nonce')),
            number=self.cfg.number_converter(block_dict.get('number')),
            parent_beacon_block_root=self.cfg.parent_beacon_block_root_converter(block_dict.get('parentBeaconBlockRoot')),
            parent_hash=self.cfg.parent_hash_converter(block_dict.get('parentHash')),
            receipts_root=self.cfg.receipts_root_converter(block_dict.get('receiptsRoot')),
            sha3_uncles=self.cfg.sha3_uncles_converter(block_dict.get('sha3Uncles')),
            size=self.cfg.size_converter(block_dict.get('size')),
            state_root=self.cfg.state_root_converter(block_dict.get('stateRoot')),
            timestamp=self.cfg.timestamp_converter(block_dict.get('timestamp')),
            total_difficulty=self.cfg.total_difficulty_converter(block_dict.get('totalDifficulty')),
            #TODO: handle for case where only tx hashes are returned
            transactions=self.cfg.transaction_parser.parse_multiple(block_dict.get('transactions'))
        ).to_dict()


