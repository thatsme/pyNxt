# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetDeletes(Parent):
    def __init__(self, asset=None, account=None, firstIndex=None, lastIndex=None, timestamp=0, includeAssetInfo=False, requireBlock=None, requireLastBlock=None ):
        """
            Get asset deletions for a specific asset or account.

            GetAssetDeletes take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Deletes

            REQUEST
            asset : is the asset ID (S)
            account : is the account ID (optional if asset is provided)
            firstIndex : is a zero-based index to the first account to retrieve (N) (O)
            lastIndex : is a zero-based index to the last account to retrieve (N) (O)
            timestamp : is the earliest deletion (in seconds since the genesis block) to retrieve (N) (O)
            includeAssetInfo : is true if asset information is to be included (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            deletes : is an array (A) of asset delete objects with following properties:
            > quantityQNT : (S) is the number of shares that was deleted
            > assetDelete : (S) is the transaction ID
            > account : (S) is the account ID
            > accountRS : (S) is the account Reed Solomon address
            > asset : (S) is the asset ID
            > height : (N) is the block height of the delete
            > timestamp : (N) is the block timestamp of the delete
            > decimals : (N) is the number of decimal places used by the asset (if includeAssetInfo is true)
            > name : (S) is the asset name (if includeAssetInfo is true)
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
        self.account = account
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.timestamp = timestamp
        self.includeAssetInfo = includeAssetInfo
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset
        self.data["account"] = self.account

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.includeAssetInfo:
            self.data["includeAssetInfo"] = self.includeAssetInfo

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAssetDeletes, self).__init__(rt="getAssetDeletes", data=self.data)

    def run(self):
        super(GetAssetDeletes, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetDeletes, self).getData(key)                           # calls 'BaseGet.getData()'
