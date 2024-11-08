from constants import WETH_ADDRESS, WETH_ABI, ACCT_ADDRESS, RPC_URL
from evm_client.contract import Contract
from evm_client.sync_client import SyncEthClient

def get_balance_of(client, weth_contract, address):
    return weth_contract.functions.balanceOf.build_transaction(
        address
    )

if __name__ == '__main__':
    client = SyncEthClient(RPC_URL)
    weth = Contract(WETH_ADDRESS, WETH_ABI)

    tx = get_balance_of(client, weth, ACCT_ADDRESS)
    result = client.call(tx, decoder=weth.functions.balanceOf.decode_result)
    print(result)

