from constants import WETH_ADDRESS, WETH_ABI, ACCT_ADDRESS, ACCT_PK, RPC_URL
from evm_client.sync_client import SyncEthClient
from evm_client.contract import Contract
from eth_account import Account

def create_weth_deposit_tx(client, weth_contract, account, amount, gas=1000000):
    return weth_contract.functions.deposit.build_transaction(
        from_=acct.address,
        value=amount,
        nonce=client.get_transaction_count(acct.address),
        gas=gas,
        gas_price=client.gas_price()
    )

if __name__ == '__main__':
    client = SyncEthClient(RPC_URL)
    weth = Contract(WETH_ADDRESS, WETH_ABI)
    acct = Account.from_key(ACCT_PK)

    weth_deposit = create_weth_deposit_tx(client, weth, acct, (10 ** 18))
    signed = acct.sign_transaction(weth_deposit.to_json())
    tx_hash = client.send_raw_transaction(signed.raw_transaction.hex())
    print(tx_hash)


