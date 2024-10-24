from evm_client.sync_client.client_core import SyncClientCore
from evm_client.batch_client.utils import chunks, process_batch_http_response

class BatchClientCore(SyncClientCore):

    def make_batch_request(self, requests, inc=100):
        chunked_reqs = chunks(requests, inc)
        return [process_batch_http_response(self.make_post_request(c)) for c in chunked_reqs]

