
class HTTPStatusError(BaseException):
    pass

#TODO: should get a bit more specific with these. Can be due to bad input, node issues, etc
class NodeError(BaseException):
    pass

