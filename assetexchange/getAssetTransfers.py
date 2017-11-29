# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetTransfers(Parent):
    def __init__(self, asset=None, account=None,  firstIndex=None, lastIndex=None, timestamp=0, includeAssetsInfo=False, requireBlock=None, requireLastBlock=None ):
        """
            Get transfers associated with a given asset and/or account in reverse block height order
            (or in the expected order of execution for expected transfers).

            GetAssetTransfers take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Transfers

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
            transfers : is an array (A) of transfer objects with the following fields for each transfer:
            > quantityQNT (S) is the quantity (in QNT) of the asset traded
            > senderRS (S) is the Reed-Solomon address of the sender
            > assetTransfer (S) is the transaction ID of the asset transfer
            > sender (S) is the account number of the sender
            > recipientRS (S) is the Reed-Solomon address of the recipient
            > decimals (N) is the number of decimal places used by the asset (if includeAssetInfo is true)
            > recipient (S) is the account number of the recipient
            > name (S) is the name of the asset (if includeAssetInfo is true)
            > asset (S) is the asset ID
            > height (N) is the height of the transfer block
            > timestamp (N) is the timestamp (in seconds since the genesis block) of the transfer block, does not apply to an expected transfer
            > phased (B) is true if the transaction is phased, false otherwise, applies only to an expected transfer
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
        self.includeAssetInfo = includeAssetsInfo
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset
        self.data["account"] = self.account
        self.data["timestamp"] = self.timestamp

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

        super(GetAssetTransfers, self).__init__(rt="getAssetTransfers", data=self.data)

    def run(self):
        super(GetAssetTransfers, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetTransfers, self).getData(key)                           # calls 'BaseGet.getData()'
