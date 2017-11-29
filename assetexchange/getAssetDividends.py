# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetDividends(Parent):
    def __init__(self, asset=None, firstIndex=None, lastIndex=None, timestamp=0, adminPassword=None, requireBlock=None, requireLastBlock=None ):
        """
            Get the dividend payment history for a specific asset.

            GetAssetDividends take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Dividends

            REQUEST
            asset : is the asset ID (S)
            account : is the account ID (optional if asset is provided)
            firstIndex : is a zero-based index to the first account to retrieve (N) (O)
            lastIndex : is a zero-based index to the last account to retrieve (N) (O)
            timestamp : is the earliest deletion (in seconds since the genesis block) to retrieve (N) (O)
            adminPassword is a string with the admin password  (S) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            dividends : is an array (A) of dividend transactions with the following properties:
            > assetDividend : (S) is the dividend payment transaction ID
            > numberOfAccounts : (N) is the number of accounts that received a dividend
            > amountNQTPerQNT : (S) is the amount of NXT (in NQT) paid per quantity (in QNT) of the asset
            > totalDividend : (S) is the total amount of NXT (in NQT) sent in the dividend payment
            > dividendHeight : (N) is the block height of the dividend calculation
            > asset : (S) is the asset ID
            > height : (N) is the block height of the dividend payment
            > timestamp : (N) is the block timestamp of the dividend payment
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
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.timestamp = timestamp
        self.adminPassword = adminPassword
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset
        self.data["timestamp"] = self.timestamp

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.adminPassword:
            self.data["adminPassword"] = self.adminPassword

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAssetDividends, self).__init__(rt="getAssetDividends", data=self.data)

    def run(self):
        super(GetAssetDividends, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetDividends, self).getData(key)                           # calls 'BaseGet.getData()'
