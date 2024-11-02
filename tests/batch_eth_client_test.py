import pytest
import os
from types import GeneratorType
from evm_client.batch_client.eth_client import BatchEthClient
from evm_client.sync_client.eth_client import SyncEthClient
from constants import ETH_USDC, TRANSFER_TOPIC

@pytest.fixture(scope="session")
def rpc_url():
    return "https://eth.llamarpc.com"#os.getenv("ETH_RPC_URL")

@pytest.fixture(scope="session")
def client(rpc_url):
    return BatchEthClient(rpc_url)

@pytest.fixture(scope="session")
def block_number(rpc_url):
    client = SyncEthClient(rpc_url)
    return client.block_number()

@pytest.fixture(scope="session")
def usdc():
    return ETH_USDC

@pytest.fixture(scope="session")
def tt():
    return TRANSFER_TOPIC

def test_batch_get_logs(client, usdc, tt, block_number):
    logs = client.get_logs(usdc, [tt], block_number - 10000, block_number)
    assert isinstance(logs, GeneratorType)

def test_batch_get_blocks_by_numbers(client, block_number):
    block_numbers = list(range(block_number - 100, block_number))
    blocks = client.get_blocks_by_numbers(block_numbers)
    assert isinstance(blocks, GeneratorType)
    for b in blocks:
        for k, v in b.items():
            print(k, v)
        print()
        
