from constants import ACCT_PK, RPC_URL
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
    client = SyncEthClient(RPC_URL)
    tx = build_transfer(client, acct)
    signed = tx.sign(ACCT_PK)
    tx_hash = client.send_raw_transaction(signed.raw_transaction.hex())
    print(tx_hash)
