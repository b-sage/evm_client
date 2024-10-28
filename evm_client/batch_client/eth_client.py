import time
from typing import List, Union
from evm_client.batch_client.client_core import BatchClientCore
from evm_client.core.eth_core import EthCore
from evm_client.types import EthFilter, Transaction
from evm_client.batch_client.utils import chunks
from evm_client.parsers import parse_raw_block, parse_raw_log

class BatchEthClient(BatchClientCore, EthCore): 

    #NOTE request id irrelevant, no back mapping required
    def get_logs(self, address: str, topics: List[str], start_block: int, end_block: int, block_inc=1000, req_inc=100):
        chunked_range = chunks(list(range(start_block, end_block+1)), block_inc)
        filter_ = EthFilter(address=address, topics=topics) 
        req_id = 1
        bodies = []
        for chunk in chunked_range:
            filter_.set_from_block(chunk[0])
            filter_.set_to_block(chunk[-1])
            body = self.get_eth_get_logs_body(filter_, request_id=req_id)
            req_id += 1
            bodies.append(body)
        result_generator = self.make_batch_request(bodies, req_inc)
        for response in result_generator:
            for request_id, logs in response.items():
                for log in logs:
                    yield(parse_raw_log(log).to_dict())

    #NOTE: request id irrelevant, no back mapping required
    def get_blocks_by_numbers(self, block_numbers: List[Union[int, str]], req_inc=100):
        req_id = 1
        bodies = []
        for block_number in block_numbers:
            bodies.append(self.get_eth_get_block_by_number_body(block_number, request_id=req_id))
            req_id += 1
        result_generator = self.make_batch_request(bodies, req_inc)
        for response in result_generator:
            for request_id, blocks in response.values():
                for block in blocks:
                    yield(parse_raw_block(block).to_dict())

    #need to return mapping of request id -> result. Not sure how we can achieve this with yield
    def calls(self, transactions: List[Transaction], req_inc=100):
        req_id = 1
        bodies = []
        for tx in transactions:
            bodies.append(self.get_eth_call_body(tx, request_id=req_id))
            req_id += 1
        result_generator = self.make_batch_request(bodies, req_inc)
        for r in result_generator:
            print(r)



