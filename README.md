<div align="center">
  <img src="https://www.quadrans.io/assets/brand/blockchain/logo_quadrans_color.svg"><br>
</div>

-----------------

## What is it?

**Quadrans Wiki** is the official documentation for the [Quadrans Blockchain](https://quadrans.io). 
This wiki is created on [Sphinx](http://www.sphinx-doc.org/) written with [Markdown](https://daringfireball.net/projects/markdown/) and [reStructuredText](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). 

The first pages of this documentation were written by **Piersandro Guerrera** and **Marco Crotta**, members of the Quadrans Foundation.

## Main Arguments

* **Get Started**: What is Quadrans? How the Quadrans blockchain works? What is a Token or a Coin?
* **Nodes**: Installation guides, compile and build, management informations and much more about Quadrans Nodes.
* **Wallets**: How-to create a wallet, check your balance, backup your private key and transfer Quadrans Coins.
* **Cryptocurrencies**: What is a Quadrans Token and how it works?
* **Programming**: Useful information for starting programming your first Quadrans blockchain smart contract.
* **Development**: How to become a go-quadrans contributor.
* **Projects**: Projects related to Quadrans Foundation and its partners.

## Contributing

Contributing to the documentation benefits everyone who uses *Quadrans blockchain*. We encourage you to help us improve the documentation, and you don’t have to be an expert to do so! If something in the docs doesn’t make sense to you, updating the relevant section after you figure it out is a great way to ensure it will help the next person.

## Building the source
For deploying the **Quadrans Wiki** clone this repository and install the `python3-sphinx` with the complete `requirements.txt`

```
cd docs
pip3 install -r requirements.txt
make html
```

### Dependancies

Software dependancies:

```
python3
python3-pip
python3-sphinx v4+
```

Module dependancies:

``` requirements.txt
pyfiglet==0.8.post1
recommonmark==0.7.1
termcolor==1.1.0
web3==5.12.0
```

## License
[GNU GPL 3](LICENSE)

## Documentation
The official documentation is hosted on Quadrans Documentation website: https://docs.quadrans.io
Thanks to the complete compatibility between the **Quadrans** and **Ethereum** blockchains, some parts of the documentation are inherited from the [Go-Ethereum documentation](https://geth.ethereum.org/docs/).