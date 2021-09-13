Importing a json wallet file to your node
=========================================

## Import json file
* Copy the UTC json file to the destination keystore folder (/home/quadrans/.quadrans/keystore)
* Restart the node

``` bash
cp UTC* /home/quadrans/.quadrans/keystore
systemctl restart quadrans-node.service
```

## Verify wallet import

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

``` js
eth.accounts
```