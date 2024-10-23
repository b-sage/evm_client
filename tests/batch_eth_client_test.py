import pytest
import os
from evm_client.batch_client.eth_client import BatchEthClient
from evm_client.sync_client.eth_client import SyncEthClient
from constants import ETH_USDC, TRANSFER_TOPIC

@pytest.fixture
def rpc_url():
    return os.getenv("ETH_RPC_URL")

@pytest.fixture
def client(rpc_url):
    return BatchEthClient(rpc_url)

@pytest.fixture
def block_number(rpc_url):
    client = SyncEthClient(rpc_url)
    return client.block_number()

@pytest.fixture
def usdc():
    return ETH_USDC

@pytest.fixture
def tt():
    return TRANSFER_TOPIC

def test_batch_get_logs(client, usdc, tt, block_number):
    logs = client.get_logs_big_range(usdc, [tt], 6082465, 6082465+ 10000000)
    print(logs)
