from evm_client.core import AdminCore
from evm_client.sync_client.client_core import SyncClientCore
from evm_client.sync_client.utils import process_http_response

class SyncAdminClient(SyncClientCore, AdminCore):

    def add_peer(self, peer_url: str, request_id: int=1):
        body = self.get_admin_add_peer_body(peer_url, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def add_trusted_peer(self, peer_url: str, request_id: int=1):
        body = self.get_admin_add_trusted_peer_body(peer_url, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def datadir(self, request_id: int=1):
        body = self.get_admin_datadir_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def export_chain(self, fname: str, from_block: int, to_block: int, request_id: int=1):
        body = self.get_admin_export_chain_body(fname, from_block, to_block, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def import_chain(self, fname: str, request_id: int=1):
        body = self.get_admin_import_chain_body(fname, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def node_info(self, request_id: int=1):
        body = self.get_admin_node_info_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def peer_events(self, request_id: int=1):
        body = self.get_admin_peer_events_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def peers(self, request_id: int=1):
        body = self.get_admin_peers_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def remove_peer(self, peer_url: str, request_id: int=1):
        body = self.get_admin_remove_peer_body(peer_url, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def remove_trusted_peer(self, peer_url: str, request_id: int=1):
        body = self.get_admin_remove_trusted_peer_body(peer_url, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def start_http(self, host: str="localhost", port: int=8545, cors: str="", apis: str="eth,net,web3", request_id: int=1):
        body = self.get_admin_start_http_body(host, port, cors, apis, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def start_ws(self, host: str="localhost", port: int=8545, cors: str="", apis: str="eth,net,web3", request_id: int=1):
        body = self.get_admin_start_ws_body(host, port, cors, apis, request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def stop_http(self, request_id: int=1):
        body = self.get_admin_stop_http_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)

    def stop_ws(self, request_id: int=1):
        body = self.get_admin_stop_ws_body(request_id=request_id)
        res = self.make_post_request(body)
        return process_http_response(res)



