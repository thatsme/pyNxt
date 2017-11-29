# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAllOpenAskOrders(Parent):
    def __init__(self, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get all open bid/ask orders in reverse block height order.

            GetAllOpenAskOrders take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_All_Open_Ask_Orders

            REQUEST
            firstIndex : is a zero-based index to the first alias to retrieve (O)
            lastIndex : is a zero-based index to the last alias to retrieve (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            openOrders :is an array (A) of order objects (refer to Get Order for details)
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
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary


        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex

        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex


        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAllOpenAskOrders, self).__init__(rt="getAllOpenAskOrders", data=self.data)

    def run(self):
        super(GetAllOpenAskOrders, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAllOpenAskOrders, self).getData(key)                           # calls 'BaseGet.getData()'
