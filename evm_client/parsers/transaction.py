from evm_client.parsers.base import ParsedObject, Parser
from evm_client.converters import convert_hex_to_int, do_not_convert

class ParsedTransaction(ParsedObject):

    def __init__(
        self,
        block_hash=None,
        block_number=None,
        from_=None,
        gas=None,
        gas_price=None,
        hash_=None,
        input_=None,
        nonce=None,
        r=None,
        s=None,
        to=None,
        transaction_index=None,
        type_=None,
        v=None,
        value=None,
        access_list=None,
        max_fee_per_gas=None,
        max_priority_fee_per_gas=None,
        chain_id=None
    ):
        self.block_hash = block_hash
        self.block_number = block_number
        self.from_ = from_
        self.gas = gas
        self.gas_price = gas_price
        self.hash = hash_
        self.input = input_
        self.nonce = nonce
        self.r = r
        self.s = s
        self.to = to
        self.transaction_index = transaction_index
        self.type = type_
        self.v = v
        self.value = value
        self.access_list = access_list
        self.max_fee_per_gas = max_fee_per_gas
        self.max_priority_fee_per_gas = max_priority_fee_per_gas
        self.chain_id = chain_id

class TransactionParserConfig:

    def __init__(
            self,
            block_hash_converter=do_not_convert,
            block_number_converter=convert_hex_to_int,
            from_converter=do_not_convert,
            gas_converter=convert_hex_to_int,
            gas_price_converter=convert_hex_to_int,
            hash_converter=do_not_convert,
            input_converter=do_not_convert,
            nonce_converter=convert_hex_to_int,
            r_converter=do_not_convert,
            s_converter=do_not_convert,
            to_converter=do_not_convert,
            transaction_index_converter=convert_hex_to_int,
            type_converter=convert_hex_to_int,
            v_converter=convert_hex_to_int,
            value_converter=convert_hex_to_int,
            access_list_converter=do_not_convert,
            max_fee_per_gas_converter=convert_hex_to_int,
            max_priority_fee_per_gas_converter=convert_hex_to_int,
            chain_id_converter=convert_hex_to_int
    ):
        self.block_hash_converter = block_hash_converter
        self.block_number_converter = block_number_converter
        self.from_converter = from_converter
        self.gas_converter = gas_converter
        self.gas_price_converter = gas_price_converter
        self.hash_converter = hash_converter
        self.input_converter = input_converter
        self.nonce_converter = nonce_converter
        self.r_converter = r_converter
        self.s_converter = s_converter
        self.to_converter = to_converter
        self.transaction_index_converter = transaction_index_converter
        self.type_converter = type_converter
        self.v_converter = v_converter
        self.value_converter = value_converter
        self.access_list_converter = access_list_converter
        self.max_fee_per_gas_converter = max_fee_per_gas_converter
        self.max_priority_fee_per_gas_converter = max_priority_fee_per_gas_converter
        self.chain_id_converter = chain_id_converter

class TransactionParser(Parser):

    def __init__(self, cfg: TransactionParserConfig=TransactionParserConfig()):
        self.cfg = cfg

    def parse(self, transaction_dict):
        return ParsedTransaction(
            block_hash=self.cfg.block_hash_converter(transaction_dict.get('blockHash')),
            block_number=self.cfg.block_number_converter(transaction_dict.get('blockNumber')),
            from_=self.cfg.from_converter(transaction_dict.get('from')),
            gas=self.cfg.gas_converter(transaction_dict.get('gas')),
            gas_price=self.cfg.gas_price_converter(transaction_dict.get('gasPrice')),
            hash_=self.cfg.hash_converter(transaction_dict.get('hash')),
            input_=self.cfg.input_converter(transaction_dict.get('input')),
            nonce=self.cfg.nonce_converter(transaction_dict.get('nonce')),
            r=self.cfg.r_converter(transaction_dict.get('r')),
            s=self.cfg.s_converter(transaction_dict.get('s')),
            to=self.cfg.to_converter(transaction_dict.get('to')),
            transaction_index=self.cfg.transaction_index_converter(transaction_dict.get('transactionIndex')),
            type_=self.cfg.type_converter(transaction_dict.get('type')),
            v=self.cfg.v_converter(transaction_dict.get('v')),
            value=self.cfg.value_converter(transaction_dict.get('value')),
            access_list=self.cfg.access_list_converter(transaction_dict.get('accessList')),
            max_fee_per_gas=self.cfg.max_fee_per_gas_converter(transaction_dict.get('maxFeePerGas')),
            max_priority_fee_per_gas=self.cfg.max_priority_fee_per_gas_converter(transaction_dict.get('maxPriorityFeePerGas')),
            chain_id=self.cfg.chain_id_converter(transaction_dict.get('chainId'))
        ).to_dict() 

