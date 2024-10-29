from evm_client.parsers.base import BaseParser
from evm_client.crypto_utils import hex_to_int
from evm_client.parsers.utils import assert_int

def parse_raw_hex_to_int(hex_str: str):
    return HexToIntParser(hex_to_int(hex_str))

class HexToIntParser(BaseParser):

    def __init__(self, value: int):
        assert_int(self.value)
        self.value = value

    def default_format(self):
        if self.value:
            return self.value
        return
