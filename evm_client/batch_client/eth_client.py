import time
from typing import List, Union, Tuple
from evm_client.batch_client.client_core import BatchClientCore
from evm_client.core.eth_core import EthCore
from evm_client.converters import convert_hex_to_int
from evm_client.types import EthFilter, Transaction
from evm_client.batch_client.utils import chunks
from evm_client.parsers import BlockParser, LogParser, TransactionParser

class BatchEthClient(BatchClientCore, EthCore): 

    def __init__(
            self, 
            node_url,
            block_parser=BlockParser(),
            log_parser=LogParser(),
            transaction_parser=TransactionParser()
    ):
        super().__init__(node_url)
        self.default_block_parser = block_parser
        self.default_log_parser = log_parser
        self.default_transaction_parser = transaction_parser

    def get_logs_batch(self, filters: List[EthFilter], req_inc: int=100, parser=None):
        parser = parser or self.default_log_parser
        req_id = 1
        bodies = []
        for filter_ in filters:
            body = self.get_eth_get_logs_body(filter_, request_id=req_id)
            req_id += 1
            bodies.append(body)
        result_generator = self.make_batch_request(bodies, req_inc)
        return self.yield_list_result_single_parser(result_generator, parser)

    def get_block_by_number_batch(self, block_numbers: List[Union[int, str]], req_inc: int=100, parser=None):
        parser = parser or self.default_block_parser
        req_id = 1
        bodies = []
        for block_number in block_numbers:
            bodies.append(self.get_eth_get_block_by_number_body(block_number, request_id=req_id))
            req_id += 1
        result_generator = self.make_batch_request(bodies, req_inc)
        return self.yield_dict_result(result_generator, parser)

    def get_block_by_hash_batch(self, block_hashes: List[str], req_inc: int=100, parser=None):
        parser = parser or self.default_block_parser
        req_id = 1
        bodies = []
        for block_hash in block_hashes:
            bodies.append(self.get_eth_get_block_by_hash_body(block_hash, request_id=req_id))
            req_id += 1
        result_generator = self.make_batch_request(bodies, req_inc)
        return self.yield_dict_result(result_generator, parser)

    def call_batch(self, transactions: List[Transaction], req_inc: int=100, drop_reverts: bool=True):
        req_id = 1
        bodies = []
        for tx in transactions:
            bodies.append(self.get_eth_call_body(tx, request_id=req_id))
            req_id += 1
        result_generator = self.make_call_batch_request(bodies, req_inc, drop_reverts=drop_reverts)
        return self.yield_request_id_and_response_from_result(result_generator)

    def get_transaction_batch(self, transaction_hashes: List[str], req_inc: int=100, parser=None):
        parser = parser or self.default_transaction_parser
        req_id = 1
        bodies = []
        for hsh in transaction_hashes:
            bodies.append(self.get_eth_get_transaction_by_hash_body(hsh, request_id=req_id))
            req_id += 1
        result_generator = self.make_batch_request(bodies, req_inc)
        return self.yield_dict_result(result_generator, parser)

    # addrs_and_blocks: [('0xabc123...', 'latest'), ('0xdef456...', 1772397)]
    def get_balance_batch(self, addrs_and_blocks: List[Tuple[str, Union[int, str]]], req_inc: int=100):
        req_id = 1
        bodies = []
        req_map = {}
        for address, block_num in addrs_and_blocks:
            bodies.append(self.get_eth_get_balance_body(address, block_number=block_num, request_id=req_id))
            req_map[req_id] = (address, block_num)
            req_id += 1
        result_generator = self.make_batch_request(bodies, req_inc)
        for r in result_generator:
            yield {req_map[k]: convert_hex_to_int(v) for k, v in r.items()}

    def get_transaction_count_batch(self, addrs_and_blocks: List[Tuple[str, Union[int, str]]], req_inc: int=100):
        req_id = 1
        bodies = []
        req_map = {}
        for address, block_num in addrs_and_blocks:
            bodies.append(self.get_eth_get_transaction_count_body(address, block_number=block_num, request_id=req_id))
            req_map[req_id] = (address, block_num)
            req_id += 1
        result_generator = self.make_batch_request(bodies, req_inc)
        for r in result_generator:
            yield {req_map[k]: convert_hex_to_int(v) for k, v in r.items()}
