from evm_client.parsers.base import BaseParser
from evm_client.parsers import parse_raw_hex_to_int, parse_null

#TODO: may be some fields we need to add as we test through networks
def parse_raw_transaction(
        transaction_dict,
        block_hash_parser=parse_null,
        block_number_parser=parse_raw_hex_to_int,
        from_parser=parse_null,
        gas_parser=parse_raw_hex_to_int,
        gas_price_parser=parse_raw_hex_to_int,
        hash_parser=parse_null,
        input_parser=parse_null,
        nonce_parser=parse_raw_hex_to_int,
        r_parser=parse_null,
        s_parser=parse_null,
        to_parser=parse_null,
        transaction_index_parser=parse_raw_hex_to_int,
        type_parser=parse_raw_hex_to_int,
        v_parser=parse_raw_hex_to_int,
        value_parser=parse_raw_hex_to_int,
        access_list_parser=parse_null,
        max_fee_per_gas_parser=parse_raw_hex_to_int,
        max_priority_fee_per_gas_parser=parse_raw_hex_to_int,
        chain_id_parser=parse_raw_hex_to_int
):
    return ParsedTransaction(
        block_hash=block_hash_parser(transaction_dict.get('blockHash')),
        block_number=block_number_parser(transaction_dict.get('blockNumber')),
        from_=from_parser(transaction_dict.get('from')),
        gas=gas_parser(transaction_dict.get('gas')),
        gas_price=gas_price_parser(transaction_dict.get('gasPrice')),
        hash_=hash_parser(transaction_dict.get('hash')),
        input_=input_parser(transaction_dict.get('input')),
        nonce=nonce_parser(transaction_dict.get('nonce')),
        r=r_parser(transaction_dict.get('r')),
        s=s_parser(transaction_dict.get('s')),
        to=to_parser(transaction_dict.get('to')),
        transaction_index=transaction_index_parser(transaction_dict.get('transactionIndex')),
        type_=type_parser(transaction_dict.get('type')),
        v=v_parser(transaction_dict.get('v')),
        value=value_parser(transaction_dict.get('value')),
        access_list=access_list_parser(transaction_dict.get('accessList')),
        max_fee_per_gas=max_fee_per_gas_parser(transaction_dict.get('maxFeePerGas')),
        max_priority_fee_per_gas=max_priority_fee_per_gas_parser(transaction_dict.get('maxPriorityFeePerGas')),
        chain_id=chain_id_parser(transaction_dict.get('chainId'))
    ).default_format()

def parse_raw_transactions(transaction_dict_list):
    if not transaction_dict_list:
        return []
    return [parse_raw_transaction(t) for t in transaction_dict_list]


class ParsedTransaction(BaseParser):

    def __init__(
        self,
        block_hash: Optional[str]=None,
        block_number: Optional[int]=None,
        from_: Optional[str]=None,
        gas: Optional[int]=None,
        gas_price: Optional[int]=None,
        hash_: Optional[str]=None,
        input_: Optional[str]=None,
        nonce: Optional[int]=None,
        r: Optional[str]=None,
        s: Optional[str]=None,
        to: Optional[str]=None,
        transaction_index: Optional[int]=None,
        type_: Optional[int]=None,
        v: Optional[int]=None,
        value: Optional[int]=None,
        access_list: Optional[list]=None,
        max_fee_per_gas: Optional[int]=None,
        max_priority_fee_per_gas: Optional[int]=None,
        chain_id: Optional[int]=None
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


    def as_dict(self):
        return {
            "blockHash": self.block_hash,
            "blockNumber": self.block_number,
            "from": self.from_,
            "gas": self.gas,
            "gasPrice": self.gas_price,
            "hash": self.hash,
            "input": self.input,
            "nonce": self.nonce,
            "r": self.r,
            "s": self.s,
            "to": self.to,
            "transactionIndex": self.transaction_index,
            "type": self.type,
            "v": self.v,
            "value": self.value,
            "accessList": self.access_list,
            "maxFeePerGas": self.max_fee_per_gas,
            "maxPriorityFeePerGas": self.max_priority_fee_per_gas,
            "chainId": self.chain_id
        }

    def to_dict(self):
        d = self.as_dict()
        return {k:v for k,v in d.items() if v is not None}

    def default_format(self):
        return self.to_dict()
