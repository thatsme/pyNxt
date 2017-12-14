# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSTags(Parent):

    def __init__(self, inStockOnly=False, ri=None, rb=None ):
        """
            Get tags used by all sellers in reverse inStockCount, reverse totalCount, tag order.

            GetDGSTags take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Tags

            REQUEST
            :param inStockOnly : is false if out-of-stock products (zero quantity) are to be retrieved (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)


            RESPONSE
            :return tags : (A) is an array of tag objects with the following fields for each tag:
            > inStockCount (N) is the number of products available for sale as tagged
            > tag (S) is the tag word
            > totalCount (N) is the total number of products as tagged
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

        self.inStockOnly = inStockOnly
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        if self.inStockOnly:
            self.data["inStockOnly"] = inStockOnly

        super(GetDGSTags, self).__init__(rt = "getDGSTags", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetDGSTags, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSTags, self).getData(key)             # calls 'BaseGet.getData()'