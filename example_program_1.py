#
# simple BlockChain working with Proof of Work
# idea and logic taken from below link
# https://www.youtube.com/watch?v=HneatE69814
# to understand more follow the link
#

import json

from BlockChainClasses import Block,BlockChain

first_block_chain = BlockChain()

print('Mining block 1...')
#first_block = Block("first Block data")
#first_block_chain.add_block(first_block)
first_block_chain.add_block(Block("first Block data"))

print('Mining block 2...')
#second_block = Block("2 Block data")
#first_block_chain.add_block(second_block)
first_block_chain.add_block(Block("2 Block data"))

print('Blockchain valid? ', first_block_chain.is_chain_valid())

#testing validity of block chain

print('Changing a block...')

first_block_chain.chain[1].data ="change first block data"
first_block_chain.chain[1].hash = first_block_chain.chain[1].calculate_hash()

print('Blockchain valid? ', first_block_chain.is_chain_valid())
