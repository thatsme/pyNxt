# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBlocks(Parent):
    def __init__(self, timestamp=0, firstIndex=None, lastIndex=None, includeTransactions=False, includeExecutedPhased=False, requireBlock=None, requireLastBlock=None ):
        """
            Get blocks from the blockchain in reverse block height order.

            GetBlocks take a default 1/3 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Blocks

            REQUEST
            timestamp : is the timestamp (N) (in seconds since the genesis block) of the block (optional if height provided)
            firstIndex : is first block to retrieve (optional, default is zero or the last block on the blockchain)
            lastIndex : is the last block to retrieve (optional, default is firstIndex + 99)
            includeTransactions : is true to include transaction details (B) (O)
            includeExecutedPhased : is true to include approved and executed phased transactions (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (optional)

            RESPONSE
            blocks : is an array (A) of blocks retrieved (refer to Get Block for details)
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
        self.includeTransactions = includeTransactions
        self.includeExecutedPhased = includeExecutedPhased
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["timestamp"] = self.timestamp
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lasetIndex"] = self.lastIndex
        if self.includeTransactions:
            self.data["includeTransactions"] = self.includeTransactions
        if self.includeExecutedPhased:
            self.data["includeExecutedPhased"] = self.includeExecutedPhased
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetBlocks, self).__init__(rt="getBlocks", data=self.data)

    def run(self):
        super(GetBlocks, self).run()                                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(GetBlocks, self).getData(key)                           # calls 'BasePost.getData()'
