from evm_client.parsers.base import ParsedObject, Parser
from evm_client.converters import convert_hex_to_int, do_not_convert
from evm_client.parsers import LogParser

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
        log_parser=LogParser(),
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
        self.logs_bloom_converter = logs_bloom_converter
        self.status_converter = status_converter
        self.to_converter = to_converter
        self.transaction_hash_converter = transaction_hash_converter
        self.transaction_index_converter = transaction_index_converter
        self.type_converter = type_converter

class ReceiptParser(Parser):

    def __init__(self, cfg: ReceiptParserConfig=ReceiptParserConfig()):
        self.cfg = cfg

    def parse(self, receipt_dict):
        return ParsedReceipt(
            block_hash=self.cfg.block_hash_converter(receipt_dict.get('blockHash')),
            block_number=self.cfg.block_number_converter(receipt_dict.get('blockNumber')),
            contract_address=self.cfg.contract_address_converter(receipt_dict.get('contractAddress')),
            cumulative_gas_used=self.cfg.cumulative_gas_used_converter(receipt_dict.get('cumulativeGasUsed')),
            effective_gas_price=self.cfg.effective_gas_price_converter(receipt_dict.get('effectiveGasPrice')),
            from_=self.cfg.from_converter(receipt_dict.get('from')),
            gas_used=self.cfg.gas_used_converter(receipt_dict.get('gasUsed')),
            logs_bloom=self.cfg.logs_bloom_converter(receipt_dict.get('logsBloom')),
            logs=self.cfg.log_parser.parse(receipt_dict.get('logs')),
            status=self.cfg.status_converter(receipt_dict.get('status')),
            to=self.cfg.to_converter(receipt_dict.get('to')),
            transaction_hash=self.cfg.transaction_hash_converter(receipt_dict.get('transactionHash')),
            transaction_index=self.cfg.transaction_index_converter(receipt_dict.get('transactionIndex')),
            type_=self.cfg.type_converter(receipt_dict.get('type'))
        ).to_dict()

