from constants import WETH_ADDRESS, WETH_ABI, ACCT_ADDRESS, ACCT_PK, RPC_URL
from evm_client.sync_client import SyncEthClient
from evm_client.contract import Contract

def create_weth_deposit_tx(client, weth_contract, account, amount=(10**18), gas=1000000):
    return weth_contract.functions.deposit.build_transaction(
        from_=account.address,
        value=amount,
        nonce=client.get_transaction_count(account.address),
        gas=gas,
        gas_price=client.gas_price()
    )

if __name__ == '__main__':
    client = SyncEthClient(RPC_URL)
    weth = Contract(WETH_ADDRESS, WETH_ABI)

    weth_deposit = create_weth_deposit_tx(client, weth, acct)
    signed = weth_deposit.sign(ACCT_PK)
    tx_hash = client.send_raw_transaction(signed.raw_transaction.hex())
    print(tx_hash)


