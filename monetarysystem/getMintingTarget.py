# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetMintingTarget(Parent):
    def __init__(self, currency=None, account=None, units= 0, rb=None ):
        """
            Get the last exchange of each of multiple currencies.

            GetMintingTarget take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Minting_Target

            REQUEST
            :param currency : is the mintable currency ID (S)
            :param account is the minting account ID
            :param units is the amount (in QNT) of currency to mint
            :param rb : rb object ( check base/Rb.py) (WP)

            Note: units cannot be greater than 1/10000 of the maxSupply (refer to Issue Currency).
            Increasing units decreases targetBytes.

            RESPONSE
            :return difficulty : (S) is the current difficulty, an estimate of the number of hashes needed to meet the target
            :return targetBytes : (S) is the 32-byte target (little endian), which must equal or exceed the computed hash of the nonce
            :return currency : (S) is the currency ID
            :return counter : (N) is the counter associated with the minting account, the value previously submitted to Currency Mint
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

            Note: If a nonce is found such that its hash is less than the target, it can be submitted to the blockchain
            along with counter + 1 using Currency Mint, which results in units NQT being credited to the minting account.
            difficulty is inversely related to the target, and so increases exponentially as maxSupply is approached because
            the target is defined as (2exp-1)/units, where exp decreases linearly from 256-minDifficulty to 256-maxDifficulty.
            (Refer to Issue Currency for maxSupply, minDifficulty and maxDifficulty.)

            Legenda :
                ° the parameter are interchangeable on
                * if you use the secretPhrase , the transaction is immediately broadcasted to network
                ** if you use the publicKey, you create an unsigned Transaction, and you need to sign and broardcast
                *** for buying
                (R) Required
                (O) Optional
                (N) Number
                (S) String
                (B) Boolean
                (A) Array
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        # Required parameters
        self.currency = currency
        self.account = account
        self.units = units
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currencies"] = self.currency
        self.data["account"] = self.account
        self.data["units"] = self.units

        super(GetMintingTarget, self).__init__(rt="getMintingTarget", data=self.data, rb=self.rb)

    def run(self):
        super(GetMintingTarget, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetMintingTarget, self).getData(key)                           # calls 'BaseGet.getData()'
