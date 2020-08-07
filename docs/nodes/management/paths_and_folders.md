Node paths and folders
======================

``` 
	--- Folder / Path ---                          |    --- Use ---
-------------------------------------------------|-------------------------------------------------------------------------
/home/quadrans/                                  |  Home folder of the node
├── environment                                  |  configuration file of the node
├── gk                                           |  tool for private key extraction (needs wallet file and it's password)
├── gqdc.sh                                      |  start script (uses the environment file)
├── status.py                                    |  status python script
└── .quadrans                                    |  
	├── geth.ipc                                 |  IPC socket for main net
	├── gqdc                                     |  
	│   ├── LOCK                                 |  
	│   ├── chaindata                            |  
	│   │   ├── 002970.log                       |  
	│   │   ├── CURRENT                          |  
	│   │   ├── CURRENT.bak                      |  
	│   │   ├── LOCK                             |  
	│   │   ├── LOG                              |  
	│   │   └── MANIFEST-002623                  |  
	│   ├── nodekey                              |  main net peer nodes info
	│   ├── nodes                                |  
	│   │   ├── 000998.log                       |  
	│   │   ├── CURRENT                          |  
	│   │   ├── CURRENT.bak                      |  
	│   │   ├── LOCK                             |  
	│   │   ├── LOG                              |  
	│   │   └── MANIFEST-000183                  |  
	│   └── transactions.rlp                     |  
	├── history                                  |  
	├── keystore                                 |  main net wallet folder
	│   └── UTC--2019-09-27T20-01-52...          |      main net wallet
	└── testnet                                  |  testnet folder (not present if running on main net)
		├── geth.ipc                             |  IPC socket for test net 
		├── gqdc                                 |  
		│   ├── LOCK                             |  lock file
		│   ├── chaindata                        |  local blockchain copy
		│   │   ├── 000336.log                   |  
		│   │   ├── CURRENT                      |  
		│   │   ├── LOCK                         |  
		│   │   ├── LOG                          |  
		│   │   └── MANIFEST-000000              |  
		│   ├── nodekey                          |  test net peer-nodes info
		│   ├── nodes                            |  
		│   │   ├── 006812.log                   |  
		│   │   ├── CURRENT                      |  
		│   │   ├── LOCK                         |  
		│   │   ├── LOG                          |  
		│   │   ├── LOG.old                      |  
		│   │   └── MANIFEST-000000              |  
		│   └── transactions.rlp                 |  
		├── history                              |  
		└── keystore                             |  folder for testnet wallets:
			├── UTC--2019-06-11T11-20-23...      |      tesnet wallet 
			├── UTC--2019-07-30T14-56-50...      |      tesnet wallet
			└── UTC--2019-07-30T15-52-24...      |      tesnet wallet
``` 