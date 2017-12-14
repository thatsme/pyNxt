# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSPurchases  (Parent):

    def __init__(self, seller=None, buyer=None, withPublicFeedbacksOnly=False, completed=False,ri=None, rb=None ):
        """
            Get the number of purchase orders given a seller and/or buyer ID, or all orders combined.

            GetDGSPurchases take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Purchases

            REQUEST
            :param seller is the accounts ID of the seller (optional, default is all sellers)
            :param buyer is the accounts ID of the buyer (optional, default is all buyers)
            :param withPublicFeedbacksOnly : is true if purchase orders without public feedback are to be omitted (B) (O)
            :param completed : is true if only completed purchase orders are to be included (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return purchases : is an array (A) of purchase orders (refer to Get DGS Purchase for details)
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
        self.buyer = buyer
        self.withPublicFeedbacksOnly = withPublicFeedbacksOnly
        self.completed = completed
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["seller"] = seller
        self.data["buyer"] = buyer

        if self.withPublicFeedbacksOnly:
            self.data["withPublicFeedbacksOnly"] = withPublicFeedbacksOnly
        if self.completed:
            self.data["completed"] = completed

        super(GetDGSPurchases, self).__init__(rt = "getDGSPurchases", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetDGSPurchases, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSPurchases, self).getData(key)             # calls 'BaseGet.getData()'