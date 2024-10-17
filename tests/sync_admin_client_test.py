import pytest
import os
from evm_client.sync_client.admin_client import SyncAdminClient
#NOTE: as I do not currently run my own node I am unable to test the admin endpoints.

@pytest.fixture
def client():
    rpc_url = os.getenv("ETH_RPC_URL")
    return SyncAdminClient(rpc_url)

@pytest.fixture
def peer_url():
    return ''

def test_add_peer(client, peer_url):
    pass

def test_add_trusted_peer(client, peer_url):
    pass

def test_datadir(client):
    pass

def test_export_chain(client):
    pass

def test_import_chain(client):
    pass

def test_node_info(client):
    info = client.node_info()
    print(info)

def test_peer_events(client):
    pass

def test_peers(client):
    pass

def test_remove_peer(client, peer_url):
    pass

def test_remove_trusted_peer(client, peer_url):
    pass

def test_start_http(client):
    pass

def test_stop_http(client):
    pass

def test_start_ws(cliet):
    pass

def test_stop_ws(client):
    pass

