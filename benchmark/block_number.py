import time
from web3 import Web3
from evm_client.sync_client import EthClient
from constants import ETH_RPC_URL

def time_w3_block_number():
    w3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))
    t = time.time()
    block_num = w3.eth.get_block_number()
    result = time.time() - t
    print("W3 RESULT: {}".format(result))

#not yet a true test... this client isn't parsing the result
def time_evm_client_block_number():
    client = EthClient(ETH_RPC_URL)
    t = time.time()
    block_num = evm_client.block_number()
    result = time.time() - t
    print("EVM_CLIENT RESULT: {}".format(result))

if __name__ == '__main__':
    time_w3_block_number()
    time_evm_client_block_number()
