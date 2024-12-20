from evm_client.parsers.base import ParsedObject, Parser
from evm_client.converters import convert_hex_to_int

class ParsedLog(ParsedObject):

    def __init__(
        self,
        address=None,
        topics=None,
        data=None,
        block_number=None,
        transaction_hash=None,
        transaction_index=None,
        block_hash=None,
        log_index=None,
        removed=None
    ):
        self.address = address
        self.topics = topics
        self.data = data
        self.block_number = block_number
        self.transaction_hash = transaction_hash
        self.transaction_index = transaction_index
        self.block_hash = block_hash
        self.log_index = log_index
        self.removed = removed

class LogParserConfig:

    def __init__(
            self,
            address_converter=None,
            topics_converter=None,
            data_converter=None,
            block_number_converter=None,
            transaction_hash_converter=None,
            transaction_index_converter=None,
            block_hash_converter=None,
            log_index_converter=None,
            removed_converter=None
    ):
        self.address_converter = address_converter
        self.topics_converter = topics_converter
        self.data_converter = data_converter
        self.block_number_converter = block_number_converter
        self.transaction_hash_converter = transaction_hash_converter
        self.transaction_index_converter = transaction_index_converter
        self.block_hash_converter = block_hash_converter
        self.log_index_converter = log_index_converter
        self.removed_converter = removed_converter

    @classmethod
    def default(cls):
        return cls(
            block_number_converter=convert_hex_to_int,
            transaction_index_converter=convert_hex_to_int,
            log_index_converter=convert_hex_to_int
        )

class LogParser(Parser):

    def __init__(self, cfg: LogParserConfig=LogParserConfig.default()):
        self.cfg = cfg

    def parse(self, log_dict):
        return ParsedLog(
            address=self.apply_converter(self.cfg.address_converter, log_dict.get('address')),
            topics=self.apply_converter(self.cfg.topics_converter, log_dict.get('topics')),
            data=self.apply_converter(self.cfg.data_converter, log_dict.get('data')),
            block_number=self.apply_converter(self.cfg.block_number_converter, log_dict.get('blockNumber')),
            transaction_hash=self.apply_converter(self.cfg.transaction_hash_converter, log_dict.get('transactionHash')),
            transaction_index=self.apply_converter(self.cfg.transaction_index_converter, log_dict.get('transactionIndex')),
            block_hash=self.apply_converter(self.cfg.block_hash_converter, log_dict.get('blockHash')),
            log_index=self.apply_converter(self.cfg.log_index_converter, log_dict.get('logIndex')),
            removed=self.apply_converter(self.cfg.removed_converter, log_dict.get('removed'))
        ).to_dict()
