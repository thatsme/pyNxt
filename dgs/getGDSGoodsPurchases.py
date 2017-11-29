# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSGoodsPurchases  (Parent):

    def __init__(self, goods=None, buyer=None, firstIndex=None, lastIndex=None, withPublicFeedbacksOnly=False, completed=False, requireBlock=None, requireLastBlock=None ):
        """
            Get completed purchase orders given a goods ID and optionally a buyer ID in reverse chronological order.

            GetDGSGoodsPurchases take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Goods_Purchases

            REQUEST
            goods is the goods ID
            buyer is a buyer ID (optional)
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            withPublicFeedbacksOnly : is true if purchase orders without public feedback are to be omitted (B) (O)
            completed : is true if only completed purchase orders are to be included (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            Note: If none of the optional parameters are specified, all in-stock products in the blockchain
            are retrieved at once, which may take a long time.

            RESPONSE
            purchases : is an array (A) of purchase orders (refer to Get DGS Purchase for details)
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

        self.goods = goods
        self.buyer = buyer
        self.withPublicFeedbacksOnly = withPublicFeedbacksOnly
        self.completed = completed
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["goods"] = goods
        self.data["buyer"] = buyer

        if self.withPublicFeedbacksOnly:
            self.data["withPublicFeedbacksOnly"] = withPublicFeedbacksOnly
        if self.completed:
            self.data["completed"] = completed

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetDGSGoodsPurchases, self).__init__(rt = "getDGSGoodsPurchases", data=self.data)

    def run(self):
        super(GetDGSGoodsPurchases, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSGoodsPurchases, self).getData(key)             # calls 'BaseGet.getData()'