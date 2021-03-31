Checking Quadrans Addresses on your node
========================================

There are several ways to check and list the address present in a node. All the following methods listed are equivalent and should bring you to the same results. You can choose the method that you prefer and/or use other methods to cross-check the results.

## Directory inspection

All addresses/wallets created on the node are stored in the *keystore* folder in those directories

For mainnet nodes:

	cd /home/quadrans/.quadrans/keystore

For testnet nodes:

	cd /home/quadrans/.quadrans/testnet/keystore

Access the corresponding directory in your node and inspect it\'s contents. You should see a list of json files in a the following format, one for each address

 UTC--YYYY-MM-DDTHH-mm-ss.sssssssssZ--<address>

## Via gqdc command line interface

Connect to the node via ssh and be sure to use the *quadrans* user.

Issue the command `gqdc account list`.

``` bash
gqdc account list
Account #0: {5afdd78bdacb56ab1dad28741ea2a0e87fe41331} keystore:///tmp/mykeystore/UTC--2017-04-28T08-46-27.437847599Z--5afdd78bdacb56ab1dad28741ea2a0e87fe41331
Account #1: {9acb9ff906641a434803efb474c96a83775628f7} keystore:///tmp/mykeystore/UTC--2017-04-28T08-46-52.180688336Z--9acb9ff906641a434803efb474c96a83775628f7
```


## Via Web3

Go to the node socket folder and attach the cli to that socket

For mainnet nodes:

``` bash
cd /home/quadrans/.quadrans
``` 

For testnet nodes:

``` bash
cd /home/quadrans/.quadrans/testnet
```

Common:

``` bash
gqdc attach gqdc.ipc
```

once presented with the `>` prompt use the following command to list your accoutns `personal.listAccounts`

``` js
["0x3ce6d53998e0b45b46d62c5e3a08025156544ef9", "0xaacbe83d9054f14e18cbf2cd0e11ba16ec759760"]
```
