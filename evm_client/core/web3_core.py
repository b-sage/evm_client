from evm_client.core.utils import get_request_body

class Web3Core:
    
    @staticmethod
    def get_web3_client_version_body(request_id: int=1):
        return get_request_body("web3_clientVersion", [], request_id=request_id)

    @staticmethod
    def get_web3_sha3_body(data: str, request_id: int=1):
        return get_request_body("web3_sha3", [data], request_id=request_id)

