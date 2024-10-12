from typing import List, Union

def generate_json_rpc(method: str, params: List[Union[int, str]], request_id: int=1):
    return {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': request_id,
    }


class Web3NamespaceCore:
    
    @staticmethod
    def get_web3_client_version_body(request_id: int=1):
        method = "web3_clientVersion"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_web3_sha3_body(data: str, request_id: int=1):
        method = "web3_sha3"
        params = [data]
        return generate_json_rpc(method, params, request_id=request_id)


class NetNamespaceCore:

    @staticmethod
    def get_net_version_body(request_id: int=1):
        method = "net_version"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_net_listening_body(request_id: int=1):
        method = "net_listening"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_net_peer_count_body(request_id: int=1):
        method = "net_peerCount"
        return generate_json_rpc(method, [], request_id=request_id)

class EthNamespaceCore:

    @staticmethod
    def get_eth_protocol_version_body(request_id: int=1):
        method = "eth_protocolVersion"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_syncing_body(request_id: int=1):
        method = "eth_syncing"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_coinbase_body(request_id: int=1):
        method = "eth_coinbase"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_chain_id_body(request_id: int=1):
        method = "eth_chainId"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_mining_body(request_id: int=1):
        method = "eth_mining"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_hashrate_body(request_id: int=1):
        method = "eth_hashrate"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_gas_price_body(request_id: int=1):
        method = "eth_gasPrice"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_accounts_body(request_id: int=1):
        method = "eth_accounts"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_block_number_body(request_id: int=1):
        method = "eth_blockNumber"
        return generate_json_rpc(method, [], request_id=request_id)

    @staticmethod
    def get_eth_get_balance_body(address: str, block_number: Union[int, str]="latest", request_id: int=1):
        method = "eth_getBalance"
        params = [address, block_number]
        return generate_json_rpc(method, params, request_id=request_id)

    @staticmethod
    def get_eth_get_storage_at_body(address: str, storage_position: int, block_number: Union[int, str]="latest", request_id: int=1):
        method = "eth_getStorageAt"
        params = [address, storage_position, block_number]
        return generate_json_rpc(method, params, request_id=request_id)


