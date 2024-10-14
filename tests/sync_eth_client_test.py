import pytest
from evm_client.sync_client import SyncEthClient
from constants import ETH_RPC_URL, NULL_ADDRESS, WETH

@pytest.fixture
def client():
    return SyncEthClient(ETH_RPC_URL)

@pytest.fixture
def null_address():
    return NULL_ADDRESS

@pytest.fixture
def weth():
    return WETH

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

def test_eth_chain_id(client):
    chain_id = client.chain_id()
    print(chain_id)
    assert type(chain_id) == int

def test_coinbase(client):
    coinbase = client.coinbase()
    print(coinbase)
    assert type(coinbase) == str

def test_mining(client):
    mining = client.mining()
    print(mining)
    assert type(mining) == bool

def test_hashrate(client):
    hashrate = client.hashrate()
    print(hashrate)
    assert type(hashrate) == int

def test_gas_price(client):
    gas_price = client.gas_price()
    print(gas_price)
    assert type(gas_price) == int

def test_accounts(client):
    accounts = client.accounts()
    print(accounts)
    assert type(accounts) == list

def test_get_storage_at(client, weth):
    storage_at = client.get_storage_at(weth, 1)
    print(storage_at)
    assert type(storage_at) == str

def test_get_transaction_count(client, weth):
    tx_count = client.get_transaction_count(weth)
    print(tx_count)
    assert type(tx_count) == int
