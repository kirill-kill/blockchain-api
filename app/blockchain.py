import hashlib
import json
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        block = {
            "index": 0,
            "timestamp": time.time(),
            "data": "Genesis Block",
            "previous_hash": "0"
        }
        block["hash"] = self.hash(block)
        self.chain.append(block)

    def hash(self, block):
        block_copy = block.copy()
        block_copy.pop("hash", None)
        return hashlib.sha256(json.dumps(block_copy, sort_keys=True).encode()).hexdigest()

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last_block = self.get_last_block()

        new_block = {
            "index": last_block["index"] + 1,
            "timestamp": time.time(),
            "data": data,
            "previous_hash": last_block["hash"]
        }

        new_block["hash"] = self.hash(new_block)
        self.chain.append(new_block)

        return new_block

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]

            if current["previous_hash"] != prev["hash"]:
                return False

            if current["hash"] != self.hash(current):
                return False

        return True
