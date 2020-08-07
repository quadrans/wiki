Accessing Blockchain via CURL
=============================

You can also access the blocchain via CURL by interacting with your node via JSON-RPC using CURL

You need to send all your CURL requests to your node or a remote node you can access on port 8545

The basic curl request is:

``` bash
curl -H "Content-Type: application/json" -X POST --data '{...}' localhost:8545
``` 

The "data" part is what changes between calls

See the whole list of calls at: <https://github.com/BlockChainCaffe/EthereumWiki/blob/master/JSON-RPC.md#example-28>