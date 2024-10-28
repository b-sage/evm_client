from evm_client.sync_client.client_core import SyncClientCore
from evm_client.batch_client.utils import chunks, process_batch_http_response
from evm_client.errors import NodeError

class BatchClientCore(SyncClientCore):

    #now, let's make sure we pass through all prior responses when we hit a failure
    def make_batch_request(self, requests, inc=100):
        chunked_reqs = chunks(requests, inc)
        #would be nice to cache the post requests if possible so if we need to iterate more than once we don't need to hit the node again,
        #but think we'll run into OOM storing those results.
        for c in chunked_reqs:
            yield process_batch_http_response(self.make_post_request(c))

    #NOTE: only applies one parser to all results. Want to put together a method to apply parsers
    @staticmethod
    def yield_single_type_parsed_list_from_result(result_generator, parser_func):
        for response in result_generator:
            for request_id, data in response.items():
                for d in data:
                    yield(parser_func(d).to_dict())

    @staticmethod
    def yield_request_id_and_response_from_result(result_generator):
        for response in result_generator:
            for request_id, data in response.items():
                for d in data:
                    yield(request_id, d)
        

