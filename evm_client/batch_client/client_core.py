from typing import List, Set, Union
from requests.models import Response
from evm_client.sync_client.client_core import SyncClientCore
from evm_client.batch_client.utils import chunks, process_batch_http_response
from evm_client.errors import NodeError, HTTPStatusError, RevertError

class BatchClientCore(SyncClientCore):
  
    #NOTE: bad_ids being passed here is not great, I don't find it to be very readable, but it's a hacky way we can skip over 
    #reverts and other bad data in our result generators
    def __process_batch_response(self, resp: Response, bad_ids: Union[List[int], None]=None):
        if bad_ids is None:
            bad_ids = []
        if resp.status_code != 200:
            raise HTTPStatusError(f"Status code: {resp.status_code}")
        results = {}
        response = resp.json()
        for r in response:
            _id = r['id']
            if bad_ids and _id in bad_ids:
                continue
            if r.get('error'):
                bad_ids.append(_id)
                raise RevertError(r['error'], _id)
            results[_id] = r['result']
        return results

    def _execute_batch_request_skip_node_exceptions(self, requests: List[dict], exceptions: Set[NodeError], chunk_increment: int=100):
        chunked_requests = chunks(requests, chunk_increment)
        for chunk in chunked_requests:
            res = self.make_post_request(chunk)
            n = NodeError('', 0)
            bad_ids = []
            while n:
                try:
                    yield self.__process_batch_response(res, bad_ids)
                except exceptions as n_:
                    n = n_
                else:
                    n = False

    def _execute_batch_request(self, requests: List[dict], chunk_increment: int=100):
        chunked_requests = chunks(requests, chunk_increment)
        for chunk in chunked_requests:
            yield self.__process_batch_response(self.make_post_request(chunk))

    def make_call_batch_request(self, requests, chunk_increment=100, drop_reverts=True):
        if drop_reverts:
            return self._execute_batch_request_skip_node_exceptions(requests, (NodeError), chunk_increment=chunk_increment)
        else:
            return self._execute_batch_request(requests, chunk_increment=chunk_increment)

    def make_batch_request(self, requests, chunk_increment=100):
        return self._execute_batch_request(requests, chunk_increment=chunk_increment)

    @staticmethod
    def yield_list_result_single_parser(result_generator, parser):
        for response in result_generator:
            for request_id, data in response.items():
                yield(parser.parse_multiple(data))

    @staticmethod
    def yield_dict_result(result_generator, parser):
        for response in result_generator:
            for request_id, data in response.items():
                yield(parser.parse(data))

    @staticmethod
    def yield_request_id_and_response_from_result(result_generator):
        for response in result_generator:
            for request_id, data in response.items():
                yield(request_id, data)

