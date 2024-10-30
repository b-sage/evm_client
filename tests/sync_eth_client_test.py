import pytest
import os
import time
from evm_client.sync_client import SyncEthClient
from evm_client.types import Transaction, EthFilter
from constants import NULL_ADDRESS, WETH, ETH_USDC, ETH_BINANCE_PEG_ADDR

#TODO: incorporate multiple networks
#TODO: cleanup fixtures. may make sense to test ex current block num and historical block num, current block hash vs historical etc

SLEEP_TIME = 1

@pytest.fixture(scope="session")
def client():
    rpc_url = os.getenv('ETH_RPC_URL')
    return SyncEthClient(rpc_url)

@pytest.fixture(scope="session")
def null_address():
    return NULL_ADDRESS

@pytest.fixture(scope="session")
def weth():
    return WETH

@pytest.fixture(scope="session")
def block_num(client):
    return client.block_number() - 10000

@pytest.fixture(scope="session")
def block(client, block_num):
    return client.get_block_by_number(block_num)

@pytest.fixture(scope="session")
def block_number(block):
    return block['number']

@pytest.fixture(scope="session")
def block_hash(block):
    return block['hash']

@pytest.fixture(scope="session")
def transaction_hash(block):
    return block['transactions'][0]['hash']

@pytest.fixture(scope="session")
def peg():
    return ETH_BINANCE_PEG_ADDR

@pytest.fixture(scope="session")
def transaction(null_address):
    return Transaction(
        '0x',
        to=null_address,
        from_=null_address,
        value=1
    )

@pytest.fixture(scope="session")
def usdc():
    return ETH_USDC

@pytest.fixture(scope="session")
def raw_transaction():
    return ''

@pytest.fixture(scope="session")
def usdc_balance_of_tx(usdc, peg, null_address):
    n = peg[2:]
    return Transaction(
        ('0x70a08231000000000000000000000000' + n).lower(),
        to=usdc
    )

@pytest.fixture(scope="session")
def usdc_filter_(client, usdc, block_number):
    return EthFilter(
        from_block=block_number-100,
        to_block=block_number,
        address=usdc,
        topics=["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"]
    )

@pytest.fixture(scope="session")
def filter_id(client, usdc_filter_):
    return client.new_filter(usdc_filter_)

@pytest.fixture(scope="session")
def subscription_id(client):
    return client.subscribe("logs")

def sleep(s=SLEEP_TIME):
    time.sleep(s)

def test_get_block_number(client):
    sleep()
    block_number = client.block_number()
    print(block_number)
    assert type(block_number) == int

#NOTE: cannot currently properly test using llamarpc
def test_protocol_version(client):
    sleep()
    protocol_version = client.protocol_version()
    print(protocol_version)
    assert type(protocol_version) == int

def test_syncing(client):
    sleep()
    syncing = client.syncing()
    print(syncing)
    assert type(syncing) == bool

def test_eth_get_balance(client, null_address, block_number):
    sleep()
    bal = client.get_balance(null_address, block_number=block_number)
    print(bal)
    assert type(bal) == int

def test_eth_chain_id(client):
    sleep()
    chain_id = client.chain_id()
    print(chain_id)
    assert type(chain_id) == int

def test_coinbase(client):
    sleep()
    coinbase = client.coinbase()
    print(coinbase)
    assert type(coinbase) == str

def test_mining(client):
    sleep()
    mining = client.mining()
    print(mining)
    assert type(mining) == bool

def test_hashrate(client):
    sleep()
    hashrate = client.hashrate()
    print(hashrate)
    assert type(hashrate) == int

def test_gas_price(client):
    sleep()
    gas_price = client.gas_price()
    print(gas_price)
    assert type(gas_price) == int

def test_accounts(client):
    sleep()
    accounts = client.accounts()
    print(accounts)
    assert type(accounts) == list

def test_get_storage_at(client, weth):
    sleep()
    storage_at = client.get_storage_at(weth, 1)
    print(storage_at)
    assert type(storage_at) == str

def test_get_transaction_count(client, weth):
    sleep()
    tx_count = client.get_transaction_count(weth)
    print(tx_count)
    assert type(tx_count) == int

def test_get_transaction(client, transaction_hash):
    sleep()
    tx = client.get_transaction(transaction_hash)
    print(tx)
    assert type(tx) == dict

def test_get_block_tx_count_by_hash(client, block_hash):
    sleep()
    tx_count = client.get_block_transaction_count_by_hash(block_hash)
    print(tx_count)
    assert type(tx_count) == int

def test_get_block_tx_count_by_number(client, block_number):
    sleep()
    tx_count = client.get_block_transaction_count_by_number(block_number)
    print(tx_count)
    assert type(tx_count) == int

def test_get_uncle_count_by_hash(client, block_hash):
    sleep()
    uncle_count = client.get_uncle_count_by_block_hash(block_hash)
    print(uncle_count)
    assert type(uncle_count) == int or uncle_count is None

