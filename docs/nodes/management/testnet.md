How to setup your node for Testnet 
==================================

The testnet node is the go-to tool for developers and testers. Installing a testnet node is pretty easy but there are a few pitfalls you must pay attention to.

## Get the right binary

The testnet receives uses the last test version of the `gqdc` node binary. This means that the version of the testnet node might not match the version of the main-net node. Please first check that the version you are running is the right one and update it if necessary.

The latest *Test* version of the binary is available from here: <http://repo.quadrans.io/linux/test/>

Starting from [Quadrans node self-installer](../installation/linux_x86-64) for Linux, you can manually edit the configuration to transform a Mainnet node in a Testnet node.

### Connect the self-installing node to the Testnet 

As *root* or *sudo* user stop the node

``` bash
systemctl stop quadrans-node
``` 

Substitute the `gqdc` binary with the latest test version for your architecture:

``` bash
wget -O /usr/local/bin/gqdc http://repo.quadrans.io/linux/test/amd64/gqdc
chmod +x /usr/local/bin/gqdc
``` 

Go to the *quadrans* home directory and change the configuration file:

``` bash
cd /home/quadrans
vim environment
``` 

Disable the *NODE\_LISTED* option i enabled:

``` bash
export NODE_LISTED=false
``` 

Save and edit the Quadrans Node launcher.

``` bash
vim gqdc.sh
``` 

Append the `--testnet` parameter in the last line of the file:

``` bash
eval "/usr/local/bin/gqdc --testnet ${MINER_OPTS} ${STATS_OPTS}"
``` 

Or like this to enable RPC connection and API:

``` bash
eval "/usr/local/bin/gqdc --testnet --rpc --rpcapi \"eth,net,web3,personal\" --rpccorsdomain \"*\" --rpcaddr \"IP_ADDRESS\" ${MINER_OPTS} ${STATS_OPTS}"
``` 

Save and restart the node.

``` bash
systemctl restart quadrans-node
``` 

### Manually launch the latest Test binary 

Download the latest test version of the *gqdc* binary, based on your arcitecture from here:

<http://repo.quadrans.io/linux/test/>

For example for x86-64 version substitute the current Quadrans node binary with the test version:

``` bash
wget -O /usr/local/bin/gqdc http://repo.quadrans.io/linux/test/amd64/gqdc
chmod +x /usr/local/bin/gqdc
``` 

Execute the node to connect to the testnet:

``` bash
/usr/local/bin/gqdc --testnet
``` 

Or like this to enable RPC connection and API:

``` bash
/usr/local/bin/gqdc --testnet --rpc --rpcapi "eth,net,web3,personal" --rpccorsdomain "*" --rpcaddr "IP_ADDRESS"
``` 

## Paths and folders

Once your node is configured for running in testnet, all working files are moved one level under the testnet folder

``` bash
cd /home/quadrans/.quadrans/testnet
``` 

In this folder you will find:

``` bash
ls -al
total 16
drwx------ 4 quadrans quadrans 4096 Oct 13 21:04 .
drwxr-xr-x 6 quadrans quadrans 4096 Aug 6 12:57 ..
srw------- 1 quadrans quadrans 0 Oct 13 21:04 gqdc.ipc
drwx------ 4 quadrans quadrans 4096 Oct 14 15:21 gqdc
drwx------ 2 quadrans quadrans 4096 Jul 26 14:11 keystore
```

Note that you'll find the gqdc.ipc socket for rpc commands, a keystore folder for available the json accounts and wallets, the gqdc folder with chaindata and nodes info.

## Check the node

You can check che node status [using the same commands used for the main-net node](node_status), of course there will be differences and small changes.

If you run into any issue please check the troubleshooting session before contacting support

## Bootnodes

You might want to run the following commands to speed-up the connections to other testnet nodes

``` 
admin.addPeer("enode://565fe0a0ef0690fe12a2db7e6bf7793e697670862e4ba0fe1c3ff6e067da39c1c8559572872fc85eb80cb16e9b3ddf61178e210eeb05f4e25439caadc3d539de\@40.74.72.56:57974");
admin.addPeer("enode://8f645fe27dee31f1551c737fc1b7ef9acf20cf0103d48f89b505de105b1ad16960220d52e9d69cb11e1a98cc576a56a2dda6724125fb69a3df29770e97235de2\@104.45.7.40:57772");
admin.addPeer("enode://e13221932a06ee3b5ef17dc09d34a73e57c68ae99e85a88ce0ef26b1909f0d0fecd884eececf4eda1978586b14b790c109c00729bdd26ab72547117db5ab29fb\@52.169.192.210:34452");
admin.addPeer("enode://3e05163a55bf163d652fe72545d4c23887cb2a4314665a9cebc9dd3b3d93f1e739439327d202abab559293a42a168c5400b87c56fa7371d8162f1eb25c6d7516\@52.167.132.30:28657");
admin.addPeer("enode://f3648d99ec98102638dcaa7bc53b512e04e79b5a6981fb9291c635f10c41a2a6ab5cccddbfe0689422d39c6b8cb7d7b2e1e4c4acf7182975a8cfb318a536e222\@40.68.62.19:54318");
admin.addPeer("enode://53a977003d47236a92da1170f3a19ea08a00d7590f6aa548b28fe22fb039cdb48a351709022980a4b0cc49f7cd931cfa4f83f628e90e5a27a09a04017efeaa2b\@35.184.244.152:49682");

net.peerCount eth.syncing
```

## Faucet

In order to run your smart contracts and make some transactions you need to have testnet coin. Get them for free at the following address. You need to have a working wallet and address to claim your coins. You can get up to 1 coin per day.

* **Quadrans Faucet page**: <https://faucetpage.quadrans.io>
* **Quadrans Faucet Telegram Bot**: <https://t.me/Quattrino_bot>