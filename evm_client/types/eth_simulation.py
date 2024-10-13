
class Withdrawals:

    def __init__(self, idx: int, validator_idx: int, address: str, amount: int):
        self.idx = idx
        self.validator_idx = validator_idx
        self.address = address
        self.amount = amount


class BlockOverrides:
    
    def __init__(self, block_number: int, prev_randao: int, time: int, gas_limit: int, fee_receipient: int, withdrawals: Withdrawals, base_fee_per_gas: int, blob_base_fee: int):
        self.block_number = block_number
        self.prev_randao = prev_randao
        self.time = time
        self.gas_limit = gas_limit
        self.fee_recipient = fee_recipient
        self.withdrawals = withdrawals
        self.base_fee_per_gas = base_fee_per_gas
        self.blob_base_fee = blob_base_fee




class BlockStateCalls:
    pass

