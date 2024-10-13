from typing import List, Union

def get_request_body(method: str, params: List[Union[int, str]], request_id: int=1):
    return {
        'jsonrpc': '2.0',
        'method': method,from typing import List, Union
        'params': params,
        'id': request_id,
    }
