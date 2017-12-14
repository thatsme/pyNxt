# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSTagCount(Parent):

    def __init__(self, inStockOnly=False, rb=None ):
        """
            Get the number of tags used by all sellers.

            GetDGSTagCount take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Tag_Count

            REQUEST
            :param completed : is true if only completed purchase orders are to be included (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            Note: If none of the optional parameters are specified, all in-stock products in the blockchain
            are retrieved at once, which may take a long time.

            RESPONSE
            :return numberOfTags : (N) is the number of tags
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

        self.inStockOnly = inStockOnly
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        if self.inStockOnly:
            self.data["inStockOnly"] = inStockOnly

        super(GetDGSTagCount, self).__init__(rt = "getDGSTagCount", data=self.data, rb=self.rb)

    def run(self):
        super(GetDGSTagCount, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSTagCount, self).getData(key)             # calls 'BaseGet.getData()'