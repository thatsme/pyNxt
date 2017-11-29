# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAskOrders(Parent):
    def __init__(self, asset=None, sortByPrice=False, showExpectedCancellations=False, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get bid/ask orders given an asset ID, in order of decreasing bid price or increasing ask price
            (if sortByPrice is true for expected orders, otherwise in the expected order of execution).

            GetAskOrders take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Ask_Orders

            REQUEST
            asset : is the asset ID (S)
            sortByPrice : is true to sort by price (optional, applies only to expected orders,
                        which are returned in expected order of execution by default) (B)
            showExpectedCancellations : is true to include orders that are expected to be cancelled in the next block,
                        based on the content of the unconfirmed transactions pool and the phased transactions
                        expected to finish in the next block (optional, does not apply to expected orders) (B)
            firstIndex : is a zero-based index to the first order ID to retrieve (O)
            lastIndex : is a zero-based index to the last order ID to retrieve (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            askOrders : is an array (A) of order objects (refer to Get Order for details) with the following additional field only for an expected order:
            > phased (B) is true if the order is phased, false otherwise
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
        self.sortByPrice = sortByPrice
        self.showExpectedCancellations = showExpectedCancellations
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["asset"] = self.asset
        if self.sortByPrice:
            self.data["sortByPrice"] = self.sortByPrice
        if self.showExpectedCancellations:
            self.data["showExpectedCancellations"] = self.showExpectedCancellations

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAskOrders, self).__init__(rt="getAskOrders", data=self.data)

    def run(self):
        super(GetAskOrders, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAskOrders, self).getData(key)                           # calls 'BaseGet.getData()'
