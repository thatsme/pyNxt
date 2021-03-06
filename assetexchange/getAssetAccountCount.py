# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetAccountCount(Parent):
    def __init__(self, asset=None, height=False, rb=None ):
        """
            Get asset information given an asset ID.

            GetAssetAccountCount take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Account_Count

            REQUEST
            :param asset : is the asset ID
            :param height : height is the height of the blockchain to determine the account count (optional, default is last block)
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
        self._asset = asset
        self._height = height
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset

        if self.includeCounts:
            self.data["includeCounts"] = self.includeCounts

        super(GetAssetAccountCount, self).__init__(rt="getAssetAccountCount", data=self.data, rb=self.rb)

    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, value):
        self._asset = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetAssetAccountCount, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAssetAccountCount, self).getData(key)                           # calls 'BaseGet.getData()'
