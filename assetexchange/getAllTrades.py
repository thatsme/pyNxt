# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAllTrades(Parent):
    def __init__(self, timestamp=0, firstIndex=None, lastIndex=None, includeAssetInfo=False, requireBlock=None, requireLastBlock=None ):
        """
            Get all trades since a given timestamp in reverse block height order.

            GetAllTrades take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_All_Trades

            REQUEST
            timestamp : is the timestamp (in seconds since the genesis block) to begin retrieving trades (optional, default 0)
            firstIndex : is a zero-based index to the first alias to retrieve (O)
            lastIndex : is a zero-based index to the last alias to retrieve (O)
            includeAssetInfo : is true if asset information is to be included in the result (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            assets : is an array (A) of asset objects (refer to Get Asset)
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
        self.timestamp = timestamp
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.includeAssetInfo = includeAssetInfo
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

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

        super(GetAllTrades, self).__init__(rt="getAllTrades", data=self.data)

    def run(self):
        super(GetAllTrades, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAllTrades, self).getData(key)                           # calls 'BaseGet.getData()'
