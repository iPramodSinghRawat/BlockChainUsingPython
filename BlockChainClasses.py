#
# simple BlockChain working with Proof of Work
# idea and logic taken from below link
# https://www.youtube.com/watch?v=HneatE69814
# to understand more follow the link
#

import hashlib
from time import time

class Block:

    def __init__(self, data):
        self.previous_hash = ''
        self.timestamp = time()
        self.data = data
        self.flag = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = self.previous_hash+str(self.timestamp)+self.data+str(self.flag)
        hash_string = hashlib.sha256(hash_string.encode()).hexdigest()
        return hash_string

    def mine_block(self,difficulty):

        while (self.hash[:difficulty] != ("0"*(difficulty))):
            self.flag += 1
            self.hash = self.calculate_hash()

        print("BLOCK MINED: ",self.hash)


class BlockChain:
    chain=[]
    difficulty = 0

    def __init__(self):
    #def __init__(self,difficulty):
        self.chain = [self.create_genesis_block()]
        #print("ghash ",self.create_genesis_block().hash)
        self.difficulty = 2 # can be passed as variable the greater it is the more time it will take to create new block
        #self.difficulty = difficulty

    def create_genesis_block(self):
        return Block("Genesis Block")

    def get_last_block(self):
        return self.chain[len(self.chain) - 1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):

        for i in range(1,len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if (current_block.hash != current_block.calculate_hash()):
                return False

            if (current_block.previous_hash != previous_block.hash):
                return False

        return True
