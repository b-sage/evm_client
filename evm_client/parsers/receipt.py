from evm_client.parsers.base import ParsedObject
from evm_client.converters import convert_hex_to_int, do_not_convert
from evm_client.parsers import parse_raw_logs, DEFAULT_LOG_PARSER_CFG

class ParsedReceipt(ParsedObject):

    def __init__(
        self,
        block_hash=None,
        block_number=None,
        contract_address=None,
        cumulative_gas_used=None,
        effective_gas_price=None,
        from_=None,
        gas_used=None,
        logs=None,
        logs_bloom=None,
        status=None,
        to=None,
        transaction_hash=None,
        transaction_index=None,
        type_=None
    ):
        self.block_hash = block_hash
        self.block_number = block_number
        self.contract_address = contract_address
        self.cumulative_gas_used = cumulative_gas_used
        self.effective_gas_price = effective_gas_price
        self.from_ = from_
        self.gas_used = gas_used
        self.logs = logs
        self.logs_bloom = logs_bloom
        self.status = status
        self.to = to
        self.transaction_hash = transaction_hash
        self.transaction_index = transaction_index
        self.type = type_

class ReceiptParserConfig:

    def __init__(
        self,
        block_hash_converter=do_not_convert,
        block_number_converter=convert_hex_to_int,
        contract_address_converter=do_not_convert,
        cumulative_gas_used_converter=convert_hex_to_int,
        effective_gas_price_converter=convert_hex_to_int,
        from_converter=do_not_convert,
        gas_used_converter=convert_hex_to_int,
        log_parser=parse_raw_logs,
        log_parser_config=DEFAULT_LOG_PARSER_CFG,
        logs_bloom_converter=do_not_convert,
        status_converter=convert_hex_to_int,
        to_converter=do_not_convert,
        transaction_hash_converter=do_not_convert,
        transaction_index_converter=convert_hex_to_int,
        type_converter=convert_hex_to_int
    ):
        self.block_hash_converter = block_hash_converter
        self.block_number_converter = block_number_converter
        self.contract_address_converter = contract_address_converter
        self.cumulative_gas_used_converter = cumulative_gas_used_converter
        self.effective_gas_price_converter = effective_gas_price_converter
        self.from_converter = from_converter
        self.gas_used_converter = gas_used_converter
        self.log_parser = log_parser
        self.log_parser_config = log_parser_config
        self.logs_bloom_converter = logs_bloom_converter
        self.status_converter = status_converter
        self.to_converter = to_converter
        self.transaction_hash_converter = transaction_hash_converter
        self.transaction_index_converter = transaction_index_converter
        self.type_converter = type_converter

DEFAULT_RECEIPT_PARSER_CFG = ReceiptParserConfig()

def parse_raw_receipt(receipt_dict, parser_cfg=DEFAULT_RECEIPT_PARSER_CFG):
    return ParsedReceipt(
        block_hash=parser_cfg.block_hash_converter(receipt_dict.get('blockHash')),
        block_number=parser_cfg.block_number_converter(receipt_dict.get('blockNumber')),
        contract_address=parser_cfg.contract_address_converter(receipt_dict.get('contractAddress')),
        cumulative_gas_used=parser_cfg.cumulative_gas_used_converter(receipt_dict.get('cumulativeGasUsed')),
        effective_gas_price=parser_cfg.effective_gas_price_converter(receipt_dict.get('effectiveGasPrice')),
        from_=parser_cfg.from_converter(receipt_dict.get('from')),
        gas_used=parser_cfg.gas_used_converter(receipt_dict.get('gasUsed')),
        logs=parser_cfg.log_parser(receipt_dict.get('logs'), parser_cfg=parser_cfg.log_parser_config),
        logs_bloom=parser_cfg.logs_bloom_converter(receipt_dict.get('logsBloom')),
        status=parser_cfg.status_converter(receipt_dict.get('status')),
        to=parser_cfg.to_converter(receipt_dict.get('to')),
        transaction_hash=parser_cfg.transaction_hash_converter(receipt_dict.get('transactionHash')),
        transaction_index=parser_cfg.transaction_index_converter(receipt_dict.get('transactionIndex')),
        type_=parser_cfg.type_converter(receipt_dict.get('type'))
    ).to_dict()

def parse_raw_receipts(receipt_dict_list, parser_cfg=DEFAULT_RECEIPT_PARSER_CFG):
    if not receipt_dict_list:
        return []
    return [parse_raw_receipt(r, parser_cfg=parser_cfg) for r in receipt_dict_list]

