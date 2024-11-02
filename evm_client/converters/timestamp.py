from datetime import datetime
from typing import Union
from evm_client.converters import convert_hex_to_int

def convert_hex_to_datetime(hex_str: Union[str, None]):
    ts = convert_hex_to_int(hex_str)
    if ts:
        return datetime.utcfromtimestamp(ts)
    return

