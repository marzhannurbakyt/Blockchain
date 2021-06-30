# from web3 import Web3

# class DeployContract:
#     def __init__(self, private_key):
#         provider = 'https://ropsten.infura.io/v3/3ba8a4f2b1a340cd9c87a54441d9e9f7'
#         self.w3 = Web3(Web3.HTTPProvider(provider))
#         self.priv = private_key

#     def deploy(self):
#         instance = self.w3.eth.contract(abi=self.abi, bytecode=self.bin)
#         # hacky .. but it works :D
#         tx_data = instance.constructor().__dict__.get('data_in_transaction')
#         transaction = {
#             'from': self.pub, # Only 'from' address, don't insert 'to' address
#             'value': 0, # Add how many ethers you'll transfer during the deploy
#             'gas': 2000000, # Trying to make it dynamic ..
#             'gasPrice': self.w3.eth.gasPrice, # Get Gas Price
#             'nonce': self.w3.eth.getTransactionCount(self.pub), # Get Nonce
#             'data': tx_data # Here is the data sent through the network
#         }
#         # Sign the transaction using your private key
#         signed = self.w3.eth.account.signTransaction(transaction, self.priv)
#         #print(signed.rawTransaction)
#         tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)
#         print(tx_hash.hex())


from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/3ba8a4f2b1a340cd9c87a54441d9e9f7'))

public_address = '0xCEF162fA25f7399d573d78f848bAE07F48C5f40f'
rec_public_address = '0xCEF162fA25f7399d573d78f848bAE07F48C5f40f'
private_key = 'd9e93c0b7a2ffd81a623e756a551e24f150f1429f589cf1cc7ba25b585b559ee'

# setup addresses and get private key for address1
# address1 = Web3.toChecksumAddress(public_address)
# address2 = Web3.toChecksumAddress(rec_public_address)

nonce = w3.eth.getTransactionCount(public_address)

tx = {
  'nonce': nonce,
  'to': rec_public_address,
  'value': w3.toWei(0.001, 'ether'),
  'gas': 21000,
  'gasPrice': w3.toWei(40, 'gwei'),
}

signed_tx = w3.eth.account.signTransaction(tx, private_key)

# send the transaction 
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
# print(web3.toHex(tx_hash))