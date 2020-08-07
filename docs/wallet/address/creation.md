Create a Quadrans Address
=========================

There are many different ways of creating a new Quadrans Address. They might use different tools and result in different feature and ways to use them. As an example some methods allow you to get access to the private key, other protect the address/wallet with a password, other might use a mnemonic list of words. Choose the method you will use accordingly with your needs.

## Via gqdc commad line interface

Access the node via ssh. Be sure to use the quadrans user. Once in the
bash use the following command. Be sure to enter the same password
twice. `$ gqdc account new`
`Your new account is locked with a password. Please give a password. Do not forget this password.`
`Passphrase:` `Repeat Passphrase:`
`Address: {168bc315a2ee09042d83d7c5811b533680531f67}`

## Via Web3

Go to the node socket folder and attach the cli to that socket.

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
gqdc attach geth.ipc
``` 

once presented with the `>` prompt use the following command to create the new account

``` bash
personal.newAccount("passphrase")
``` 

Change *passphrase* with the password you will use later to unlock the wallet. Afther a few seconds the cli will output the new account address.

## Create and anddress manually starting from the private key

This a rather unorthodox method but might be useful in some cases. Please remember that the private key of an address is the most important piece of information and must be kept safe and secret at all time or you might lose your cryptoassets or the access to your deployed smart contracts.

### Steps

Create the **private key file** by generating 256 random bits in a file. You can pipe any data you want to the sha256sum function. Be sure to have excactly 64 bytes of data:

``` bash
date | sha256sum | head -c 64 > priv.key
``` 

Use the **import** account function on the private key. The command will ask for a **new** password to protect the json file that will be generated (it will not protect the private key file)

``` bash
gqdc account import priv.key
Your new account is locked with a password. Please give a password. Do not forget this password.
Passphrase: 
Repeat passphrase: 
Address: {<your-new-address-here>}
``` 

At the end of the procedure you\'ll find the new json file for the new address in the keystore directory. Be sure to backup the private key and/or the json file+password.

*Note: Remember to delete the private key file from the node.*

## See also

* [How to safely store a Quadrans Address](storage)
* [Checking Quadrans Addresses on your node](check)
