Install Quadrans on Raspberry Pi
================================

## What is Raspberry Pi

The [Raspberry Pi](https://www.raspberrypi.org) is a low cost, credit-card sized computer developed by [Raspberry Pi Foundation](https://www.raspberrypi.org). It can run Linux operating system. Recent models use [Broadcom](https://en.wikipedia.org/wiki/Broadcom_Inc.) SoC, and could have 1, 2 or 4 GB of RAM.


![img400](../../_static/images/nodes/raspberry-pi-3-board.jpg)

### Raspberry Pi 3/4

Quadrans Technical Team\*\* tested the [arm7 binary](http://repo.quadrans.io/arm/arm7/) (32bit) in combination with [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) operating system with the Raspberry devboards.

Models tested are:

* Raspberry Pi 4
* Raspberry Pi 3 Model B+


### Suggested Operating System

* [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) Buster (Ubuntu 18.04.3 LTS based) 
* [Installation guides](https://www.raspberrypi.org/documentation/installation/installing-images/) are available in the [official Raspberry website](https://www.raspberrypi.org)

## Manual installation for Linux (arm 7) 

This guide will recreate the same conditions as the go-quadrans binary automatically creates on Debian/Ubuntu for Linux x86-64. 

The basic steps are :

* Create a *quadrans* user with no password
* Download the binary
* Setup your configuration file (optional)
* Create the go-quadrans launcher (optional)
* Make the launcher a systemd service (optional)

### Software requirements

Before downloading the go-quadrans verify in `dialog`, `python3`, `systemd` are already installed in your Linux Machine. For clock sync (mandatory) you can use indifferently `ntp` or `systemd-timesyncd`.

### Create the quadrans user and download the latest binary

As *root* create a *quadrans* user with no password:

``` bash
useradd -r -m quadrans
``` 

#### ARM7 32 bit CPU
Download the latest binary:

``` bash
wget -O /usr/local/bin/gqdc http://repo.quadrans.io/arm/arm7/gqdc 
chmod +x /usr/local/bin/gqdc
``` 

### Useful command line options 

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

### Set up the Quadrans node launcher (optional)

To create a go-quadrans launcher firstly create and edit a configuration file called `environment`. 

Enviromnent variable like *NODE_LISTED* (options *true* or *false*) and *NODE_NAME* are required to be listed in the [Quadrans Status page](https://status.quadrans.io). *Your node information will be publicly available*. 

If your node will be a Miner or a Masternode *MINER_OPTIONS* (options *true* or *false*) and *MINER_WALLET* with the *MINER_PASSWORD* are required.

To create your configuration simpy edit and type the following code as **quadrans** user:

``` bash
cat > /home/quadrans/environment <<'EOF'
export NODE_LISTED=true
export NODE_NAME="Your node name"
export MINER_OPTIONS=false
export MINER_WALLET=0xYourQuadransWalletAddress
export MINER_PASSWORD=/path/to/wallet_password_file.txt
EOF
``` 

The next step is create a go-quadrans launcher:

``` bash
cat > /home/quadrans/gqdc.sh <<'EOF'
#!/bin/bash
source /home/quadrans/environment

MINER_OPTS=""
STATS_OPTS=""

if [ "${MINER_OPTIONS}" = "true" ]; then
    MINER_OPTS="--mine --unlock ${MINER_WALLET} --password ${MINER_PASSWORD}"
fi

if [ $(grep -c "NODE_LISTED=true" /home/quadrans/environment ) -eq 1 ]; then
    STATS_OPTS=$(printf "%sethstats \"%s\":\"QuadransStatsNetwork\"@status.quadrans.io:3000" "--" "${NODE_NAME}")
fi

eval "/usr/local/bin/gqdc ${GETH_PARAMS} ${MINER_OPTS} ${STATS_OPTS}"
EOF
``` 

Make the `gqdc.sh` launcher executable:

``` bash
chmod +x /home/quadrans/gqdc.sh
``` 

Run.

### Set up the Quadrans node as systemd service (optional)

To make your node a systemd service and type the following code as **root**:

``` bash
cat > /etc/systemd/system/quadrans-node.service <<'EOF'
Description=Quadrans Node Service
After=network.target

[Service]
Type=simple
User=quadrans
WorkingDirectory=/home/quadrans
EnvironmentFile=/home/quadrans/environment
ExecStart=/home/quadrans/gqdc.sh
Restart=on-failure
RestartSec=60
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=QuadransNode

[Install]
WantedBy=default.target
EOF
``` 

#### Enable and start the service

To launch the service for the first time and start automatically on boot:

``` bash
systemctl start quadrans-node
systemctl enable quadrans-node
``` 

To check your node status:

``` bash
systemctl status quadrans-node
``` 

or

``` bash
journalctl -f | grep Quadrans
``` 

### Enable your node for mining

Go to [Mining and Reward](../../cryptocurrencies/mining_and_reward) chapter of this Wiki.

### Create a Quadrans Node updater script (optional)

**Quadrans Node Update Installer** for [ARM7](../management/gqdc-update.html#script-for-arm7-devices) is bash script that check Internet connection, suspend the Quadrans Node Service, download the new version of the **gqdc** binary and relaunch the service at the end of the process.

## Connect the node to Testnet 

Please read the **How to setup your node for testnet** documentation.

### Important

You can move from **Testnet** to **Mainnet** at any time but **you can\'t connect to the two networks at the same time**.