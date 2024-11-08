import pytest
import os
from types import GeneratorType
from evm_client.batch_client.eth_client import BatchEthClient
from evm_client.sync_client.eth_client import SyncEthClient
from evm_client.batch_client.utils import chunks
from evm_client.types import EthFilter
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

@pytest.fixture(scope="session")
def filter_(usdc, tt):
    return EthFilter(
            topics=[tt],
            address=usdc
    )

@pytest.fixture
def block_hashes(block_number, rpc_url):
    client = SyncEthClient(rpc_url)
    hashes = []
    for n in range(block_number - 100, block_number):
        block = client.get_block_by_number(n)
        hashes.append(block['hash'])
    return hashes


def test_batch_get_logs(client, filter_, block_number):
    block_range = list(range(block_number - 10000, block_number))
    chunked = chunks(block_range, 100)
    filters = []
    for c in chunked:
        filter_.set_from_block(c[0])
        filter_.set_to_block(c[-1])
        filters.append(filter_)
    logs = client.get_logs_batch(filters)
    assert isinstance(logs, GeneratorType)

def test_batch_get_blocks_by_numbers(client, block_number):
    block_numbers = list(range(block_number - 100, block_number))
    blocks = client.get_block_by_number_batch(block_numbers)
    assert isinstance(blocks, GeneratorType)

def test_batch_get_blocks_by_hashes(client, block_hashes):
    blocks = client.get_block_by_hash_batch(block_hashes)
    assert isinstance(blocks, GeneratorType)
