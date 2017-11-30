# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountCurrentBidOrderIds(Parent):

    def __init__(self, account=None, assets=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):
        """
            GetAccountCurrentBidOrderIds take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Current_Bid_Order_Ids

            REQUEST
            accounts : is the id of accounts (S) (R)
            asset : is an asset ID filter (S) (O)
            firstIndex : is a zero-based index to the first order ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last order ID to retrieve (N) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            bidOrderIds or askOrderIds : is an array (A) of order IDs
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            requestProcessingTime : is the API request processing time (N) (in millisec)

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

        self.account = account
        self.assets = assets
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["assets"] = self.assets
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountCurrentBidOrderIds, self).__init__(rt = "getAccountCurrentBidOrderIds", data=self.data)

    def run(self):
        super(GetAccountCurrentBidOrderIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrentBidOrderIds, self).getData(key)    # calls 'BaseGet.getData()'