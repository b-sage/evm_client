from evm_client.core.net_core import NetCore
from evm_client.sync_client.client_core import SyncClientCore
from evm_client.sync_client.utils import process_http_response
from evm_client.crypto_utils import hex_to_int

class SyncNetClient(SyncClientCore, NetCore):

    def version(self, request_id: int=1):
        body = self.get_net_version_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def listening(self, request_id: int=1):
        body = self.get_net_listening_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def peer_count(self, request_id: int=1):
        body = self.get_net_peer_count_body(request_id=request_id)
        res = self.make_post_request(body)
        return hex_to_int(process_http_response(res))

