How to safely Backup a Quadrans Address 
=======================================

Depending on the way you created your address there are different things you can do and best practices to follow to backup an adderss/wallet.

If the address is in use on a node, you will for sure have the json file of the address and can follow the directions here

## Keystore Json account and password files

Each node stores data of the addresses it can work with in the keystore directory. The directory tree used in this guide is based on a self-installing Quadrans Linux node.

The unlock `password.txt` file is tipically stored on *quadrans* user home folder

``` bash
cd /home/quadrans/
``` 

The wallet private key for Mainnet nodes is available in:

``` bash
cd /home/quadrans/.quadrans/keystore
``` 

The wallet private key for Testnet nodes is available in:

``` bash
cd /home/quadrans/.quadrans/testnet/keystore
``` 

In those directories there is one json file for each address whose name is in the form:

``` bash
UTC--YYYY-MM-DDTHH-mm-ss.sssssssssZ--<address>
``` 

Ex:

``` bash
UTC--2017-04-28T08-46-52.180688336Z--9acb9ff906641a434803efb474c96a83775628f7
``` 

is the file name of address `9acb9ff906641a434803efb474c96a83775628f7` created april 28th 2017 a few milliseconds afther 8:46 and 52 seconds

It contents might look something like: 

``` json
{
"address": "9acb9ff906641a434803efb474c96a83775628f7",
	"crypto": {
		"cipher": "aes-128-ctr",
		"ciphertext": "033ee73205182e91d28a3660e17cb690de7c5f0f2599416b927314b16a9938fd",
		"cipherparams": {
			"iv": "f59792e7b06b4c657925f1b362780065"
		},
		"kdf": "scrypt",
		"kdfparams": {
			"dklen": 32,
			"n": 262144,
			"p": 1,
			"r": 8,
			"salt": "6f3cb9aec0be5ff173a340d4d5e3c50dac943668f1f1e787bbc7321d5edc38ba"
		},
		"mac": "a4a95d2a7e4664469bbd1ebb89f563399a5d760f9b5e6585a06d93433bd75cea"
	},
	"id": "bbdeacb2-168e-4e73-8659-d1880ee4fb4c",
	"version": 3
}
``` 

Those files are **encrypted format** and can safely be copied from one node to another. You need to use the corresponding **password** in order to unlock and use it

## What to store

In order to operate and/or migrate the account form one node to another you need to have:

* the Json file
* the corresponding password (*password.txt* for Quadrans nodes)

Save those two, back them up and store them in a safe place
