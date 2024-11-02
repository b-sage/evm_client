import pytest
import os
from constants import ERC20_ABI, ETH_USDC
from evm_client.contract import Contract
from evm_client.sync_client import SyncEthClient

@pytest.fixture(scope="session")
def rpc_url():
    return "https://eth.llamarpc.com"#os.getenv("ETH_RPC_URL") 

@pytest.fixture(scope="session")
def client(rpc_url):
    return SyncEthClient(rpc_url)

@pytest.fixture(scope="session")
def usdc():
    return ETH_USDC

@pytest.fixture(scope="session")
def abi():
    return ERC20_ABI

@pytest.fixture(scope="session")
def contract(usdc, abi):
    return Contract(usdc, abi)

@pytest.fixture(scope="session")
def n(client):
    return client.block_number()

def test_name(client, contract):
    name = client.call(
        contract.functions.name.build_transaction(), 
        decoder=contract.functions.name.decode_result
    )
    assert type(name) == str
    assert name == 'USD Coin'

def test_symbol(client, contract):
    symbol = client.call(
            contract.functions.symbol.build_transaction(),
            decoder=contract.functions.symbol.decode_result
    )
    assert type(symbol) == str
    assert symbol == 'USDC'

def test_decimals(client, contract):
    decimals = client.call(
            contract.functions.decimals.build_transaction(),
            decoder=contract.functions.decimals.decode_result
    )
    assert type(decimals) == int
    assert decimals == 6

def test_get_logs(client, contract, n):
    logs = client.get_logs(
        contract.events.Transfer.build_filter(from_block=n-100, to_block=n),
        decoder=contract.events.Transfer.decode_results
    )
    assert type(logs) == list
    for l in logs:
        assert type(l) == dict
        assert type(l['data']) == dict
        assert l.get('topics') is None

