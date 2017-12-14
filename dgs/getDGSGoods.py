# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSGoods(Parent):

    def __init__(self, seller=None, inStockOnly=False, hideDelisted=False, includeCounts=False, ri=None, rb=None ):
        """
            Get DGS products for sale in reverse chronological listing creation order unless a seller is given, then in product name order.

            GetDGSGoods take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Goods

            REQUEST
            :param seller : is the accounts ID of the product seller (S) (O)
            :param inStockOnly : is false if out-of-stock products (zero quantity) are to be retrieved (B) (O)
            :param hideDelisted : is true if delisted products are to be omitted (B) (O)
            :param includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            Note: If none of the optional parameters are specified, all in-stock products in the blockchain
            are retrieved at once, which may take a long time.

            RESPONSE
            :return goods : is an array (A) of goods (refer to Get DGS Good for details)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self.seller = seller
        self.inStockOnly = inStockOnly
        self.hideDelisted = hideDelisted
        self.includeCounts = includeCounts
        self.ri = ri
        self.rb = rb
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

        super(GetDGSGoods, self).__init__(rt = "getDGSGoods", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetDGSGoods, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSGoods, self).getData(key)             # calls 'BaseGet.getData()'