from typing import List
from evm_client.batch_client.client_core import BatchClientCore
from evm_client.core.eth_core import EthCore
from evm_client.types import EthFilter
from evm_client.batch_client.utils import chunks

class BatchEthClient(BatchClientCore, EthCore): 

    #TODO: definitely prefer instantiating the filter object within the method rather than outside. Update this in sync client
    def get_logs_big_range(self, address: str, topics: List[str], start_block: int, end_block: int, block_inc=10000, req_inc=100):
        chunked_range = chunks(list(range(start_block, end_block+1)), block_inc)
        filter_ = EthFilter(address=address, topics=topics) 
        req_id = 1
        bodies = []
        for chunk in chunked_range:
            filter_.from_block = chunk[0]
            filter_.to_block = chunk[-1]
            body = self.get_eth_get_logs_body(filter_, request_id=req_id)
            req_id += 1
            bodies.append(body)
        return self.make_batch_request(bodies, req_inc)


