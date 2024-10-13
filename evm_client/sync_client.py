import requests
from evm_client.core import EthNamespaceCore

class SyncClient:

    def __init__(self, node_url: str):
        self.url = node_url

    def make_request(self, body):
        return requests.post(self.url, data=body)



class SyncEthNamespaceClient(SyncClient):

    def block_number(self):
        body = EthNamespaceCore.get_eth_block_number_body()
        return self.make_request(body)



