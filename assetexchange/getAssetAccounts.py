# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetAccounts(Parent):
    def __init__(self, asset=None, height=None, requireBlock=None, requireLastBlock=None ):
        """
            Get the accounts that own an asset given the asset ID in reverse quantity order.

            GetAssetAccounts take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Accounts

            REQUEST
            asset : is the asset ID (S)
            height : is the height of the blockchain to determine the accounts (N) (O) ( default is last block)
            firstIndex : is a zero-based index to the first account to retrieve (N) (O)
            lastIndex : is a zero-based index to the last account to retrieve (N) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            Note: If table trimming is enabled (default), the height must be within 1440 blocks of the last block.

            RESPONSE
            accountAssets : is an array (A) of asset objects with the following fields for each asset:
            > quantityQNT : is the quantity (in QNT) of the assets (S)
            > accountRS : is the Reed-Solomon address of the account that own the asset (S)
            > unconfirmedQuantityQNT : is the unconfirmed quantity (in QNT) of the asset (S)
            > asset : is the asset ID (S)
            > account : is the number of the account that own the asset (S)
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            requestProcessingTime : is the API request processing time (in millisec) (N)

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
                (O) Object
                >   Array Element
                (WP) Wrapper specific parameter


        """

        # Required parameters
        self.asset = asset
        self.height = height
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset
        self.data["height"] = self.height

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAssetAccounts, self).__init__(rt="getAssetAccounts", data=self.data)

    def run(self):
        super(GetAssetAccounts, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetAccounts, self).getData(key)                           # calls 'BaseGet.getData()'
