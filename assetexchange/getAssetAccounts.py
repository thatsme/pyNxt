# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetAccounts(Parent):
    def __init__(self, asset=None, height=None, rb=None ):
        """
            Get the accounts that own an asset given the asset ID in reverse quantity order.

            GetAssetAccounts take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Accounts

            REQUEST
            :param asset : is the asset ID (S)
            :param height : is the height of the blockchain to determine the accounts (N) (O) ( default is last block)
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
        self.asset = asset
        self.height = height
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset
        self.data["height"] = self.height

        super(GetAssetAccounts, self).__init__(rt="getAssetAccounts", data=self.data, rb=self.rb)

    def run(self):
        super(GetAssetAccounts, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetAccounts, self).getData(key)                           # calls 'BaseGet.getData()'
