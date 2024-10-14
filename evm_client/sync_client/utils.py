from requests.models import Response
from evm_client.errors import HTTPStatusError, NodeError

def process_http_response(resp: Response):
        if not resp.status_code == 200:
            raise HTTPStatusError("Status code: {}".format(resp.status_code))
        r = resp.json()
        if r.get('error'):
            raise NodeError('Error: {}'.format(r['error']))
        return r['result']

