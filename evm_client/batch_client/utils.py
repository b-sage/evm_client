from typing import Union, List
from requests.models import Response
from evm_client.errors import HTTPStatusError, NodeError

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def flatten(xss):
    return [x for xs in xss for x in xs]

#TODO: determine how to appoly yeild here properly, otherwise we're going to run into tons of OOM errors
def process_batch_http_response(resp: Response, bad_ids: Union[List[int], None]=None):
        if not resp.status_code == 200:
            raise HTTPStatusError("Status code: {}".format(resp.status_code))
        results = resp.json()
        results_ = {}
        for r in results:
            _id = r['id']
            if bad_ids and _id in bad_ids:
                continue
            if r.get('error'):
                bad_ids.append(_id)
                raise NodeError(r['error'], _id, results=results_)
            results_[_id] = r['result']
        return results_
