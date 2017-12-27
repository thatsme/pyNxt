# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSGoodsCount(Parent):

    def __init__(self, seller=None, inStockOnly=False, ri=None, rb=None ):
        """
            Get the number of products for sale by a given seller or all sellers.

            GetDGSGoodsCount take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Goods_Count

            REQUEST
            :param seller : is the accounts ID of the product seller (S) (O)
            :param inStockOnly : is false if out-of-stock products (zero quantity) are to be retrieved (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            Note: If none of the optional parameters are specified, all in-stock products in the blockchain
            are retrieved at once, which may take a long time.

            RESPONSE
            :return numberOfGoods : (N) is the number of goods for sale by the seller
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

        self._seller = seller
        self._inStockOnly = inStockOnly
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["seller"] = seller

        if self.inStockOnly:
            self.data["inStockOnly"] = inStockOnly

        super(GetDGSGoodsCount, self).__init__(rt = "getDGSGoodsCount", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        self._seller = value

    @property
    def inStockOnly(self):
        return self._inStockOnly

    @inStockOnly.setter
    def inStockOnly(self, value):
        self._inStockOnly = value

    @property
    def ri(self):
        return self._ri

    @ri.setter
    def ri(self, value):
        self._ri = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetDGSGoodsCount, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSGoodsCount, self).getData(key)             # calls 'BaseGet.getData()'