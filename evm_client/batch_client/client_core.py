from evm_client.sync_client.client_core import SyncClientCore
from evm_client.batch_client.utils import chunks, process_batch_http_response
from evm_client.errors import NodeError

class BatchClientCore(SyncClientCore):

    #now, let's make sure we pass through all prior responses when we hit a failure
    def make_batch_request(self, requests, inc=100):
        chunked_reqs = chunks(requests, inc)
        for c in chunked_reqs:
            yield process_batch_http_response(self.make_post_request(c))

    #if one really prefers the results as a dict, they can use this. Expect to get OOM errors
    @staticmethod
    def generator_to_dict(generator):
        result = {}
        for res in generator:
            for k, v in res.items():
                result[k] = v
        return result
