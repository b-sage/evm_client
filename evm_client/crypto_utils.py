from eth_abi import decode
from hexbytes import HexBytes
from eth_utils import to_checksum_address

def hex_to_int(hex_str: str):
    return int(hex_str, 16)

def unpack_address(packed_address: str):
    return to_checksum_address(decode(['address'], HexBytes(packed_address))[0])

def decode_string(hex_str: str):
    return decode(['string'], HexBytes(hex_str))[0]

def decode_bytes32(hex_str: str):
    return decode(['bytes32'], HexBytes(hex_str))[0]
