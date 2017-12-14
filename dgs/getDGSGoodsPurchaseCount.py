# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSGoodsPurchaseCount(Parent):

    def __init__(self, goods=None, withPublicFeedbacksOnly=False, completed=False, rb=None ):
        """
            Get the number of completed purchase orders given a goods ID.

            GetDGSGoodsPurchaseCount take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Goods_Purchase_Count

            REQUEST
            :param goods is the goods ID
            :param withPublicFeedbacksOnly : is true if purchase orders without public feedback are to be omitted (B) (O)
            :param completed : is true if only completed purchase orders are to be included (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            Note: If none of the optional parameters are specified, all in-stock products in the blockchain
            are retrieved at once, which may take a long time.

            RESPONSE
            :return numberOfPurchases : (N) is the number of completed purchase orders
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

        self.goods = goods
        self.withPublicFeedbacksOnly = withPublicFeedbacksOnly
        self.completed = completed
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["goods"] = goods

        if self.withPublicFeedbacksOnly:
            self.data["withPublicFeedbacksOnly"] = withPublicFeedbacksOnly
        if self.completed:
            self.data["completed"] = completed

        super(GetDGSGoodsPurchaseCount, self).__init__(rt = "getDGSGoodsPurchaseCount", data=self.data, rb=self.rb)

    def run(self):
        super(GetDGSGoodsPurchaseCount, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSGoodsPurchaseCount, self).getData(key)             # calls 'BaseGet.getData()'