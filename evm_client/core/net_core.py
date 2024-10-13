from evm_client.core.utils import get_request_body

class NetCore:

    @staticmethod
    def get_net_version_body(request_id: int=1):
        return get_request_body("net_version", [], request_id=request_id)

    @staticmethod
    def get_net_listening_body(request_id: int=1):
        return get_request_body("net_listening", [], request_id=request_id)

    @staticmethod
    def get_net_peer_count_body(request_id: int=1):
        return get_request_body("net_peerCount", [], request_id=request_id)

