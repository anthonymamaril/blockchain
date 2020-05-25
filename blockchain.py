import time
import hashlib
import json

blockchain = []
transactions = [
    "hello", # data for block at index 1
    "hi", # data for index 2
    "ECU", # data for index 3
    "Science", # data for index 4
    "Uni", # data for index 5 
    ]

print("Mine a new block and add it to the blockchain")
print("prefixHash: , fourteen zeros")

# generate the hash to the block ### is _hashPrevBlock
def getBlockHash(prev_hash, blockData, nonce):
  # concatenate prev_hash, data and stringified nonce
  data = prev_hash + blockData + str(nonce)
  # convert hashData to bytes
  hdToBytes = data.encode()
  # compute the hash of the bytes data
  hash = hashlib.sha256(hdToBytes)
  # convert bytes to hexadecimal
  hashDigest = hash.hexdigest()
  return hashDigest

# _newBlock
# guess the nonce (a random number) that when added to prev_hash & data will result in a hash that has however many '0' as the start
# input (prev_hash, data)
# output -> nonce (the correct nonce)
def mine(prev_hash, data):
  print('Mining block ', " ...")
  nonce = 0
  # compute the hash
  computedHash = getBlockHash(prev_hash, data, nonce)
  while computedHash[0:14] != '00000000000000':
    # if nonce reaches the limit
    if nonce >= 50000:
      # terminate the while loop
      break
    # increment the nonce
    nonce += 1
    # compute the hash using the incremented nonce
    computedHash = getBlockHash(prev_hash, data, nonce)
  print(prev_hash, data, nonce)
  print("Computed hash: ", computedHash, "\n")
  return nonce

# construct the block and add it to the blockchain ### _newBlock()
def addBlockToChain(prev_hash, data, nonce, blockHash):
  nextBlock = {
    # the index of the next block is the current length of the blockchain (i.e. lastIndex + 1)
    'index': len(blockchain),
    'prev_hash': prev_hash,
    'data': data,
    'timestamp': int(time.time()), # unix timestamp,
    'nonce': nonce,
    'blockHash': blockHash
  }
  blockchain.append(nextBlock)

# append the genesis block ### _newBlock()
def addGenesisBlock():
    # genesis data set
    genesisPrevHash = hashlib.sha256(json.dumps(blockchain).encode()).hexdigest()
    genesisNonce = 0
    genesisData = "first block"
    # compute genesis block hash
    genesisBlockHash = getBlockHash(genesisPrevHash, genesisData, genesisNonce)
    # add genesis block to the blockchain
    addBlockToChain(genesisPrevHash, genesisData, genesisNonce, genesisBlockHash)

# go through the data set, compute the correct values of the next block and append to the blockchain
def processData():
  # process the data list
    for data in transactions:
      # get the index of the previous block (i.e. the last block in the chain)
      prevBlockIndex = len(blockchain) - 1
      # use the index to get the previous block
      prevBlock = blockchain[prevBlockIndex]
      # the previous hash of the new block is the previous block's hash
      prevBlockHash = prevBlock['blockHash']
      # calculate the correct nonce
      nonce = mine(prevBlockHash, data)
      # get the blockHash of the current block ()
      blockHash = getBlockHash(prevBlockHash, data, nonce)
      addBlockToChain(prevBlockHash, data, nonce, blockHash)

def execute():
  # if blockchain is empty
  if len(blockchain) == 0:
    addGenesisBlock()
  # process the transaction data
  processData()
  print(blockchain)
execute()
    
