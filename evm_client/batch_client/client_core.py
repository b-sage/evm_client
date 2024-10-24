from evm_client.sync_client.client_core import SyncClientCore
from evm_client.batch_client.utils import chunks, process_batch_http_response
from evm_client.errors import NodeError

class BatchClientCore(SyncClientCore):

    def make_batch_request(self, requests, inc=100):
        chunked_reqs = chunks(requests, inc)
        res = {}
        for c in chunked_reqs:
            #TODO: fix this hacky try except. Just doing this so we can pass already good results through when a batch request fails
            try:
                chunk_res = process_batch_http_response(self.make_post_request(c))
                res = {**res, **chunk_res}
            except NodeError as n:
                n.results = {**res, **n.results}
                raise n
        return res
