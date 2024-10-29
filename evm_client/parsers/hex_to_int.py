from evm_client.crypto_utils import hex_to_int

def parse_raw_hex_to_int(hex_str: str):
    if hex_str:
        return hex_to_int(hex_str)
    return

