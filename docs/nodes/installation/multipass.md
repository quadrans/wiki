Install Quadrans with Multipass
===============================

## What is Multipass

Multipass is a mini-cloud on your workstation using native hypervisors of all the supported plaforms (Windows, macOS and Linux), it will give you an Ubuntu command line in just a few minutes and allows you to create a secure and fully working Quadrans node in your computer.

With Multipass you will create a virtual server with basic environment and you can install the latest Quadrans node for Ubuntu Linux without without having to perform complicated steps.

## How-to start

Multipass provides a command line interface to launch, manage and generally fiddle about with instances of Linux. First of wall you need to simply prepare your computer to create an environment.

### Download and install Multipass on Windows 10

To get Multipass for Windows, download the latest installer from the  [official GitHub releases page](https://github.com/CanonicalLtd/multipass/releases/). It is the *.exe* file.

#### Prerequisites

Multipass will work without additional requirements on **Windows 10 Pro** or **Windows Enterprise**, version 1803 (“April 2018 Update”) or later that integrate the **Hyper-V** virtualization provider (or *hypervisor*).

For **Windows 10 Home** user (or if you want to change the virtualization provider) you need to download and install **Oracle VirtualBox** from the [official website](https://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html).

#### Installation

Run the installer and it will guide you through the steps necessary. 

* You will need to allow the installer to gain Administrator privileges;
* Select your preferred hypervisor (*Hyper-V* is the default or Windows 10 Pro/Enterprise, or *VirtualBox* is mandatory for Windows 10 Home);
* Select *Add multipass to the system PATH for all users*;
* Confirm the installation folder;
* Click on *Install* and reboot at the end of the process.

### Download and install Multipass on Mac OS

*Work in progress*

### Download and install Multipass on Linux

Multipass for Linux is published as a **snap** package. Before to start verify if your [Linux distribution supports snap](https://docs.snapcraft.io/installing-snapd) or [how to get ready for snap](https://docs.snapcraft.io/installing-snapd).

After that, to install multipass simply type this command in your Terminal.

```bash
snap install multipass
```

## Create the Quadrans virtual machine

**Quadrans node** minimum requirements are tipically a computer or VPS with 2 core CPU, 4 GB of RAM and 100 GB of hard disk. In Multipass configuration you can easily reduce to 2 GB of RAM your virtual machine.

To create a new Multipass instance you can use the following command inside the Windows *Command Prompt* or *PowerShell*, and Mac OS or Linux *Terminal*: 

``` bash
multipass launch -c 2 -m 2G -d 100G --name quadrans
```

This will automatically create a new virtual machine with the latest version of **Ubuntu LTS** with minimal setup. 

For your information *-c 2* means the number of logical core allocated from your CPU, *-m 2* to allocate 2 GB of RAM, *-d 100G* to create a virtual drive of 100 GB for data, *--name quadrans* is the name of your VM. You can customize and increase the allocation of resources for your virtual machine based on the power of your computer and the available amount of logical core, RAM or disk space. 

## Connect and install the Quadrans node

Once your virtual machine were created you can *execute* commands or *connect* to your enviroment. For the first run and the installation of your node use this command.

``` bash
multipass shell quadrans
```

You will be connected to your virtual machine. From here you can simply copy and paste the commands to use the self-installer for Ubuntu Linux.

``` bash
sudo wget -O /etc/apt/sources.list.d/quadrans.list http://repo.quadrans.io/apt/conf/quadrans.list
sudo wget -O - http://repo.quadrans.io/apt/conf/quadrans.gpg.key|sudo apt-key add -
sudo apt update
sudo apt install -y python quadrans-node
```

The installer will guide you through the steps necessary.

At the end of the process your node will start to sync and you can type ``exit`` to disconnect from the virtual machine.

## Useful informations

Your Multipass virtual machine will be automatically launched on boot as a service, you don't need to log-in on your operating system to start the **Quadrans node**.

You can stop the virtual machine (and it will not restart automatically on boot) with this command:

``` bash
multipass stop quadrans
```

To start the virtual machine the command is similar:

``` bash
multipass start quadrans
```

You can obtain information about the status and your virtual machine (CPU load, disk usage, memory usage, etc.) with this command:

``` bash
multipass info quadrans
```

You can execute a command outside the virtual machine, for example to check the status of your node:

``` bash
multipass exec quadrans -- systemctl status quadrans-node
```

To update your virtual machine:

``` bash
multipass exec quadrans -- sudo apt update
multipass exec quadrans -- sudo apt upgrade -y
```

To connect to your virtual machine and use the Linux console:

``` bash
multipass shell quadrans
```

To disconnect:

``` bash
exit
```

On Windows machine Multipass will install a simple to use systray icon. By clicking with the right button of you mouse you will find the "quadrans" virtual machine and you can *start*, *stop* or connect (*shell*) directly from this menu.