from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/3ba8a4f2b1a340cd9c87a54441d9e9f7'))
print ("Latest Ethereum block number" , w3.eth.blockNumber)