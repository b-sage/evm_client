from evm_client.core import EthCore
from evm_client.sync_client.client_core import SyncClientCore

class SyncEthClient(SyncClientCore, EthCore):

    def block_number(self, request_id: int=1):
        body = self.get_eth_block_number_body(request_id=request_id)
        return self.make_post_request(body)


