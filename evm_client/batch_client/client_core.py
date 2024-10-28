from evm_client.sync_client.client_core import SyncClientCore
from evm_client.batch_client.utils import chunks, process_batch_http_response
from evm_client.errors import NodeError

class BatchClientCore(SyncClientCore):

    def _execute_chunked_requests(self, chunked_requests):
        for c in chunked_reqs:
            res = self.make_post_request(c)
            yield process_batch_http_response(res)

    def make_batch_request(self, requests, inc=100, drop_reverts=True):
        chunked_reqs = chunks(requests, inc)
        while True:
            if drop_reverts:
                try:
                    return self._execute_chunked_requests(chunked_reqs)
                except NodeError as n:
                    bad_id = n.request_id
                    requests = [r for r in requests in r['request_id'] > bad_id]
                    chunked_reqs = chunks(requests, inc)
            else:
                return self._execute_chunked_requests(chunked_reqs)

    #NOTE: only applies one parser to all results. Want to put together a method to apply parsers
    #TODO: make parser funcs return a Parser object which has method .default()
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
                yield(request_id, data)


