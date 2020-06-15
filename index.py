'''
Sala Coin --> Just for fun
timestamp --> When a block was created
index --> Where the block sits on the chain.. 
data --> any type of data to  associate with the block.. 
previous_hash --> Hash of the previous block, ensures integrity..
'''
import hashlib
import datetime as date
class Block:
    def __init__(self,index,timestamp,data,previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        hasher = hashlib.sha256()
        hasher.update(
            (
                str(self.index)
                +str(self.timestamp)
                +str(self.data)
                +str(self.previous_hash)
            ).encode('utf-8')
        )
        
        return hasher.hexdigest()
  
def create_genesis_block():
    return Block(0,date.datetime.now(),'Genesis Block','0')  

def add_block(last_block):
    block_index = last_block.index + 1
    block_timestamp = date.datetime.now()
    block_data = 'This is block number ' + str(block_index)
    block_hash = last_block.hash
    
    return Block(block_index,block_timestamp,block_data,block_hash)
 
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# No of blocks to add after genesis block... 25
total_blocks_to_add = 25

for i in range(0,total_blocks_to_add):
    block_to_add = add_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    
    print(f'Block #{block_to_add.index} has been added to the blockchain')
    print(f'Hash: {block_to_add.hash}')