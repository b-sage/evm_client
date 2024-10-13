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
    return int(client.block_number().json()['result'], 16)


def test_get_block_number(client):
    block_number = client.block_number()
    print(block_number.json())
    assert type(block_number.json()) == dict
    assert block_number.status_code == 200

def test_protocol_version(client):
    protocol_version = client.protocol_version()
    print(protocol_version.json())
    assert type(protocol_version.json()) == dict
    assert protocol_version.status_code == 200

def test_syncing(client):
    syncing = client.syncing()
    print(syncing.json())
    assert type(syncing.json()) == dict
    assert syncing.status_code == 200

def test_eth_get_balance(client, null_address, block_num):
    bal = client.get_balance(null_address, block_number=block_num)
    print(bal.json())
    assert type(bal.json()) == dict
    assert bal.status_code == 200
