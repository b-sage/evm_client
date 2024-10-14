#NOTE: parsers need some thought... blocks, transactions, etc can look different across networks
from evm_client.crypto_utils import hex_to_int

class TransactionParser:

    def __init__(
        self,
        block_hash: str,
        block_number: str,
        from_: str,
        gas: str,
        gas_price: str,
        hash_: str,
        input_: str,
        nonce: str,
        r: str,
        s: str,
        to: str,
        transaction_index: str,
        type_: str,
        v: str,
        value: str
    ):
        self.block_hash = block_hash
        self.block_number = block_number
        self.from_ = from_
        self.gas = gas
        self.gas_price = gas_price
        self.hash_ = hash_
        self.input_ = input_
        self.nonce = nonce
        self.r = r
        self.s = s
        self.to = to
        self.transaction_index = transaction_index
        self.type_ = type_
        self.v = v
        self.value = value

    @classmethod
    def from_raw_json(cls, d):
        return cls(
            d['blockHash'],
            d['blockNumber'],
            d['from'],
            d['gas'],
            d['gasPrice'],
            d['hash'],
            d['input'],
            d['nonce'],
            d['r'],
            d['s'],
            d['to'],
            d['transactionIndex'],
            d['type'],
            d['v'],
            d['value']
        )

    def to_json(self):
        return {
            "blockHash": self.block_hash,
            "blockNumber": hex_to_int(self.block_number),
            "from": self.from_,
            "gas": hex_to_int(self.gas),
            "gasPrice": hex_to_int(self.gas_price),
            "hash": self.hash_,
            "input": self.input_,
            "nonce": hex_to_int(self.nonce),
            "r": self.r,
            "s": self.s,
            "to": self.to,
            "transactionIndex": hex_to_int(self.transaction_index),
            "type": hex_to_int(self.type_),
            "v": hex_to_int(self.v),
            "value": hex_to_int(self.value)
        }







{'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd', 'blockNumber': '0xb443', 'from': '0xa1e4380a3b1f749673e270229993ee55f35663b4', 'gas': '0x5208', 'gasPrice': '0x2d79883d2000', 'hash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060', 'input': '0x', 'nonce': '0x0', 'r': '0x88ff6cf0fefd94db46111149ae4bfc179e9b94721fffd821d38d16464b3f71d0', 's': '0x45e0aff800961cfce805daef7016b9b675c137a6a41a548f7b60a3484c06a33a', 'to': '0x5df9b87991262f6ba471f09758cde1c0fc1de734', 'transactionIndex': '0x0', 'type': '0x0', 'v': '0x1c', 'value': '0x7a69'}

