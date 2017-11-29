# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSGoods(Parent):

    def __init__(self, seller=None, firstIndex=None, lastIndex=None, inStockOnly=False, hideDelisted=False, includeCounts=False, requireBlock=None, requireLastBlock=None ):
        """
            Get DGS products for sale in reverse chronological listing creation order unless a seller is given, then in product name order.

            GetDGSGoods take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Goods

            REQUEST
            seller : is the account ID of the product seller (S) (O)
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            inStockOnly : is false if out-of-stock products (zero quantity) are to be retrieved (B) (O)
            hideDelisted : is true if delisted products are to be omitted (B) (O)
            includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            Note: If none of the optional parameters are specified, all in-stock products in the blockchain
            are retrieved at once, which may take a long time.

            RESPONSE
            goods : is an array (A) of goods (refer to Get DGS Good for details)
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

        self.seller = seller
        self.inStockOnly = inStockOnly
        self.hideDelisted = hideDelisted
        self.includeCounts = includeCounts
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["seller"] = seller

        if self.inStockOnly:
            self.data["inStockOnly"] = inStockOnly
        if self.hideDelisted:
            self.data["hideDelisted"] = hideDelisted
        if self.includeCounts:
            self.data["includeCounts"] = includeCounts

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetDGSGoods, self).__init__(rt = "getDGSGoods", data=self.data)

    def run(self):
        super(GetDGSGoods, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSGoods, self).getData(key)             # calls 'BaseGet.getData()'