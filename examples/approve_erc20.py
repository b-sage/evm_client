from constants import WETH_ADDRESS, WETH_ABI, ACCT_PK, RPC_URL
from evm_client.sync_client import SyncEthClient
from evm_client.contract import Contract

def build_weth_approval(client, weth_contract, account, spender=WETH_ADDRESS, amt=(10**18), gas=1000000):
    return weth_contract.functions.approve.build_transaction(
        spender,
        amt,
        from_=account.address,
        value=0,
        nonce=client.get_transaction_count(account.address),
        gas=gas,
        gas_price=client.gas_price()
    )

if __name__ == '__main__':
    client = SyncEthClient(RPC_URL)
    weth = Contract(WETH_ADDRESS, WETH_ABI)

    approval = build_weth_approval(client, weth, acct)
    signed = approval.sign(ACCT_PK)
    tx_hash = client.send_raw_transaction(signed.raw_transaction.hex())
    print(tx_hash)

