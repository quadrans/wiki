Checking the status of your Quadrans node 
=========================================

There are multiple ways and steps that you can take to check the status
of your quadrans node

## Check with status.py tool 

Go to the node home folder and [use for the status.py script](statuspy_tool)

## Check with systemctl

Use the systemctl utility to check if the service is up and running

``` bash
systemctl status quadrans-node
``` 

You shold either see an error message or an output similar to the one
below:

``` text
	● quadrans-node.service - Quadrans Node Service
	Loaded: loaded (/etc/systemd/system/quadrans-node.service; enabled; vendor preset: enabled)
	Active: active (running) since Sun 2019-10-13 21:04:36 CEST; 18h ago
Main PID: 1000 (gqdc.sh)
	Tasks: 33 (limit: 4915)
	CGroup: /system.slice/quadrans-node.service
			├─1000 /bin/bash /home/quadrans/gqdc.sh
			└─1007 /usr/local/bin/gqdc --cache 1024 --maxpeers 25 --ws --wsaddr localhost --wsport 8546 
Oct 14 15:26:03 Venice2 QuadransNode[1000]: INFO [10-14|15:26:03.353] Imported new chain segment               blocks=1    txs=0    mgas=0.000    elapsed=365.042µs mgasps=0.000   number=1000772 hash=25e8ed…9ab1b6 dirty=27.17MiB
Oct 14 15:26:18 Venice2 QuadransNode[1000]: INFO [10-14|15:26:18.048] Imported new chain segment               blocks=1    txs=0    mgas=0.000    elapsed=444.135µs mgasps=0.000   number=1000773 hash=e3a8f6…309e5b dirty=27.17MiB
Oct 14 15:26:32 Venice2 QuadransNode[1000]: INFO [10-14|15:26:32.632] Imported new chain segment               blocks=1    txs=0    mgas=0.000    elapsed=415.308µs mgasps=0.000   number=1000774 hash=d7cbf2…d80c57 dirty=27.17MiB
Oct 14 15:26:48 Venice2 QuadransNode[1000]: INFO [10-14|15:26:48.876] Imported new chain segment               blocks=1    txs=0    mgas=0.000    elapsed=401.431µs mgasps=0.000   number=1000775 hash=54add2…9a65ad dirty=27.17MiB
``` 

## Check with journalctl 

Use the journalctl utility to follow the service in real time
`journalctl -f | grep Quadrans`

If the Quadrans Node service is up and running you will see an output
similat to the one below:

``` text
Oct 17 10:31:54 orangepierlite2d QuadransNode[734]: INFO [10-17|10:31:54.242] Imported new chain segment blocks=1 txs=0 mgas=0.000 elapsed=1.902ms mgasps=0.000 number=3970750 hash=7bd3e3…07ce7c dirty=173.24KiB
Oct 17 10:31:59 orangepierlite2d QuadransNode[734]: INFO [10-17|10:31:59.719] Imported new chain segment blocks=1 txs=0 mgas=0.000 elapsed=1.935ms mgasps=0.000 number=3970751 hash=d58e65…5fff71 dirty=173.24KiB
Oct 17 10:32:04 orangepierlite2d QuadransNode[734]: INFO [10-17|10:32:04.133] Imported new chain segment blocks=1 txs=0 mgas=0.000 elapsed=1.836ms mgasps=0.000 number=3970752 hash=957ef7…4dc32e dirty=173.24KiB
Oct 17 10:32:04 orangepierlite2d QuadransNode[734]: INFO [10-17|10:32:04.697] Imported new chain segment blocks=1 txs=0 mgas=0.000 elapsed=1.091ms mgasps=0.000 number=3970752 hash=8e51ab…31d643 dirty=173.24KiB
``` 

## Check network connections 

Use netstat to see if the node process is running and has connections to
other nodes

``` bash
testnet netstat -tnap | grep gqdc
``` 

A running node will show multiple connections to other peer nodes:

``` text
tcp 0 0 127.0.0.1:8545 0.0.0.0:* LISTEN 1007/gqdc
tcp 0 0 127.0.0.1:8546 0.0.0.0:* LISTEN 1007/gqdc
tcp 0 0 192.168.231.124:37972 40.74.72.56:28657 ESTABLISHED 1007/gqdc
tcp 0 1 192.168.231.124:39740 113.45.207.126:30303 SYN_SENT 1007/gqdc
tcp 0 0 192.168.231.124:58556 52.167.132.30:28657 ESTABLISHED 1007/gqdc
tcp 0 320 192.168.231.124:42580 140.82.48.9:30666 ESTABLISHED 1007/gqdc
tcp 0 1 192.168.231.124:34504 39.154.132.226:20182 SYN_SENT 1007/gqdc
tcp 0 0 192.168.231.124:47928 104.45.7.40:28657 ESTABLISHED 1007/gqdc
tcp 0 1 192.168.231.124:38892 165.227.91.25:50000 SYN_SENT 1007/gqdc
tcp 0 1 192.168.231.124:38924 13.239.121.57:30303 SYN_SENT 1007/gqdc
tcp6 0 0 :::28657 :::* LISTEN 1007/gqdc
``` 

## Connect to the node socket 

Get to the application folder, find the gqdc socket and use it to connect

Mainnet default application folder

``` bash
cd /home/quadrans/.quadrans
``` 

Testnet  default application folder

``` bash
cd /home/quadrans/.quadrans/testnet
``` 

Run:

``` bash
gqdc attach gqdc.ipc
``` 

This is what you will see inside the JavaScript console:

``` console
Welcome to the Gqdc JavaScript console!

instance: gqdc/v1.3.0-stable-1528b791/linux-amd64/go1.12 coinbase: 0x8598b3e931aacb7c1c708427702fa419b0762d57 at block: 1000805 (Mon, 14 Oct 2019 15:34:17 CEST)

datadir: /home/quadrans/.quadrans/testnet
modules: admin:1.0 clique:1.0 debug:1.0 eth:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0
``` 

## Get the node status via CLI 

Once you connected to the node via RPC socket like shown in the previous step, you can run the following commands to get the status of the node

``` console
admin.nodeInfo # gives info about this node
admin.peers    # gives a list of the connected peers (other nodes)
eth.syncing    # if true, node is catching up with the mined blocks
``` 