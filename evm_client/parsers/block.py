from evm_client.parsers.base import ParsedObject, Parser
from evm_client.parsers import TransactionParser
from evm_client.converters import convert_hex_to_int, convert_hex_to_datetime

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

    #TODO: rather than using do_not_convert function, just set these to None, then in the converter check if it's None and leave the value as is if so
    def __init__(
            self,
            base_fee_per_gas_converter=None,
            blob_gas_used_converter=None,
            difficulty_converter=None,
            excess_blob_gas_converter=None,
            extra_data_converter=None,
            gas_limit_converter=None,
            gas_used_converter=None,
            hash_converter=None,
            logs_bloom_converter=None,
            miner_converter=None,
            mix_hash_converter=None,
            nonce_converter=None,
            number_converter=None,
            parent_beacon_block_root_converter=None,
            parent_hash_converter=None,
            receipts_root_converter=None,
            sha3_uncles_converter=None,
            size_converter=None,
            state_root_converter=None,
            timestamp_converter=None,
            total_difficulty_converter=None,
            #NOTE: must handle for list of transactions, not just single tx
            transaction_parser=None
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

    @classmethod
    def default(cls):
        return cls(
            base_fee_per_gas_converter=convert_hex_to_int,
            blob_gas_used_converter=convert_hex_to_int,
            difficulty_converter=convert_hex_to_int,
            excess_blob_gas_converter=convert_hex_to_int,
            gas_limit_converter=convert_hex_to_int,
            gas_used_converter=convert_hex_to_int,
            nonce_converter=convert_hex_to_int,
            number_converter=convert_hex_to_int,
            size_converter=convert_hex_to_int,
            timestamp_converter=convert_hex_to_datetime,
            total_difficulty_converter=convert_hex_to_int,
            transaction_parser=TransactionParser()
        )

class BlockParser(Parser):

    def __init__(self, cfg: BlockParserConfig=BlockParserConfig.default()):
        self.cfg = cfg

    def parse(self, block_dict):
        return ParsedBlock(
            base_fee_per_gas=self.apply_converter(self.cfg.base_fee_per_gas_converter, block_dict.get('baseFeePerGas')),
            blob_gas_used=self.apply_converter(self.cfg.blob_gas_used_converter, block_dict.get('blobGasUsed')),
            difficulty=self.apply_converter(self.cfg.difficulty_converter, block_dict.get('difficulty')),
            excess_blob_gas=self.apply_converter(self.cfg.excess_blob_gas_converter, block_dict.get('excessBlobGas')),
            extra_data=self.apply_converter(self.cfg.extra_data_converter, block_dict.get('extraData')),
            gas_limit=self.apply_converter(self.cfg.gas_limit_converter, block_dict.get('gasLimit')),
            gas_used=self.apply_converter(self.cfg.gas_used_converter, block_dict.get('gasUsed')),
            hash_=self.apply_converter(self.cfg.hash_converter, block_dict.get('hash')),
            logs_bloom=self.apply_converter(self.cfg.logs_bloom_converter, block_dict.get('logsBloom')),
            miner=self.apply_converter(self.cfg.miner_converter, block_dict.get('miner')),
            mix_hash=self.apply_converter(self.cfg.mix_hash_converter, block_dict.get('mixHash')),
            nonce=self.apply_converter(self.cfg.nonce_converter, block_dict.get('nonce')),
            number=self.apply_converter(self.cfg.number_converter, block_dict.get('number')),
            parent_beacon_block_root=self.apply_converter(self.cfg.parent_beacon_block_root_converter, block_dict.get('parentBeaconBlockRoot')),
            parent_hash=self.apply_converter(self.cfg.parent_hash_converter, block_dict.get('parentHash')),
            receipts_root=self.apply_converter(self.cfg.receipts_root_converter, block_dict.get('receiptsRoot')),
            sha3_uncles=self.apply_converter(self.cfg.sha3_uncles_converter, block_dict.get('sha3Uncles')),
            size=self.apply_converter(self.cfg.size_converter, block_dict.get('size')),
            state_root=self.apply_converter(self.cfg.state_root_converter, block_dict.get('stateRoot')),
            timestamp=self.apply_converter(self.cfg.timestamp_converter, block_dict.get('timestamp')),
            total_difficulty=self.apply_converter(self.cfg.total_difficulty_converter, block_dict.get('totalDifficulty')),
            #TODO: handle for case where only tx hashes are returned
            transactions=self.cfg.transaction_parser.parse_multiple(block_dict.get('transactions'))
        ).to_dict()


