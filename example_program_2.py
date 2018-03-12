#
# With Miner Reward and Transactions
# idea and logic taken from below link
# https://www.youtube.com/watch?v=fRV6cGXVQ4I
# to understand more follow the link
#

import json

from time import time
from BlockChainClasses2 import Transaction,Block,BlockChain

# let initial be 1000
#let say initially A have only 200 Coins
# a to b Rs 120
# b to c Rs 100
# c to d Rs 50
# d to a Rs 20

# miner_a
# miner_b

transaction_1 = Transaction("a","b",120)# remaining 120 after transfer
transaction_2 = Transaction("b","c",100)# remaining 20 after transfer
transaction_3 = Transaction("c","d",60)# remaining 40 after transfer
transaction_4 = Transaction("d","a",20)# remaining 40 after transfer

block_chain_obj = BlockChain()
block_chain_obj.create_transaction(transaction_1)
block_chain_obj.create_transaction(transaction_2)

print('\n Starting the Miner...')

block_chain_obj.mine_pending_transactions('miner_a')

print('\nBlockchain valid? ', block_chain_obj.is_chain_valid())

print('\nBalance of miner_a is: ', block_chain_obj.get_balance_of_address('miner_a'))

print('\n Starting the Miner again...')

block_chain_obj.mine_pending_transactions('miner_a') #transcation mined by miner_a

print('\nBalance of miner_a is: ', block_chain_obj.get_balance_of_address('miner_a'))
print('\nBlockchain valid? ', block_chain_obj.is_chain_valid())

block_chain_obj.create_transaction(transaction_3)

print('\n Starting the Miner again...')
block_chain_obj.mine_pending_transactions('miner_a')

print('\nBalance of miner_a is: ', block_chain_obj.get_balance_of_address('miner_a'))
print('\nBlockchain valid? ', block_chain_obj.is_chain_valid())


print('\nBalance of A is: ', block_chain_obj.get_balance_of_address('a'))
print('\nBalance of B is: ', block_chain_obj.get_balance_of_address('b'))
print('\nBalance of C is: ', block_chain_obj.get_balance_of_address('c'))
print('\nBalance of D is: ', block_chain_obj.get_balance_of_address('d'))

block_chain_obj.create_transaction(transaction_4)

print('\n Starting the miner again ...')
block_chain_obj.mine_pending_transactions('miner_a')

print('\nBalance of D is: ', block_chain_obj.get_balance_of_address('d'))
print('\nBalance of A is: ', block_chain_obj.get_balance_of_address('a'))

print('\nBalance of miner_a is: ', block_chain_obj.get_balance_of_address('miner_a'))
print('\nBlockchain valid? ', block_chain_obj.is_chain_valid())
