from typing import Optional
from evm_client.parsers.utils import assert_int, assert_str
from evm_client.parsers.base import BaseParser
from evm_client.parsers import parse_raw_hex_to_int

def parse_raw_receipt(receipt_dict):
    return ReceiptParser(
        block_hash=receipt_dict.get('blockHash', None),
        block_number=parse_raw_hex_to_int(receipt_dict.get('blockNumber')).default_format(),
        contract_address=receipt_dict.get('contractAddress', None),
        cumulative_gas_used=parse_raw_hex_to_int(receipt_dict.get('cumulativeGasUsed')).default_format(),
        effective_gas_price=parse_raw_hex_to_int(receipt_dict.get('effectiveGasPrice')).default_format(),
        from_=receipt_dict.get('from', None),
        gas_used=parse_raw_hex_to_int(receipt_dict.get('gasUsed')).default_format(),
        logs=[log.default_format() for log in parse_raw_logs(receipt_dict['logs'])] if receipt_dict.get('logs') else None,
        logs_bloom=receipt_dict.get('logsBloom', None),
        status=parse_raw_hex_to_int(receipt_dict.get('status')).default_format(),
        to=receipt_dict.get('to', None),
        transaction_hash=receipt_dict.get('transactionHash', None),
        transaction_index=parse_raw_hex_to_int(receipt_dict.get('transactionIndex')).default_format(),
        type_=parse_raw_hex_to_int(receipt_dict.get('type')).default_format()
    )

def parse_raw_log(log_dict):
    return LogParser(
        address=log_dict.get('address', None),
        topics=log_dict.get('topics', None),
        data=log_dict.get('data', None),
        block_number=parse_raw_hex_to_int(log_dict.get('blockNumber')).default_format(),
        transaction_hash=log_dict.get('transactionHash', None),
        transaction_index=parse_raw_hex_to_int(log_dict.get('transactionIndex')).default_format(),
        block_hash=log_dict.get('blockHash', None),
        log_index=parse_raw_hex_to_int(log_dict.get('logIndex')).default_format(),
        removed=log_dict.get('removed', None)
    )

def parse_raw_logs(log_dict_list):
    return [parse_raw_log(l) for l in log_dict_list]

def parse_raw_receipts(receipt_dict_list):
    return [parse_raw_receipt(r) for r in receipt_dict_list]

class ReceiptParser(BaseParser):

    def __init__(
        self,
        block_hash: Optional[str]=None,
        block_number: Optional[int]=None,
        contract_address: Optional[str]=None,
        cumulative_gas_used: Optional[int]=None,
        effective_gas_price: Optional[int]=None,
        from_: Optional[str]=None,
        gas_used: Optional[int]=None,
        logs: Optional[list]=None,
        logs_bloom: Optional[str]=None,
        status: Optional[int]=None,
        to: Optional[str]=None,
        transaction_hash: Optional[str]=None,
        transaction_index: Optional[int]=None,
        type_: Optional[int]=None
    ):
        assert_str(block_hash)
        self.block_hash = block_hash
        assert_int(block_number)
        self.block_number = block_number
        assert_str(contract_address)
        self.contract_address = contract_address
        assert_int(cumulative_gas_used)
        self.cumulative_gas_used = cumulative_gas_used
        assert_int(effective_gas_price)
        self.effective_gas_price = effective_gas_price
        assert_str(from_)
        self.from_ = from_
        assert_int(gas_used)
        self.gas_used = gas_used
        assert type(logs) == list or logs is None
        self.logs = logs
        assert_str(logs_bloom)
        self.logs_bloom = logs_bloom
        assert_int(status)
        self.status = status
        assert_str(to)
        self.to = to
        assert_str(transaction_hash)
        self.transaction_hash = transaction_hash
        assert_int(transaction_index)
        self.transaction_index = transaction_index
        assert_int(type_)
        self.type = type_

    def as_dict(self):
        return {
            "blockHash": self.block_hash,
            "blockNumber": self.block_number,
            "contractAddress": self.contract_address,
            "cumulativeGasUsed": self.cumulative_gas_used,
            "effectiveGasPrice": self.effective_gas_price,
            "from": self.from_,
            "gasUsed": self.gas_used,
            "logs": self.logs,
            "logsBloom": self.logs_bloom,
            "status": self.status,
            "to": self.to,
            "transactionHash": self.transaction_hash,
            "transactionIndex": self.transaction_index,
            "type": self.type
        }

    def to_dict(self):
        d = self.as_dict()
        return {k:v for k,v in d.items() if v is not None}

    def default_format(self):
        return self.to_dict()

class LogParser(BaseParser):

    def __init__(
        self,
        address: Optional[str]=None,
        topics: Optional[list]=None,
        data: Optional[str]=None,
        block_number: Optional[int]=None,
        transaction_hash: Optional[str]=None,
        transaction_index: Optional[int]=None,
        block_hash: Optional[str]=None,
        log_index: Optional[int]=None,
        removed: Optional[bool]=None
    ):
        assert_str(address)
        self.address = address
        assert type(topics) == list or topics is None
        self.topics = topics
        assert_str(data)
        self.data = data
        assert_int(block_number)
        self.block_number = block_number
        assert_str(transaction_hash)
        self.transaction_hash = transaction_hash
        assert_int(transaction_index)
        self.transaction_index = transaction_index
        assert_str(block_hash)
        self.block_hash = block_hash
        assert_int(log_index)
        self.log_index = log_index
        assert type(removed) == bool or removed is None
        self.removed = removed

    def as_dict(self):
        return {
            "address": self.address,
            "topics": self.topics,
            "data": self.data,
            "blockNumber": self.block_number,
            "transactionHash": self.transaction_hash,
            "transactionIndex": self.transaction_index,
            "blockHash": self.block_hash,
            "logIndex": self.log_index,
            "removed": self.removed
        }

    def to_dict(self):
        d = self.as_dict()
        return {k:v for k,v in d.items() if v is not None}

    def default_format(self):
        return self.to_dict()
