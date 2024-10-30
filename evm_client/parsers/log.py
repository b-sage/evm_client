from evm_client.parsers.base import ParsedObject
from evm_client.converters import convert_hex_to_int, do_not_convert

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
            address_converter=do_not_convert,
            topics_converter=do_not_convert,
            data_converter=do_not_convert,
            block_number_converter=convert_hex_to_int,
            transaction_hash_converter=do_not_convert,
            transaction_index_converter=convert_hex_to_int,
            block_hash_converter=do_not_convert,
            log_index_converter=convert_hex_to_int,
            removed_converter=do_not_convert
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

DEFAULT_LOG_PARSER_CFG = LogParserConfig()

def parse_raw_log(log_dict, parser_cfg=DEFAULT_LOG_PARSER_CFG):
    return ParsedLog(
        address=parser_cfg.address_converter(log_dict.get('address')),
        topics=parser_cfg.topics_converter(log_dict.get('topics')),
        data=parser_cfg.data_converter(log_dict.get('data')),
        block_number=parser_cfg.block_number_converter(log_dict.get('blockNumber')),
        transaction_hash=parser_cfg.transaction_hash_converter(log_dict.get('transactionHash')),
        transaction_index=parser_cfg.transaction_index_converter(log_dict.get('transactionIndex')),
        block_hash=parser_cfg.block_hash_converter(log_dict.get('blockHash')),
        log_index=parser_cfg.log_index_converter(log_dict.get('logIndex')),
        removed=parser_cfg.removed_converter(log_dict.get('removed'))
    ).to_dict()

def parse_raw_logs(log_dict_list, parser_cfg=DEFAULT_LOG_PARSER_CFG):
    if not log_dict_list:
        return []
    return [parse_raw_log(l, parser_cfg=parser_cfg) for l in log_dict_list]
