# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class SearchDGSGoods(Parent):

    def __init__(self, query=None, tag=None, seller=None, inStockOnly=False, hideDelisted=False, includeCounts=False, ri=None, rb=None ):
        """
            Get product listings that have a name or description that match a given query in reverse relevance order,
            then name order (given a seller), then reverse chronological order.

            SearchDGSGoods take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Search_DGS_Goods

            REQUEST
            :param query : is a full text query on the goods fields name and description in the standard Lucene syntax (S) (O)
            :param tag : is a query on the good field tags in the standard Lucene syntax (S) (O)
            :param seller : is the accounts ID of the product seller (S) (O)
            :param inStockOnly : is false if out-of-stock products (zero quantity) are to be retrieved (B) (O)
            :param hideDelisted : is true if delisted products are to be omitted (B) (O)
            :param includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)


            RESPONSE
            :return goods : (A) is an array of goods objects (refer to Get DGS Good for details)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

            Note: The ...Count fields refer to the number of distinct products tagged, regardless of the quantity of each.

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
        self.query = query
        self.tag = tag
        self.seller = seller
        self.inStockOnly = inStockOnly
        self.hideDelisted = hideDelisted
        self.includeCounts = includeCounts
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}
        ## Create data dictionary
        self.data["query"] = query
        self.data["tag"] = tag
        self.data["seller"] = seller

        if self.inStockOnly:
            self.data["inStockOnly"] = inStockOnly
        if self.hideDelisted:
            self.data["hideDelisted"] = hideDelisted
        if self.inStockOnly:
            self.data["includeCounts"] = includeCounts

        super(SearchDGSGoods, self).__init__(rt = "searchDGSGoods", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(SearchDGSGoods, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(SearchDGSGoods, self).getData(key)             # calls 'BaseGet.getData()'
