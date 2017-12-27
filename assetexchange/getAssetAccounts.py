# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetAccounts(Parent):
    def __init__(self, asset=None, height=None, ri=None, rb=None ):
        """
            Get the accounts that own an asset given the asset ID in reverse quantity order.

            GetAssetAccounts take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Accounts

            REQUEST
            :param asset : is the asset ID (S)
            :param height : is the height of the blockchain to determine the accounts (N) (O) ( default is last block)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            Note: If table trimming is enabled (default), the height must be within 1440 blocks of the last block.

            RESPONSE
            :return accountAssets : is an array (A) of asset objects with the following fields for each asset:
            > quantityQNT : is the quantity (in QNT) of the assets (S)
            > accountRS : is the Reed-Solomon address of the accounts that own the asset (S)
            > unconfirmedQuantityQNT : is the unconfirmed quantity (in QNT) of the asset (S)
            > asset : is the asset ID (S)
            > accounts : is the number of the accounts that own the asset (S)
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
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset
        self.data["height"] = self.height

        super(GetAssetAccounts, self).__init__(rt="getAssetAccounts", data=self.data, rb=self.rb)

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
    def ri(self):
        return self._ri

    @ri.setter
    def ri(self, value):
        self._ri = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetAssetAccounts, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetAccounts, self).getData(key)                           # calls 'BaseGet.getData()'
