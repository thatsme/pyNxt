# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAsset(Parent):
    def __init__(self, asset=None, includeCounts=False, requireBlock=None, requireLastBlock=None ):
        """
            Get asset information given an asset ID.

            GetAsset take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset

            REQUEST
            asset : is the asset ID (S) (R)
            includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            account : is the number of the account that issued the asset (S)
            accountRS : is the Reed-Solomon address of the account that issued the asset (S)
            name : is the asset name (S)
            description : is the asset description (S)
            quantityQNT : is the total asset quantity (in QNT) in existence (S)
            asset : is the asset ID (N)
            decimals : is the number of decimal places used by the asset (N)
            numberOfAccounts : is the number of accounts that own the asset (N)
            numberOfTrades : is the number of trades of this asset (N)
            numberOfTransfers : is the number of transfers of this asset (N)
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
        self.includeCounts = includeCounts
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset

        if self.includeCounts:
            self.data["includeCounts"] = self.includeCounts

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAsset, self).__init__(rt="getAsset", data=self.data)

    def run(self):
        super(GetAsset, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAsset, self).getData(key)                           # calls 'BaseGet.getData()'
