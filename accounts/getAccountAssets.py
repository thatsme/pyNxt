# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountAssets(Parent):

    def __init__(self, account=None, assets=None, height=None, includeAssetsInfo=False, rb=None):
        """
            GetAccountAssets take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Assets

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param assets : is an asset ID filter (O)
            :param height : is the height of the blockchain to determine the asset count (N) (O) (default is last block)
            :param includeAssetInfo : is true if asset information is to be included (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return accountAssets : is an array of asset objects (A) (unless the asset parameter is specified) with the following fields for each asset:
            > quantityQNT : is the quantity (in QNT) of the asset (S)
            > unconfirmedQuantityQNT : is the unconfirmed quantity (in QNT) of the asset (S)
            > decimals : is the number of decimal places used by the asset (N) (if includeAssetInfo is true)
            > name : is the asset name (S) (if includeAssetInfo is true)
            > asset : is the asset ID (S)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

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

        self.account = account
        self.assets = assets
        self.height = height
        self.includeAssetsInfo = includeAssetsInfo
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.assets:
            self.data["assets"] = self.assets
        if self.includeAssetsInfo:
            self.data["includeAssetsInfo"] = self.includeAssetsInfo
        if self.height:
            self.data["height"] = self.height

        super(GetAccountAssets, self).__init__(rt = "getAccountAssets", data=self.data, rb=self.rb)

    def run(self):
        super(GetAccountAssets, self).run()                                 # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountAssets, self).getData(key)                   # calls 'BaseGet.getData()'