from typing import Optional
from evm_client.crypto_utils import hex_to_int
from evm_client.parsers.utils import assert_int, assert_str


#TODO: may be some fields we need to add as we test through networks
def parse_raw_transaction(transaction_dict):
    return ParsedTransaction(
        block_hash=transaction_dict.get('blockHash', None),
        block_number=hex_to_int(transaction_dict['blockNumber']) if transaction_dict.get('blockNumber') is not None else None,
        from_=transaction_dict.get('from', None),
        gas=hex_to_int(transaction_dict['gas']) if transaction_dict.get('gas') is not None else None,
        gas_price=hex_to_int(transaction_dict['gasPrice']) if transaction_dict.get('gasPrice') is not None else None,
        hash_=transaction_dict.get('hash', None),
        input_=transaction_dict.get('input', None),
        nonce=hex_to_int(transaction_dict['nonce']) if transaction_dict.get('nonce') is not None else None,
        r=transaction_dict.get('r', None),
        s=transaction_dict.get('s', None),
        to=transaction_dict.get('to', None),
        transaction_index=hex_to_int(transaction_dict['transactionIndex']) if transaction_dict.get('transactionIndex') is not None else None,
        type_=hex_to_int(transaction_dict['type']) if transaction_dict.get('type') is not None else None,
        v=hex_to_int(transaction_dict['v']) if transaction_dict.get('v') is not None else None,
        value=hex_to_int(transaction_dict['value']) if transaction_dict.get('value') is not None else None,
        access_list=transaction_dict.get('accessList', None),
        max_fee_per_gas=hex_to_int(transaction_dict['maxFeePerGas']) if transaction_dict.get('maxFeePerGas') is not None else None,
        max_priority_fee_per_gas=hex_to_int(transaction_dict['maxPriorityFeePerGas']) if transaction_dict.get('maxPriorityFeePerGas') is not None else None,
        chain_id=hex_to_int(transaction_dict['chainId']) if transaction_dict.get('chainId') is not None else None
    )


class ParsedTransaction:

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
        assert_str(block_hash)
        self.block_hash = block_hash
        assert_int(block_number)
        self.block_number = block_number
        assert_str(from_)
        self.from_ = from_
        assert_int(gas)
        self.gas = gas
        assert_int(gas_price)
        self.gas_price = gas_price
        assert_str(hash_)
        self.hash = hash_
        assert_str(input_)
        self.input = input_
        assert_int(nonce)
        self.nonce = nonce
        assert_str(r)
        self.r = r
        assert_str(s)
        self.s = s
        assert_str(to)
        self.to = to
        assert_int(transaction_index)
        self.transaction_index = transaction_index
        assert_int(type_)
        self.type = type_
        assert_int(v)
        self.v = v
        assert_int(value)
        self.value = value
        assert type(access_list) == list or access_list is None
        self.access_list = access_list
        assert_int(max_fee_per_gas)
        self.max_fee_per_gas = max_fee_per_gas
        assert_int(max_priority_fee_per_gas)
        self.max_priority_fee_per_gas = max_priority_fee_per_gas
        assert_int(chain_id)
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
