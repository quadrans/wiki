#!/usr/bin/python3
import sys
import json
from termcolor import colored
from web3.auto import Web3
from web3 import IPCProvider
from web3.middleware import geth_poa_middleware
from pyfiglet import Figlet
 
 
 
### CONFIG #####################################################################
 
ipcMiddleware = {"MainNet":"/home/quadrans/.quadrans/geth.ipc", "TestNet":"/home/quadrans/.quadrans/testnet/geth.ipc"}
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