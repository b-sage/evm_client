import requests

class SyncClientCore:

    def __init__(self, node_url: str):
        self.url = node_url

    def make_request(self, body):
        return requests.post(self.url, data=body)
    
    #batch request func?

