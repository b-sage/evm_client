from typing import Optional
from evm_client.crypto_utils import hex_to_int
from evm_client.parsers import parse_raw_transaction
from evm_client.parsers.utils import assert_int, assert_str


#TODO: may be missing fields from other networks we'll have to fill as we test through
def parse_raw_block(block_dict):
    return ParsedBlock(
        base_fee_per_gas=hex_to_int(block_dict['baseFeePerGas']) if block_dict.get('baseFeePerGas') is not None else None,
        blob_gas_used=hex_to_int(block_dict['blobGasUsed']) if block_dict.get('blobGasUsed') is not None else None,
        difficulty=hex_to_int(block_dict['difficulty']) if block_dict.get('difficulty') is not None else None,
        excess_blob_gas=hex_to_int(block_dict['excessBlobGas']) if block_dict.get('excessBlobGas') is not None else None,
        extra_data=block_dict.get('extraData', None),
        gas_limit=hex_to_int(block_dict['gasLimit']) if block_dict.get('gasLimit') is not None else None,
        gas_used=hex_to_int(block_dict['gasUsed']) if block_dict.get('gasUsed') is not None else None,
        hash_=block_dict.get('hash', None),
        logs_bloom=block_dict.get('logsBloom', None),
        miner=block_dict.get('miner', None),
        mix_hash=block_dict.get('mixHash', None),
        nonce=hex_to_int(block_dict['nonce']) if block_dict.get('nonce') is not None else None,
        number=hex_to_int(block_dict['number']) if block_dict.get('number') is not None else None,
        parent_beacon_block_root=block_dict.get('parentBeaconBlockRoot', None),
        parent_hash=block_dict.get('parentHash', None),
        receipts_root=block_dict.get('receiptsRoot', None),
        sha3_uncles=block_dict.get('sha3Uncles', None),
        size=hex_to_int(block_dict['size']) if not block_dict.get('size') is not None else None,
        state_root=block_dict.get('stateRoot', None),
        timestamp=hex_to_int(block_dict['timestamp']) if block_dict.get('timestamp') is not None else None,
        total_difficulty=hex_to_int(block_dict['totalDifficulty']) if block_dict.get('totalDifficulty') is not None else None,
        transactions=[parse_raw_transaction(tx).to_dict() for tx in block_dict['transactions']] if block_dict.get('transactions') is not None else None
    )

class ParsedBlock:

    #TODO: these are not actually all optional, but in trying to be robust to cover many networks we'll leave them as such until we have a better
    #idea of which fields are consistent across networks and which aren't.
    def __init__(
        self,
        base_fee_per_gas: Optional[int]=None,
        blob_gas_used: Optional[int]=None,
        difficulty: Optional[int]=None,
        excess_blob_gas: Optional[int]=None,
        extra_data: Optional[str]=None,
        gas_limit: Optional[int]=None,
        gas_used: Optional[int]=None,
        hash_: Optional[str]=None,
        logs_bloom: Optional[str]=None,
        miner: Optional[str]=None,
        mix_hash: Optional[str]=None,
        nonce: Optional[int]=None,
        number: Optional[int]=None,
        parent_beacon_block_root: Optional[str]=None,
        parent_hash: Optional[str]=None,
        receipts_root: Optional[str]=None,
        sha3_uncles: Optional[str]=None,
        size: Optional[str]=None,
        state_root: Optional[str]=None,
        timestamp: Optional[int]=None,
        total_difficulty: Optional[int]=None,
        transactions: Optional[list]=None
    ):
        assert_int(base_fee_per_gas)
        self.base_fee_per_gas = base_fee_per_gas
        assert_int(blob_gas_used)
        self.blob_gas_used = blob_gas_used
        assert_int(difficulty)
        self.difficulty = difficulty
        assert_int(excess_blob_gas)
        self.excess_blob_gas = excess_blob_gas
        assert_str(extra_data)
        self.extra_data = extra_data
        assert_int(gas_limit)
        self.gas_limit = gas_limit
        assert_int(gas_used)
        self.gas_used = gas_used
        assert_str(hash_)
        self.hash = hash_
        assert_str(logs_bloom)
        self.logs_bloom = logs_bloom
        assert_str(miner)
        self.miner = miner
        assert_str(mix_hash)
        self.mix_hash = mix_hash
        assert_int(nonce)
        self.nonce = nonce
        assert_int(number)
        self.number = number
        assert_str(parent_beacon_block_root)
        self.parent_beacon_block_root = parent_beacon_block_root
        assert_str(parent_hash)
        self.parent_hash = parent_hash
        assert_str(receipts_root)
        self.receipts_root = receipts_root
        assert_str(sha3_uncles)
        self.sha3_uncles = sha3_uncles
        assert_int(size)
        self.size = size
        assert_str(state_root)
        self.state_root = state_root
        assert_int(timestamp)
        self.timestamp = timestamp
        assert_int(total_difficulty)
        self.total_difficulty = total_difficulty
        assert type(transactions) == list or transactions is None
        self.transactions = transactions

    def as_dict(self):
        return {
            "baseFeePerGas": self.base_fee_per_gas,
            "blobGasUsed": self.blob_gas_used,
            "difficulty": self.difficulty,
            "excessBlobGas": self.excess_blob_gas,
            "extraData": self.extra_data,
            "gasLimit": self.gas_limit,
            "gasUsed": self.gas_used,
            "hash": self.hash,
            "logsBloom": self.logs_bloom,
            "miner": self.miner,
            "mixHash": self.mix_hash,
            "nonce": self.nonce,
            "number": self.number,
            "parentBeaconBlockRoot": self.parent_beacon_block_root,
            "parentHash": self.parent_hash,
            "receiptsRoot": self.receipts_root,
            "sha3Uncles": self.sha3_uncles,
            "size": self.size,
            "stateRoot": self.state_root,
            "timestamp": self.timestamp,
            "totalDifficulty": self.total_difficulty,
            "transactions": self.transactions
        }

    def to_dict(self):
        d = self.as_dict()
        return {k:v for k,v in d.items() if v is not None}



