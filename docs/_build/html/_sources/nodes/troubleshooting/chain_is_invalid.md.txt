
Error: retrieved hash chain is invalid
======================================

## Sample

``` text
mar 24 12:51:12 DPET40U20QN QuadransNode[684]: WARN [03-24|12:51:12.970] Synchronisation failed, dropping peer peer=994519f3842f2b9b err="retrieved hash chain is invalid"
mar 24 12:52:22 DPET40U20QN QuadransNode[684]: WARN [03-24|12:52:22.499] Synchronisation failed, dropping peer peer=ff84fa216bff0a0d err="retrieved hash chain is invalid"
``` 

This error is usally due to a corrupted chaindata in your node. 

This might be due to:

* slow I/O storage
* hard reboot of your computer

To fix this you might need to:

* reset your chaindata
* reboot the node

Simply use this command on self-installed go-quadrans installation:

``` bash
sudo su quadrans -c "gqdc removedb" && sudo systemctl restart quadrans-node
```

Or remove the content of the `~/.quadrans/gqdc/chaindata/` folder.