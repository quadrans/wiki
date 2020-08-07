How to open RPC/WS to external connections
==========================================

In order to accept incoming connections from the network you need to configure the node accordingly. This can be done editing the  `/home/quadrans/environment`  file.

The default for the node is to listen to localhost only, using port 8456 for web-socket and 8545 for rpc.

Once edited, save the file and restart your node. Use netstat to check the changes.

## For web-socket

The first parameter enables web-socket, the second sets the IP address to listen to, the third is the port

``` bash
--ws --wsaddr "0.0.0.0" --wsport "8546"
``` 

## For RPC

The first parameter enables rpc, the second sets the IP address to listen to, the third is the port

``` bash
--rpc --rpcaddr "0.0.0.0" --rpcport "8545"
``` 

