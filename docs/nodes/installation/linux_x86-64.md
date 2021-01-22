Install Quadrans on Linux x86-64
================================

## Hardware requirements

Minimum system requirements:

* Computer Desktop, Server or Virtual Machine
* 1 Core 64bit CPU
* 2 GB RAM
* 50 GB storage

Suggested requirements:

* Computer Desktop, Server or Virtual Machine
* 2 Core 64bit CPU
* 4 GB RAM
* 100 GB storage

## Self-installing from Quadrans repository on Debian/Ubuntu 

Quadrans team recommends to use a supported **Ubuntu LTS** (18.04 or 20.04) or an updated **Debian** installation. 

``` bash
sudo wget -O /etc/apt/sources.list.d/quadrans.list http://repo.quadrans.io/apt/conf/quadrans.list
sudo wget -O - http://repo.quadrans.io/apt/conf/quadrans.gpg.key|sudo apt-key add -
sudo apt update
sudo apt install -y python quadrans-node
``` 

Follow the on screen instructions to install the node, enable miner options and create a Quadrans wallet address.

## Self-installing via Quadrans Installer

This bash script allows you to install or update your node for other Linux distributions.

``` bash
wget http://repo.quadrans.io/linux/experiments/installer/gqdc-installer.sh
sudo bash gqdc-installer.sh
``` 

The installation process will ask for a node name and a password if you want to create a wallet to became a Quadrans Miner.

This tool allow you to update your node if needed.

## Enable your node for mining

Go to [Mining and Reward](../../cryptocurrencies/mining_and_reward) chapter of this Wiki.

## Useful options 

After downloading, run `gqdc` to connect your node to the Quadrans Network. Make sure to check the different options and commands with `gqdc --help`

To set your data directory:

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

## Connect the node to Testnet 

Please read the [How to setup your node for testnet](../management/testnet) documentation.

### Important

You can move from **Testnet** to **Mainnet** at any time but **you can\'t connect to the two networks at the same time**.