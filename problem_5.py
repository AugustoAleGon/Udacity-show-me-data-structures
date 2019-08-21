from datetime import datetime
import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def get_gmt_time(self):
        return datetime.utcfromtimestamp(float(self.timestamp))

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.timestamp.encode('utf-8') + self.data.encode('utf-8')
        if self.previous_hash != None:
            hash_str+= self.previous_hash.hash.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:
    
    def __init__(self):
        self.tail = None
    
    def add(self, data):
        if data == None:
            return
        if self.tail is None:
            self.tail = Block(str(datetime.now().timestamp()), data, None)
        else:
            tail = self.tail
            new_tail = Block(str(datetime.now().timestamp()), data, tail)
            self.tail = new_tail
        return self.tail

    def print_blockchain(self):
        tail = self.tail
        while tail is not None:
            print("<-", tail.data, tail.hash, tail.get_gmt_time())
            tail = tail.previous_hash
    

def test_block_created():
    blockchain = BlockChain()
    blockchain.add("hey")
    blockchain.add("lets")
    blockchain.print_blockchain()


def _check_hash(hash_previous, hash_after):
    current = hash_previous
    after = hash_after

    while current is not None:
        current_hash = current.hash
        if after.previous_hash.hash != current_hash:
            return "Not Passed"
        after = current
        current = current.previous_hash

    return "Pass"


def test_hash_matching():
    blockchain = BlockChain()
    blockchain.add("hey")
    blockchain.add("lets")
    print(_check_hash(blockchain.tail.previous_hash, blockchain.tail))


def test_created_before():
    blockchain = BlockChain()
    start = blockchain.add("hey")
    blockchain.add("lets")

    current = blockchain.tail
    while current.previous_hash is not None:
        current = current.previous_hash

    print("Pass" if current == start else "Not Passed")

def test_empty_blockchain():
    blockchain = BlockChain()
    blockchain.add("")
    blockchain.add(None)
    blockchain.print_blockchain()

test_block_created()
test_hash_matching()
test_created_before()
test_empty_blockchain()