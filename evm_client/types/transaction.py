from typing import Optional

#TODO: think we need both SignedTransaction and UnsignedTransaction types

class Transaction:

    def __init__(
            self, 
            input_: str,
            from_: Optional[str]=None,
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
            "data": self.input_,
            "nonce": self.nonce,
            "value": self.value
        }

    def to_json(self):
        json = {}
        for k, v in self.json.items():
            if type(v) == int:
                v = str(hex(v))
            elif type(v) == float:
                v = str(hex(int(v)))
            if v is not None:
                json[k] = v
        return json

