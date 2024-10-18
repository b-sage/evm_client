import pytest
import os
from evm_client.sync_client.net_client import SyncNetClient

@pytest.fixture
def client():
    rpc_url = os.getenv('ETH_RPC_URL')
    return SyncNetClient(rpc_url)

def test_listening(client):
    l = client.listening()
    print(l)
    assert type(l) == bool

def test_peer_count(client):
    peer_count = client.peer_count()
    print(peer_count)
    assert type(peer_count) == int

def test_version(client):
    v = client.version()
    print(v)
    assert type(v) == str
