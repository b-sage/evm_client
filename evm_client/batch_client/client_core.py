from evm_client.sync_client.client_core import SyncClientCore
from evm_client.batch_client.utils import chunks, process_batch_http_response
from evm_client.errors import NodeError

class BatchClientCore(SyncClientCore):
    
    #TODO: ensure NodeError is a revert
    def _execute_drop_reverts(self, chunked_requests):
        for i, chunk in enumerate(chunked_requests):
            while True:
                res = self.make_post_request(chunk)
                try:
                    yield process_batch_http_response(res)
                except NodeError as n:
                    print(n.request_id)
                    chunked_requests[i] = [c for c in chunk if c['request_id'] != n.request_id]
                    return self._execute_drop_reverts(chunked_requests)

    def _execute(self, chunked_requests):
        for chunk in chunked_requests:
            yield process_http_response(self.make_post_request(chunk))

    def make_batch_request(self, requests, inc=100, drop_reverts=True):
        chunked_reqs = chunks(requests, inc)
        if drop_reverts:
            return self._execute_drop_reverts(chunked_reqs)
        else:
            return self._execute(chunked_reqs)

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


