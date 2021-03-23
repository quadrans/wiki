Install Quadrans on macOS (darwin)
==================================

## Hardware requirements

Minimum system requirements:

* Apple Mac, Server or Virtual Machine
* 2 Core 64bit CPU
* 4 GB RAM
* 50 GB storage

Suggested requirements:

* Apple Mac, Server or Virtual Machine
* 2 Core 64bit CPU
* 4 GB RAM
* 100 GB storage

## Self-installing via Quadrans Installer

This bash script allows you to install or update your node on various Linux distributions.

``` bash
curl -s http://repo.quadrans.io/installer/gqdc-installer.sh > gqdc-installer.sh
sudo bash gqdc-installer.sh
``` 

The installation process will ask for a node name and a password if you want to create a wallet to became a Quadrans Miner.

This tool allow you to update your node if needed.

## Enable your node for mining

Go to [Mining and Reward](../../cryptocurrencies/mining_and_reward) chapter of this Wiki.

## Manual installation for macOS (Intel 64bit)

From macOS Terminal application type:

``` bash
cd /your_destination_folder/
curl http://repo.quadrans.io/macos/intel64/gqdc -o gqdc
chmod +x gqdc
```

After downloading, run *gqdc* to connect your node to the Quadrans Network.

Make sure to check the different options and commands with ``gqdc --help``

### Useful options

To change your data directory.

``` bash
gqdc -datadir datadir_path
``` 

To show your node in the Quadrans Network Status page:

``` bash
gqdc --ethstats "Your Node Name":QuadransStatsNetwork@status.quadrans.io:3000
``` 

To create a new Quadrans wallet create a password inside a text file and execute the following command:

``` bash
gqdc account new --password Your_Password_File.txt
``` 

To execute the node as a *Miner*:

``` bash
gqdc --mine --unlock 0xYour_Wallet_Address --password Your_Password_File.txt
``` 

To connect to Quadrans Testnet (download the [last test Quadrans node binary](../management/testnet)).

``` bash
--testnet
``` 

### Enable your node for mining

Go to [Mining and Reward](../../cryptocurrencies/mining_and_reward) chapter of this Wiki.
