How to Convert a BIP39 Mnemonic Passphrase in a Private Key
===========================================================

## What is this

This guide is dedicated to users who use software wallets such as **Coinomi** or **Eidoo** who intend to participate in the [Quadrans Staking Program](../../cryptocurrencies/staking.md) or who want to use the **MetaMask** as wallet instead of their previous software. In no other case is it necessary to follow the instructions below. If you don't need it, don't do it.

**Warning:** Never share your recovery phrase or private keys with anyone. Anyone who has access to that information can steal your funds without your permission.

Software wallets such as **Coinomi** or **Eidoo** do not natively allow the export the Private Key of your wallet. To ensure ease of use, these software generally require the user to keep only a **BIP39 Mnemonic Passphrase** (or "seed phrase") to restore their wallets with extreme ease.

## How to use Mnemonic Code Converter

The tool we offer is a **Mnemonic Code converter** developed by [Ian Coleman](https://github.com/iancoleman/bip39) that allows you to export your Private Key easely. It can be used in offline mode, after loading the page you can disconnect your computer from the Internet or if you prefer to save the page and run it locally.

First open the following web address: [https://iancoleman.io/bip39/](https://iancoleman.io/bip39/)

Select the language of the seed phrases you have in the *Mnemonic Language*.

Enter your "seed phrase" in the *BIP39 mnemonic* field. Make sure that all the words are correct, a list of those not recognized will appear at the top.

In the *Coin* field select “ETH - Ethereum” (the network in which Quadrans Token are present).

Now in the **Deviation Path** section select the *BIP32* tab and set the Client as follows according to your software wallet.

## Identify your software wallet

### Coinomi

Select "Coinomi, Ledger" in the *Client* field.

### Eidoo

Select "Custom deviation path" in the *Client* field and fill in *BIP32 Deviation Path* with `m/44'/60'/0`

### Exodus

Select "Custom deviation path" in the *Client* field and fill in *BIP32 Deviation Path* with `m/44'/0'/0'` or `m/84'/0'/0'`

### Trust Wallet

Select "Custom deviation path" in the *Client* field and fill in *BIP32 Deviation Path* with `m/84'/0'/0'/0/0`

### Other

Please inform the [Quadrans Foundation](https://quadrans.io/contacts.php) or ask on our [Telegram support channel](https://t.me/quadrans) to identify the BIP32 Deviation Path of your software wallet to help you and update this guide.

## Extract the private key

Once this step is done at the bottom of the **Derived Addresses** paragraph, you will be presented with a list of wallet addresses derived from your Mnemonic Passphrase. The first should match the one you are using. Find your address and copy the private key that corresponds to it. 

If you are on a mobile device, you will need to scroll all the way to the right to see the corresponding private key.

## Import to Metamask

Click the circle icon at the top right corner of your MetaMask pop-up next to the network indicator.

Select *Import Account* on the dropdown menu. You will be directed to the *Import page*. 

Paste your Private Key and click “Import”.

You should be able to see the newly added account in the dropdown menu with an "Imported" tag next to the account.