from typing import Optional

class Transaction:

    def __init__(
            self, 
            from_: str, 
            to: Optional[str]=None, 
            gas: Optional[int]=None, 
            gas_price: Optional[int]=None, 
            value: Optional[int]=None, 
            input_: str,
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
        return {k: v for k, v in self.json.items() if v is not None}

