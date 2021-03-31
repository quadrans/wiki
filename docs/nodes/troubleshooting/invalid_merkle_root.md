
Error: invalid merkle root
===========================

## Sample

``` text
Feb 13 10:41:21 wallettest QuadransNode[6538]: Chain config: {ChainID: 10947 Homestead: 0 DAO:  <nil> DAOSupport: true EIP150: 0 EIP155: 0 EIP158: 0 Byzantium: 0 Constantinople: 0 ConstantinopleFix: 0 Engine: clique}
Feb 13 10:41:21 wallettest QuadransNode[6538]: Number: 1699802
Feb 13 10:41:21 wallettest QuadransNode[6538]: Hash: 0x062e18fbc28c5cf9a118fc264973e8ce540a8a8570666eaedc35e539c19b1257
Feb 13 10:41:21 wallettest QuadransNode[6538]: Error: invalid merkle root (remote: c0814de04f941ec8a527cb67d8b4a2a3a02a5f074667d28a3a36862eac255459 local: fa080412b6f4e30e368589324d35df655481844eb0125fa262eba56a33c11d1b)
``` 


This error is usally due to an incompatibility between the binary you are dunning and che blockchain you are connected to. 

This might be due to:

* test-net binary not meant to run on main-net
* main-net only binary not meant to be run on test-net
* test node not made it to release (lab only)
* binary no longer supported

To fix this you might need to:

* figure out the blockchain net you want to run (main/test)
* pick the last version of the binary compatible with said net
* update the binary
