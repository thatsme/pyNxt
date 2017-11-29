# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBidOrderIds(Parent):
    def __init__(self, asset=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get bid/ask order IDs given an asset ID, in order of decreasing bid price or increasing ask price.

            GetBidOrderIds take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Bid_Order_Ids

            REQUEST
            asset : is the asset ID (S)
            firstIndex : is a zero-based index to the first order ID to retrieve (O)
            lastIndex : is a zero-based index to the last order ID to retrieve (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            bidOrderIds : is an array (A) of order IDs
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
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["asset"] = self.asset

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetBidOrderIds, self).__init__(rt="getBidOrderIds", data=self.data)

    def run(self):
        super(GetBidOrderIds, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBidOrderIds, self).getData(key)                           # calls 'BaseGet.getData()'
