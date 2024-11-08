import pytest
import os
from types import GeneratorType
from evm_client.batch_client.eth_client import BatchEthClient
from evm_client.sync_client.eth_client import SyncEthClient
from evm_client.batch_client.utils import chunks
from evm_client.types import EthFilter
from evm_client.contract import Contract
from constants import ETH_USDC, ERC20_ABI

@pytest.fixture(scope="session")
def rpc_url():
    return "https://eth.llamarpc.com"#os.getenv("ETH_RPC_URL")

@pytest.fixture(scope="session")
def client(rpc_url):
    return BatchEthClient(rpc_url)

@pytest.fixture(scope="session")
def block(rpc_url):
    client = SyncEthClient(rpc_url)
    return client.get_block_by_number("latest")

@pytest.fixture(scope="session")
def block_number(block):
    return block['number']

@pytest.fixture(scope="session")
def block_hash(block):
    return block['hash']

@pytest.fixture(scope="session")
def usdc():
    return Contract(ETH_USDC, ERC20_ABI)

@pytest.fixture(scope="session")
def transfer_filter(usdc):
    return usdc.events.Transfer.build_filter()

@pytest.fixture(scope="session")
def block_numbers(block_number):
    return list(range(block_number - 100, block_number))

@pytest.fixture(scope="session")
def blocks(client, block_numbers):
    return client.get_block_by_number_batch(block_numbers)

@pytest.fixture(scope="session")
def block_hashes(blocks):
    return [block['hash'] for block in blocks]

@pytest.fixture(scope="session")
def transaction_hashes(block):
    return [tx['hash'] for tx in block['transactions']]

def test_batch_get_logs(client, transfer_filter, block_numbers):
    chunked = chunks(block_numbers, 100)
    filters = []
    for c in chunked:
        transfer_filter.set_from_block(c[0])
        transfer_filter.set_to_block(c[-1])
        filters.append(transfer_filter)
    logs = client.get_logs_batch(filters)
    assert isinstance(logs, GeneratorType)

def test_batch_get_blocks_by_numbers(client, block_numbers):
    blocks = client.get_block_by_number_batch(block_numbers)
    assert isinstance(blocks, GeneratorType)

def test_batch_get_blocks_by_hashes(client, block_hashes):
    blocks = client.get_block_by_hash_batch(block_hashes)
    assert isinstance(blocks, GeneratorType)

def test_batch_get_transactions(client, transaction_hashes):
    transactions = client.get_transaction_batch(transaction_hashes)
    assert isinstance(transactions, GeneratorType)
