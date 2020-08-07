Test Contract: Echo
===================

Echo is a simple test contract deployed on the Quadrans **test** network. You can use it to test procedures and interfaces. All it does is store a string value and allow you to retrieve the value later: write a string, read a string

## Deploy

* The contract address is: **0x12C67Ba6AF1AeD8dC58c8337c2100789DfFb02A9**
* Deploy tx = **0x62daf8bcd72fc76a3f9193e46cb252e6dd31e20eb0526f3f29341b03a1ea3766**

## Code

NB: please do not re-deploy this contract on testnet or main net

``` 
pragma solidity \^0.5.1;

contract test {

  string str;
   event report(string _s, address _addr);

   constructor() public {
       str="echo.sol";
   }

   function get() public view returns (string memory) {
       return str;
   }

   function set(string memory  _s) public {
       str =  _s;
       emit report(_s,msg.sender);
   }

}
```

## ABI

Oneliner

``` 
[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"_s","type":"string"},{"indexed":false,"internalType":"address","name":"_addr","type":"address"}],"name":"report","type":"event"},{"constant":true,"inputs":[],"name":"get","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_s","type":"string"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]
```

Multi line:

``` js
[
   {
       "inputs": [],
       "payable": false,
       "stateMutability": "nonpayable",
       "type": "constructor"
   },
   {
       "anonymous": false,
       "inputs": [
           {
               "indexed": false,
               "internalType": "string",
               "name": "_s",
               "type": "string"
           },
           {
               "indexed": false,
               "internalType": "address",
               "name": "_addr",
               "type": "address"
           }
       ],
       "name": "report",
       "type": "event"
   },
   {
       "constant": true,
       "inputs": [],
       "name": "get",
       "outputs": [
           {
               "internalType": "string",
               "name": "",
               "type": "string"
           }
       ],
       "payable": false,
       "stateMutability": "view",
       "type": "function"
   },
   {
       "constant": false,
       "inputs": [
           {
               "internalType": "string",
               "name": "_s",
               "type": "string"
           }
       ],
       "name": "set",
       "outputs": [],
       "payable": false,
       "stateMutability": "nonpayable",
       "type": "function"
   }

]
```