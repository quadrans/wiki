Update your manually configured Linux Quadrans node
===================================================

## What is the Quadrans Node Update installer

This simple script allows to update manually configured Linux machines with a **Quadrans Node**.

Copy and paste the code in your Linux console as *root* user.

## Create the gqdc-update.sh for your architecture

Create a `gqdc-update.sh` script to update your Quadrans node based on your CPU and Linux installation.

### Script for x86-64 devices

``` bash
cat > /usr/local/bin/gqdc-update.sh <<'EOF'
#!/bin/bash
# Test your internet connection
printf "\e[1mNetwork test...\n\e[0m"
wget -q --spider http://google.com
if [ $? -eq 0 ]; then
    printf "\e[32m...it works! \n\n\e[0m"
    figlet Quadrans Node
    printf "Update in progress...\n\n"
    # Close the Quadrans Node Service
    systemctl stop quadrans-node
    # Download the new binary and make it executable
    wget http://repo.quadrans.io/linux/amd64/gqdc -O /usr/local/bin/gqdc
    chmod +x /usr/local/bin/gqdc
    # Start the Quadrans Node Service
    systemctl start quadrans-node
    printf "Quadrans Node update completed.\n\n"
else
    printf "\e[31moffline.\e[0m\n\nQuadrans Node update skipped this time.\n"
fi
EOF
``` 

### Script for ARM64 devices

``` bash
cat > /usr/local/bin/gqdc-update.sh <<'EOF'
#!/bin/bash
# Test your internet connection
printf "\e[1mNetwork test...\n\e[0m"
wget -q --spider http://google.com
if [ $? -eq 0 ]; then
    printf "\e[32m...it works! \n\n\e[0m"
    figlet Quadrans Node
    printf "Update in progress...\n\n"
    # Close the Quadrans Node Service
    systemctl stop quadrans-node
    # Download the new binary and make it executable
    wget http://repo.quadrans.io/arm/arm64/gqdc -O /usr/local/bin/gqdc
    chmod +x /usr/local/bin/gqdc
    # Start the Quadrans Node Service
    systemctl start quadrans-node
    printf "Quadrans Node update completed.\n\n"
else
    printf "\e[31moffline.\e[0m\n\nQuadrans Node update skipped this time.\n"
fi
EOF
``` 

### Script for ARM7 devices

``` bash
cat > /usr/local/bin/gqdc-update.sh <<'EOF'
#!/bin/bash
# Test your internet connection
printf "\e[1mNetwork test...\n\e[0m"
wget -q --spider http://google.com
if [ $? -eq 0 ]; then
    printf "\e[32m...it works! \n\n\e[0m"
    figlet Quadrans Node
    printf "Update in progress...\n\n"
    # Close the Quadrans Node Service
    systemctl stop quadrans-node
    # Download the new binary and make it executable
    wget http://repo.quadrans.io/arm/arm7/gqdc -O /usr/local/bin/gqdc
    chmod +x /usr/local/bin/gqdc
    # Start the Quadrans Node Service
    systemctl start quadrans-node
    printf "Quadrans Node update completed.\n\n"
else
    printf "\e[31moffline.\e[0m\n\nQuadrans Node update skipped this time.\n"
fi
EOF
``` 

## Make the updater executable

Make the *gqdc-update.sh* executable.

``` bash
chmod +x /usr/local/bin/gqdc-update.sh
``` 

## Update your Quadrans Node

Run the updater.

``` bash
sudo gqdc-update.sh
```