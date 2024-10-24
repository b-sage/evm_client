from evm_client.sync_client.client_core import SyncClientCore
from evm_client.batch_client.utils import chunks, process_batch_http_response

class BatchClientCore(SyncClientCore):

    def make_batch_request(self, requests, inc=100):
        chunked_reqs = chunks(requests, inc)
        res = {}
        for c in chunked_reqs:
            chunk_res = process_batch_http_response(self.make_post_request(c))
            res = {**res, **chunked_res}
        return res
