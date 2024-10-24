
class HTTPStatusError(Exception):
    pass

#TODO: should get a bit more specific with these. Can be due to bad input, node issues, etc
class NodeError(Exception):
    
    def __init__(self, error_msg, request_id):
        super().__init__(error_msg)
        self.error_msg = error_msg
        self.request_id=request_id

