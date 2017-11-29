# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBidOrder(Parent):
    def __init__(self, order=None, requireBlock=None, requireLastBlock=None ):
        """
            Get a bid/ask order given an order ID.

            GetBidOrder take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Bid_Order

            REQUEST
            order : is the Order ID
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            account : is the account number associated with the order (S)
            accountRS : is the Reed-Solomon address of the account (S)
            asset : is the ID of the asset being ordered (S)
            quantityQNT : is the order quantity (in QNT) (S)
            priceNQT : is the order price (in NQT) (S)
            height : is the block height of the order transaction (N)
            transactionHeight : is the transaction height (N)
            transactionIndex : is a zero-based index giving the order of the transaction in its block (N)
            order : is the ID of the order (S)
            type : is the type of order (bid or ask) (S)
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
        self.order = order
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["order"] = self.order

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetBidOrder, self).__init__(rt="getBidOrder", data=self.data)

    def run(self):
        super(GetBidOrder, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBidOrder, self).getData(key)                           # calls 'BaseGet.getData()'
