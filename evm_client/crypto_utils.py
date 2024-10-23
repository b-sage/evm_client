from eth_abi import decode
from hexbytes import HexBytes
from eth_utils import to_checksum_address

def hex_to_int(hex_str: str):
    return int(hex_str, 16)

def unpack_address(packed_address: str):
    return to_checksum_address(decode(['address'], HexBytes(packed_address))[0])
