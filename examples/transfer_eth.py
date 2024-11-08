from constants import ACCT_PK, RPC_URL
from eth_account import Account
from evm_client.sync_client import SyncEthClient
from evm_client.types import Transaction

def build_transfer(client, account, value=(10**18), gas=1000000):
    return Transaction(
            '',
            to=account.address,
            from_=account.address,
            value=value,
            nonce=client.get_transaction_count(account.address),
            gas=gas,
            gas_price=client.gas_price()
    )

if __name__ == '__main__':
    acct = Account.from_key(ACCT_PK)
    client = SyncEthClient(RPC_URL)
    tx = build_transfer(client, acct)
    signed = acct.sign_transaction(tx.to_json())
    tx_hash = client.send_raw_transaction(signed.raw_transaction.hex())
    print(tx_hash)
