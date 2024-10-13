from evm_client.core import EthCore
from evm_client.sync_client.client_core import SyncClientCore

class SyncEthClient(SyncClientCore, EthCore):

    def protocol_version(self, request_id: int=1):
        body = self.get_eth_protocol_version_body(request_id=request_id)
        return self.make_post_request(body)

    def syncing(self, request_id: int=1):
        body = self.get_eth_syncing_body(request_id=request_id)
        return self.make_post_request(body)

    def block_number(self, request_id: int=1):
        body = self.get_eth_block_number_body(request_id=request_id)
        return self.make_post_request(body)


