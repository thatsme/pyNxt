# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAsset(Parent):
    def __init__(self, asset=None, includeCounts=False, rb=None ):
        """
            Get asset information given an asset ID.

            GetAsset take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset

            REQUEST
            :param asset : is the asset ID (S) (R)
            :param includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return accounts : is the number of the accounts that issued the asset (S)
            :return accountRS : is the Reed-Solomon address of the accounts that issued the asset (S)
            :return name : is the asset name (S)
            :return description : is the asset description (S)
            :return quantityQNT : is the total asset quantity (in QNT) in existence (S)
            :return asset : is the asset ID (N)
            :return decimals : is the number of decimal places used by the asset (N)
            :return numberOfAccounts : is the number of accounts that own the asset (N)
            :return numberOfTrades : is the number of trades of this asset (N)
            :return numberOfTransfers : is the number of transfers of this asset (N)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)

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
        self.asset = asset
        self.includeCounts = includeCounts
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset

        if self.includeCounts:
            self.data["includeCounts"] = self.includeCounts

        super(GetAsset, self).__init__(rt="getAsset", data=self.data, rb=self.rb)

    def run(self):
        super(GetAsset, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAsset, self).getData(key)                           # calls 'BaseGet.getData()'
