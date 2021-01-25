Install Quadrans on Raspberry Pi
================================

## What is Raspberry Pi

The [Raspberry Pi](https://www.raspberrypi.org) is a low cost, credit-card sized computer developed by [Raspberry Pi Foundation](https://www.raspberrypi.org). It can run Linux operating system. Recent models use [Broadcom](https://en.wikipedia.org/wiki/Broadcom_Inc.) SoC, and could have 1, 2 or 4 GB of RAM.


![img400](../../_static/images/nodes/raspberry-pi-3-board.jpg)

### Raspberry Pi 3/4

**Quadrans Technical Team** tested the [arm7 binary](http://repo.quadrans.io/arm/arm7/) (32bit) in combination with [Raspberry OS](https://www.raspberrypi.org/software/) operating system with the Raspberry devboards.

Models tested are:

* Raspberry Pi 4
* Raspberry Pi 3 Model B+


### Suggested Operating System
* [Raspberry OS](https://www.raspberrypi.org/software/) (32 bit)
  * Installation guides are available in the [official Raspberry website](https://www.raspberrypi.org)
* [Ubuntu](https://ubuntu.com/download/raspberry-pi) (64 bit)

## Self-installing via Quadrans Installer

This bash script allows you to install or update your node on various Linux distributions.

``` bash
wget http://repo.quadrans.io/linux/experiments/installer/gqdc-installer.sh
sudo bash gqdc-installer.sh
``` 

The installation process will ask for a node name and a password if you want to create a wallet to became a Quadrans Miner.

This tool allow you to update your node if needed.

## Enable your node for mining

Go to [Mining and Reward](../../cryptocurrencies/mining_and_reward) chapter of this Wiki.

## Useful command line options 

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