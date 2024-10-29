from typing import Optional
from evm_client.parsers.utils import assert_int, assert_str
from evm_client.parsers.base import BaseParser
from evm_client.parsers import parse_raw_hex_to_int, parse_null

#technically need to pass through all log parsers to parse_raw_log call
def parse_raw_receipt(
        receipt_dict,
        block_hash_parser=parse_null,
        block_number_parser=parse_raw_hex_to_int,
        contract_address_parser=parse_null,
        cumulative_gas_used_parser=parse_raw_hex_to_int,
        effective_gas_price_parser=parse_raw_hex_to_int,
        from_parser=parse_null,
        gas_used_parser=parse_raw_hex_to_int,
        logs_parser=parse_raw_logs,
        #NOTE: must handle for list of logs, not individual log
        logs_bloom_parser=parse_null,
        status_parser=parse_raw_hex_to_int,
        to_parser=parse_null,
        transaction_hash_parser=parse_null,
        transaction_index_parser=parse_raw_hex_to_int,
        type_parser=parse_raw_hex_to_int,
        log_address_parser=parse_null,
        log_topics_parser=parse_null,
        log_data_parser=parse_null,
        log_block_number_parser=parse_raw_hex_to_int,
        log_transaction_hash_parser=parse_null,
        log_transaction_index_parser=parse_raw_hex_to_int,
        log_block_hash_parser=parse_null,
        log_log_index_parser=parse_raw_hex_to_int,
        log_removed_parser=parse_null
):
    return ParsedReceipt(
        block_hash=block_hash_parser(receipt_dict.get('blockHash')),
        block_number=block_number_parser(receipt_dict.get('blockNumber')),
        contract_address=contract_address_parser(receipt_dict.get('contractAddress'),
        cumulative_gas_used=cumulative_gas_used_parser(receipt_dict.get('cumulativeGasUsed')),
        effective_gas_price=effective_gas_price_parser(receipt_dict.get('effectiveGasPrice')),
        from_=from_parser(receipt_dict.get('from')),
        gas_used=gas_used_parser(receipt_dict.get('gasUsed')),
        logs=logs_parser(
            receipt_dict.get('logs'),
            address_parser=log_address_parser,
            topics_parser=log_topics_parser,
            data_parser=log_data_parser,
            block_number_parser=log_block_number_parser,
            transaction_hash_parser=log_transaction_hash_parser,
            transaction_index_parser=log_transaction_index_parser,
            block_hash_parser=log_block_hash_parser,
            log_index_parser=log_log_index_parser,
            removed_parser=log_remove_parser
        )
        logs_bloom=logs_bloom_parser(receipt_dict.get('logsBloom')),
        status=status_parser(receipt_dict.get('status')),
        to=to_parser(receipt_dict.get('to')),
        transaction_hash=transaction_hash_parser(receipt_dict.get('transactionHash')),
        transaction_index=transaction_index_parser(receipt_dict.get('transactionIndex')),
        type_=type_parser(receipt_dict.get('type'))
    ).default_format()


def parse_raw_log(
        log_dict,
        address_parser=parse_null,
        topics_parser=parse_null,
        data_parser=parse_null,
        block_number_parser=parse_raw_hex_to_int,
        transaction_hash_parser=parse_null,
        transaction_index_parser=parse_raw_hex_to_int,
        block_hash_parser=parse_null,
        log_index_parser=parse_raw_hex_to_int,
        removed_parser=parse_null
):
    return ParsedLog(
        address=address_parser(log_dict.get('address')),
        topics=topics_parser(log_dict.get('topics')),
        data=data_parser(log_dict.get('data')),
        block_number=block_number_parser(log_dict.get('blockNumber')),
        transaction_hash=transaction_hash_parser(log_dict.get('transactionHash')),
        transaction_index=transaction_index_parser(log_dict.get('transactionIndex')),
        block_hash=block_hash_parser(log_dict.get('blockHash')),
        log_index=log_index_parser(log_dict.get('logIndex')),
        removed=removed_parser(log_dict.get('removed'))
    ).default_format()

def parse_raw_logs(log_dict_list):
    if not log_dict_list:
        return []
    return [parse_raw_log(l) for l in log_dict_list]

def parse_raw_receipts(receipt_dict_list):
    if not receipt_dict_list:
        return []
    return [parse_raw_receipt(r) for r in receipt_dict_list]

class ParsedReceipt(BaseParser):

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

class ParsedLog(BaseParser):

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
        self.address = address
        self.topics = topics
        self.data = data
        self.block_number = block_number
        self.transaction_hash = transaction_hash
        self.transaction_index = transaction_index
        self.block_hash = block_hash
        self.log_index = log_index
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
