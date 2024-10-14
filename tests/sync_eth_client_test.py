import pytest
from evm_client.sync_client import SyncEthClient
from constants import ETH_RPC_URL, NULL_ADDRESS

@pytest.fixture
def client():
    return SyncEthClient(ETH_RPC_URL)

@pytest.fixture
def null_address():
    return NULL_ADDRESS

@pytest.fixture
def block_num(client):
    return client.block_number()


def test_get_block_number(client):
    block_number = client.block_number()
    print(block_number)
    assert type(block_number) == int

def test_protocol_version(client):
    protocol_version = client.protocol_version()
    print(protocol_version)
    assert type(protocol_version) == str

def test_syncing(client):
    syncing = client.syncing()
    print(syncing)
    assert type(syncing) == bool

def test_eth_get_balance(client, null_address, block_num):
    bal = client.get_balance(null_address, block_number=block_num)
    print(bal)
    assert type(bal) == int
