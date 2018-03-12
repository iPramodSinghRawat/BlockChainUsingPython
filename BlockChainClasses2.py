#
# With Miner Reward and Transactions
# idea and logic taken from below link
# https://www.youtube.com/watch?v=fRV6cGXVQ4I
# to understand more follow the link
#

import hashlib
import json

from time import time

#Transaction Class
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time()

class OldTransaction(Transaction):
    def __init__(self, sender, receiver, amount, timestamp):
        Transaction.__init__(self, sender, receiver, amount)
        self.timestamp = timestamp

#Block Class
class Block:

    def __init__(self, transactions_data):
        self.previous_hash = '0'
        self.timestamp = time()
        self.transactions_data = transactions_data
        self.flag = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # transaction list to json string to create transaction list data hash
        json_string = json.dumps([obj.__dict__ for obj in self.transactions_data])

        hash_string = self.previous_hash+str(self.timestamp)+json_string+str(self.flag)
        hash_string = hashlib.sha256(hash_string.encode()).hexdigest()
        return hash_string

    def mine_block(self,difficulty):
        while (self.hash[:difficulty] != ("0"*(difficulty))):
            self.flag += 1
            self.hash = self.calculate_hash()

#BlockChain Class
class BlockChain:
    chain=[]
    difficulty = 0

    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2 # can be passed as variable
        self.pending_transactions = []
        self.mining_reward = 10

    def create_genesis_block(self):
        return Block([])

    def get_last_block(self):
        return self.chain[len(self.chain) - 1]

    def mine_pending_transactions(self,mining_reward_address):

        transaction_block = Block(self.pending_transactions)
        transaction_block.previous_hash = self.get_last_block().hash
        transaction_block.mine_block(self.difficulty)

        print('Block successfully mined!')

        self.chain.append(transaction_block)

        self.pending_transactions = [Transaction(None, mining_reward_address, self.mining_reward)]

    def create_transaction(self,transaction_data):
        self.pending_transactions.append(transaction_data)

    '''
    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        #print("New Block pre_hash: ", new_block.previous_hash)
        self.chain.append(new_block)
    '''

    def get_balance_of_address(self, address):
        balance = 0

        for i in range(len(self.chain)):

            block_transactions_data = self.chain[i].transactions_data

            for j in range(len(block_transactions_data)):
                transaction_data = block_transactions_data[j]

                if(transaction_data.receiver == address):
                    balance += transaction_data.amount

                if(transaction_data.sender == address):
                    balance -= transaction_data.amount

        return balance

    def is_chain_valid(self):

        for i in range(1,len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if (current_block.hash != current_block.calculate_hash()):
                #print("current block != ")
                return False

            if (current_block.previous_hash != previous_block.hash):
                #print("current block previous_hash != previous_block.hash")
                return False

        return True
