from evm_client.core.utils import get_request_body

class AdminCore:

    @staticmethod
    def get_admin_add_peer_body(peer_url: str, request_id: int=1):
        return get_request_body("admin_adPeer", [peer_url], request_id=request_id)

    @staticmethod
    def get_admin_add_trusted_peer_body(peer_url: str, request_id: int=1):
        return get_request_body("admine_addTrustedPeer", [peer_url], request_id=request_id)

    @staticmethod
    def get_admin_datadir_body(request_id: int=1):
        return get_request_body("admin_datadir", [], request_id=request_id)

    @staticmethod
    def get_admin_export_chain_body(fname: str, from_block: int, to_block: int, request_id: int=1):
        params = [fname, hex(from_block), hex(to_block)]
        return get_request_body("admin_exportChain", params, request_id=request_id)

    @staticmethod
    def get_admin_import_chain_body(fname: str, request_id: int=1):
        return get_request_body("admin_importChain", [fname], request_id=request_id)

    @staticmethod
    def get_admin_node_info_body(request_id: int=1):
        return get_request_body("admin_nodeInfo", [], request_id=request_id)

    @staticmethod
    def get_admin_peer_events_body(request_id: int=1):
        return get_request_body("admin_peerEvents", [], request_id=request_id)

    @staticmethod
    def get_admin_peers_body(request_id: int=1):
        return get_request_body("admin_peers", [], request_id=request_id)

    @staticmethod
    def get_admin_remove_peer_body(peer_url: str, request_id: int=1):
        return get_request_body("admin_removePeer", [peer_url], request_id=request_id)

    @staticmethod
    def get_admin_remove_trusted_peer_body(peer_url: str, request_id: int=1):
        return get_request_body("admin_removeTrustedPeer", [peer_url], request_id=request_id)

    @staticmethod
    def get_admin_start_http_body(host: str="localhost", port: int=8545, cors: str="", apis: str="eth,net,web3", request_id: int=1):
        params = [host, str(hex(port)), cors, apis]
        return get_request_body("admin_startHTTP", params, request_id=request_id)

    @staticmethod
    def get_admin_start_ws_body(host: str="localhost", port: int=8545, cors: str="", apis: str="eth,net,web3", request_id: int=1):
        params = [host, str(hex(port)), cors, apis]
        return get_request_body("admin_startWS", params, request_id=request_id)

    @staticmethod
    def get_admin_stop_http_body(request_id: int=1):
        return get_request_body("admin_stopHTTP", [], request_id=request_id)

    @staticmethod
    def get_admin_stop_ws_body(request_id: int=1):
        return get_request_body("admin_stopWS", [], request_id=request_id)

