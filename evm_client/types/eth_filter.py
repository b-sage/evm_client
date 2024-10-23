from typing import Optional, Union, List

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

    def set_from_block(self, from_block: Union[int, str]):
        self.from_block = from_block
        self.json['fromBlock'] = from_block

    def set_to_block(self, to_block: Union[int, str]):
        self.to_block = to_block
        self.json['toBlock'] = to_block

    def to_json(self):
        json = {}
        for k, v in self.json.items():
            if type(v) == int:
                v = str(hex(v))
            if v is not None:
                json[k] = v
        return json