def test_get_uncle_count_by_number(client, block_number):
    sleep()
    uncle_count = client.get_uncle_count_by_block_number(block_number)
    print(uncle_count)
    assert type(uncle_count) == int or uncle_count is None

def test_get_code(client, weth):
    sleep()
    code = client.get_code(weth)
    print(code)
    assert type(code) == str

#NOTE: cannot currently properly test with llamarpc
def test_sign(client, null_address):
    sleep()
    sign = client.sign(null_address, '0x')
    print(sign)
    assert type(sign) == dict

#NOTE: cannot currently properly test with llamrpc
def test_sign_transaction(client, transaction):
    sleep()
    sign = client.sign_transaction(transaction)
    print(sign)
    assert type(sign) == dict

#NOTE: cannot test this without actually executing a tx, costing me ETH. probably worth testing on a testnet for these types of calls
def test_sign_raw_transaction(client, raw_transaction):
    sleep()
    res = client.send_raw_transaction(raw_transaction)
    print(res)
    assert type(res) == str

def test_call(client, usdc_balance_of_tx):
    sleep()
    res = client.call(usdc_balance_of_tx)
    print(res)
    assert type(res) == str

def test_estimate_gas(client, transaction):
    sleep()
    res = client.estimate_gas(transaction)
    print(res)
    assert type(res) == int

def test_get_block_by_number(client, block_number):
    sleep()
    res = client.get_block_by_number(block_number)
    print(res)
    assert type(res) == dict

def test_get_block_by_hash(client, block_hash):
    sleep()
    res = client.get_block_by_hash(block_hash)
    print(res)
    assert type(res) == dict

def test_get_transaction_by_block_number_and_index(client, block_number):
    sleep()
    res = client.get_transaction_by_block_number_and_index(block_number, 0)
    print(res)
    assert type(res) == dict

def test_get_transaction_by_block_hash_and_index(client, block_hash):
    sleep()
    res = client.get_transaction_by_block_hash_and_index(block_hash, 0)
    print(res)
    assert type(res) == dict

def test_get_transaction_receipt(client, transaction_hash):
    sleep()
    res = client.get_transaction_receipt(transaction_hash)
    print(res)
    assert type(res) == dict

def test_get_uncle_by_block_hash_and_index(client, block_hash):
    sleep()
    res = client.get_uncle_by_block_hash_and_index(block_hash, 1)
    print(res)
    assert type(res) == str or res is None

def test_get_uncle_by_block_number_and_index(client, block_number):
    sleep()
    res = client.get_uncle_by_block_number_and_index(block_number, 1)
    print(res)
    assert type(res) == str or res is None

def test_blob_base_fee(client):
    sleep()
    blob = client.blob_base_fee()
    print(blob)
    assert type(blob) == int

def test_new_filter(client, usdc_filter_):
    sleep()
    filt = client.new_filter(usdc_filter_)
    print(filt)
    assert type(filt) == str

def test_new_block_filter(client):
    sleep()
    filt = client.new_block_filter()
    print(filt)
    assert type(filt) == str

def test_new_pending_transaction_filter(client):
    sleep()
    filt = client.new_pending_transaction_filter()
    print(filt)
    assert type(filt) == str

def test_filter_changes(client, filter_id):
    sleep()
    changes = client.get_filter_changes(filter_id)
    print(changes)
    assert type(changes) == list

def test_filter_logs(client, filter_id):
    sleep()
    logs = client.get_filter_logs(filter_id)
    print(logs)
    assert type(logs) == list

def test_uninstall_filter(client, filter_id):
    sleep()
    u = client.uninstall_filter(filter_id)
    print(u)
    assert type(u) == bool

def test_get_logs(client, usdc_filter_):
    sleep()
    logs = client.get_logs(usdc_filter_)
    print(logs)
    assert type(logs) == list

def test_get_account(client, weth):
    sleep()
    acct = client.get_account(weth)
    print(acct)
    assert type(acct) == dict

def test_block_receipts(client, block_number):
    sleep()
    receipts = client.get_block_receipts(block_number)
    print(receipts)
    assert type(receipts) == list

def test_max_priority_fee(client):
    sleep()
    fee = client.max_priority_fee_per_gas()
    print(fee)
    assert type(fee) == int

#NOTE: geth method, may not work on all clients
def test_subscribe(client):
    sleep()
    sub = client.subscribe("logs")
    print(sub)
    assert type(sub) == str

def test_unsubscribe(client, subscription_id):
    sleep()
    r = client.unsubscribe(subscription_id)
    print(r)
    assert type(r) == bool

def test_create_access_list(client, usdc_balance_of_tx):
    sleep()
    l = client.create_access_list(usdc_balance_of_tx)
    print(l)
    assert type(l) == dict

