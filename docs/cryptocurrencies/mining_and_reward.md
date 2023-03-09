Mining and Reward
=================

**Quadrans reward mechanism** is designed to allow Token Holders, Miner nodes and Masternodes to be rewarded for their service to the network, with an amount of QDC that is proportional to the QDT held, every time new QDC are generated.

The distribution of QDC is regulated by an algorithm every time a block is closed (Epoch). QDC of each Epoch are stored on a Smart Contract, and they are sent to Quadrans Token Holders on a monthly basis.

The distribution of  [**newly minted QDC**](quadrans_coin.html#minting-quadrans-coin) is defined by the Quadrans protocol, according to the activity made by Token Holders (including mining nodes) during the previous month. As mining nodes participate to the consensus mechanism, Masternodes and Miner nodes are rewarded with more QDC compared to non-mining Token Holders.

|*|QDT Q.ty|Kind of work|Reward|
|--|--|--|--|
|Holder|⩾ 1|*to be comunicated*|5%|
|Miner|⩾ 1.000|Active node|40%|
|Masternode|⩾ 100.000|Active node|55%|

QDC intended for reward are sent to wallet addresses registered on an active node (with a minimum uptime of 80% on a weekly basis) to simplify the distribution of the reward.

## Enable your node for mining

### Requirements

* Registration to the [Quadrans Community](https://quadrans.io/get-started);
* [Quadrans Node](../nodes/index.html) configured as a Miner;
* Link your Quadrans Tokens with your Quadrans Node in the Community Hub:
  * Complete the KYC to access to the Nodes section;
  * To be recognised as a **Masternode**, a Token Holder needs to own at least **100.000 Quadrans Tokens (QDT)** and join Quadrans network by installing a node;
  * To be recognised as a **Miner**, a Token Holder needs to own at least **1.000 Quadrans Tokens (QDT)** and join Quadrans network by installing a node;
  * Check that in your node the mining options are enabled in the [configuration file](../nodes/index.html#installation);
* Keep your node active with a minimum uptime of 80% on a weekly basis.

### Link your Quadrans Tokens to your node

Through the **Community Hub**, Quadrans Token owners have the possibility to enable mining on their nodes.

To proceed, after registering in the [Quadrans Community](https://quadrans.io/get-started) simply select the *Add Miner* or *Add Masternode* items from the Nodes menu of the Token Portal, depending on the number of Tokens in your possession.


### Quadrans Token wallet verification

To activate your node as a *Miner* or *Masternode* it is necessary to confirm the ownership of the Ethereum wallet address where you store your Quadrans Tokens (QDT).
The verification will be made by signing a message using the address itself. No transaction fees will be applied.

The **Token Portal** allows to automatically sign the verification and confirm the ownership of an Ethereum wallet created in the Metamask wallet application for computer or manually with any other.

#### Metamask Quadrans Token wallet signing:

1. From the *Add Miner* or *Add Masternode* page insert the Node Name, the Quadrans Coin Address (the Wallet created inside the Quadrans Node) and the Quadrans Token address (the wallet where the QDT are stored)
2. Click on *Activate*
3. Click on *Verify using Metamask wallet* button
4. Insert your wallet password on Metamask when requested
5. Select the wallet you want to use
6. Authorize “Quadrans Token Portal” application
7. Click on the *Sign* button to confirm

For others wallet it is necessary to manually sign the verification message. The procedure may change for each single wallet application. As an example the following guide will consider the Coinomi application.

#### Coinomi Quadrans Token wallet signing: 

1. From the *Add Miner* or *Add Masternode* page insert the Node Name, the Quadrans Coin Address (the Wallet created inside the Quadrans Node) and the Quadrans Token address (the wallet where the QDT are stored)
2. Click on *Activate*
3. Click on *Verify using your wallet app* button
4. Open the Ethereum wallet where your Quadrans Token are stored 
5. On the "receive" screen, copy the address to sign with
6. Back to the "balance" screen, select "... - Sign/verify message"
7. Paste the address you want to sign on the first box
8. Write the message showed on the Token Portal page
9. Press the "sign" button and confirm with your password
10. Copy the signature completely, and copy the result in the form
11. Press the "Verify" button

#### Other wallet signing: 

You can use any other Ethereum Wallet to store the Quadrans Tokens. For signing please verify how to sign the verification message with your wallet.

*If you use a different wallet application and want to contribute to this guide please update the GitHub repository or contact the Quadrans Foundation from the official website indicating how to sign with your app.*

### Quadrans Coins reward

According to the activity made by Quadrans Miner and Quadrans Masternode during the previous month, the Quadrans Coin wallet will receive a monthly reward.

## Protect your Quadrans Community Hub account

To ensure that your account in the Quadrans Community Hub is fully protected, from your Profile you can enable the two-factor authentication to strengthen the security of your account. 

Two-factor authentication (2FA) is a security system that requires two distinct forms of identification in order to access to your account: your password and a one time code generated by an application.

The choice of 2FA apps is surprisingly wide, here some of the most used 2FA applications for your smartphone or computer.

### Google Authenticator

Supported platforms:
[Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) | [iOS](https://itunes.apple.com/app/google-authenticator/id388497605)

Google Authenticator is the easiest to use of all the many 2FA apps out there. It doesn’t even have any settings.
  
### Microsoft Authenticator

Supported platforms: [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) | [iOS](https://itunes.apple.com/app/microsoft-authenticator/id983156458)

Microsoft Authenticator is noticeably more feature-rich than Google Authenticator. All codes are shown by default, each token can be separately configured to be hidden.

### Duo Mobile

Supported platforms: [Android](https://play.google.com/store/apps/details?id=com.duosecurity.duomobile) | [iOS](https://itunes.apple.com/app/duo-mobile/id422663827)

It has one advantage over Google Authenticator: Duo Mobile keeps codes hidden by default. To see them the user must tap the specific token. 
  
### FreeOTP

Supported platforms: [Android](https://play.google.com/store/apps/details?id=org.fedorahosted.freeotp) | [iOS](https://itunes.apple.com/app/freeotp-authenticator/id872559395)

This software, by Red Hat, is open source and it is the lightest app for your smartphone (less than 1 Megabyte). The app hides codes by default, displaying them only if the token is tapped.  

### Authy

Supported platforms: [Android](https://play.google.com/store/apps/details?id=com.authy.authy) | [iOS](https://itunes.apple.com/app/authy/id494168017) | [Windows](https://authy.com/download/) | [macOS](https://authy.com/download/)

Authy  main advantage being that all tokens are stored in the cloud. This makes it possible to access tokens from any of your devices (computers or smartphone).

### Yandex.Key

Supported platforms: [Android](https://play.google.com/store/apps/details?id=ru.yandex.key) | [iOS](https://itunes.apple.com/app/yandex-key-2fa-and-one-time-passwords/id957324816)

Easy to use as Google Authenticator and it has several additional features available. Yandex.Key can be locked with a PIN or fingerprint and allows toto create a password-protected backup copy of tokens in the Yandex cloud.