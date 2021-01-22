Install Quadrans on Orange Pi
=============================

## What is Orange Pi

The [Orange Pi](https://www.orangepi.org/) is an open-source single-board computer developed by [Shenzhen Xunlong Software CO.](https://www.orangepi.org/). It can run Android 4.4 or Linux. Recent models use the [Rockchip](https://en.wikipedia.org/wiki/Rockchip) RK3399, [AllWinner Technology](https://en.wikipedia.org/wiki/Allwinner_Technology) H6 SoC, and could have 1, 2 or 4 GB of RAM.

![img400](../../_static/images/nodes/orange-pi-3-h6-2gb-board.jpg)

### Orange Pi with Rockchip RK3399

**Quadrans Technical Team** tested the [arm64 binary (64 bit)](http://repo.quadrans.io/arm/arm64/) in combination with [official Ubuntu Image](http://www.orangepi.org/downloadresources/) operating system with these devboards:

* Orange Pi 4

### Orange Pi with AllWinner H6 SoC

**Quadrans Technical Team** tested the [arm64 binary (64 bit)](http://repo.quadrans.io/arm/arm64/) in combination with [Armbian for Orange Pi](https://www.armbian.com/download/?tx_maker=xunlong) operating system with the AllWinner H6 devboards.

Models tested are:

* Orange Pi 3
* Orange Pi One Plus
* Orange Pi Lite 2

### Orange Pi with other SoC

**Quadrans Technical Team** tested the [arm7 binary (32 bit)](http://repo.quadrans.io/arm/arm7/) in combination with [Armbian for Orange Pi](https://www.armbian.com/download/?tx_maker=xunlong) operating system with these devboards:

* Orange Pi Zero Plus

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