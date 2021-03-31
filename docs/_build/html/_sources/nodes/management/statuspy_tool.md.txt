Status.py tool
==============

The status.py tool is a simple python script that connects to the node and gives some stats about the node. You should find this tool already installed and configured on your node. In that case just go to the folder, launch the tool and see the result

## Dependecies

``` bash
sudo apt install python3-pip python3-dev
sudo pip3 install wheel setuptools termcolor rlp web3 pyfiglet
``` 

## Code

Create a new **status.py** file with this content:

``` python
#!/usr/bin/python3
import sys
import json
from termcolor import colored
from web3.auto import Web3
from web3 import IPCProvider
from web3.middleware import geth_poa_middleware
from pyfiglet import Figlet
	
### CONFIG #####################################################################
	
ipcMiddleware = {
	"Mainnet":"/home/quadrans/.quadrans/gqdc.ipc", 
	"Testnet":"/home/quadrans/.quadrans/testnet/gqdc.ipc"
	}
custom_fig = Figlet(font='standard')
	
### MAIN #######################################################################
	
print(custom_fig.renderText('Quadrans Node'))
	
try:
	for net, ipc in ipcMiddleware.items() :
		web3 = Web3(IPCProvider(ipc))
		if web3.isConnected():
			print("Provider:\t\tIPC ("+net+": "+ipc+")" )
			break
	if not web3.isConnected():
			sys.exit()
except SystemExit:
	print("Could not connect to node via providers")
	sys.exit()
except:
	print("Critical error connectiong to node")
	sys.exit()
	
def show(status):
	
	print("Connected:\t\t", end='')
	if status["Connected"] == False:
		print(colored(" False  ", 'red', attrs=['reverse', 'blink']))
	else:
		print(colored("  OK !  ", 'green', attrs=['reverse']))
	
	print("Peer Connections:\t", end='')
	p = str(status["Peer Connections"]).center(8,' ')
	c = colored(p, 'green', attrs=['reverse'])
	if status["Peer Connections"] < 5:
		c = colored(p, 'yellow', attrs=['reverse', 'blink'])
	if status["Peer Connections"] < 2:
		c = colored(p, 'red', attrs=['reverse', 'blink'])
	print(c)
	
	print("Syncing:\t\t", end='')
	if status["Syncing"] == False:
		print(colored("  100%  ", 'green', attrs=['reverse']))
	else:
		local = status["Syncing"]["currentBlock"]
		limit = status["Syncing"]["highestBlock"]
		P = float( (local*100.00)/limit )
		S = "{0:2.2f}%".format(P).center(8,' ')
		if P < 50:
			print(colored(S, 'red', attrs=['reverse']))
		else:
			print(colored(S, 'yellow', attrs=['reverse']))
	
	print("Block Number:\t\t", end='')
	print(colored(status["Block Number"], attrs=['bold'] ))
	print("Software Version:\t", end='')
	print(status["Software Version"])
	print("Protocol Version:\t", end='')
	print(status["Protocol Version"])
	print("Chain ID:\t\t", end='')
	print(status["Chain ID"])
	print("Net Version:\t\t", end='')
	print(status["Net Version"])
	
def main():
	status = {}
	status["Connected"] = web3.isConnected()
	status["Syncing"]   = web3.eth.syncing
	status["Block Number"] = web3.eth.blockNumber
	status["Protocol Version"] = web3.eth.protocolVersion
	status["Chain ID"]   = web3.eth.chainId
	status["Net Version"]   = web3.net.version
	status["Software Version"]   = web3.geth.admin.node_info()["name"]
	status["Peer Connections"]   = len( web3.geth.admin.peers() )
	
	show(status)
	
### RUN ########################################################################
	
if sys.version_info[0] < 3:
	raise Exception("Python 3 or a more recent version is required.")
	
if __name__ == "__main__": 
	main()
```

## Please note:

This tool can be used by users root and quadrans (for the [Quadrans node self-installer](../installation/linux_x86-64) for Linux) due to permissions on the ipc socket

``` bash
cd /home/quadrans
./status.py
``` 

The expected result should look like:

``` 
Provider: IPC (TestNet: /home/quadrans/.quadrans/testnet/gqdc.ipc)
Connected: OK !
Peer Connections: 3
Syncing: 100%
Block Number: 1000936
Software Version: gqdc/v1.3.0-stable-1528b791/linux-amd64/go1.12
Protocol Version: 63
Chain ID: 10947
Net Version: 3
```

You can clearly see the main info about the status of your node, the  number of peers, the chain ID, the net version, the software version, the sync status and wether the node is running in testnet or mainnet