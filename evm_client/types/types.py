from typing import Optional, Union, List

class Transaction:

    def __init__(
            self, 
            from_: str,
            input_: str,
            to: Optional[str]=None, 
            gas: Optional[int]=None, 
            gas_price: Optional[int]=None, 
            value: Optional[int]=None, 
            nonce: Optional[int]=None
    ):
        self.from_ = from_
        self.to = to
        self.gas = gas
        self.gas_price = gas_price
        self.value = value
        self.input_ = input_
        self.nonce = nonce
        self.json = {
            "from": self.from_,
            "to": self.to,
            "gas": self.gas,
            "gasPrice": self.gas_price,
            "input": self.input_,
            "nonce": self.nonce
        }

    def to_json(self):
        json = {}
        for k, v in self.json.items():
            if type(v) == int:
                v = str(hex(v))
            if v is not None:
                json[k] = v
        return json


class EthFilter:

    def __init__(
            self, 
            from_block: Optional[Union[int, str]]="latest", 
            to_block: Optional[Union[int, str]]="latest", 
            address: Optional[str]=None, 
            topics: Optional[List[str]]=None,
            block_hash: Optional[str]=None
    ):
        self.from_block = from_block
        self.to_block = to_block
        self.address = address
        self.topics = topics
        self.block_hash = block_hash
        self.json = {
                "fromBlock": self.from_block,
                "toBlock": self.to_block,
                "address": self.address,
                "topics": self.topics,
                "blockHash": self.block_hash
        }

    def to_json(self):
        json = {}
        for k, v in self.json.items():
            if type(v) == int:
                v = str(hex(v))
            if v is not None:
                json[k] = v
        return json
