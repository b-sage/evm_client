from evm_client.sync_client.client_core import SyncClientCore
from evm_client.batch_client.utils import flatten, chunks, process_batch_http_response

class BatchClientCore(SyncClientCore):

    def make_batch_request(self, requests, inc=100):
        chunked_reqs = chunks(requests, inc)
        result = []
        for c in chunked_reqs:
            res = process_batch_http_response(self.make_post_request(c))
            result.append(res)
        return flatten(result)

