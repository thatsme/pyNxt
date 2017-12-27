# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSPurchaseCount  (Parent):

    def __init__(self, seller=None, buyer=None, withPublicFeedbacksOnly=False, completed=False, rb=None ):
        """
            Get the number of purchase orders given a seller and/or buyer ID, or all orders combined.

            GetDGSPurchaseCount take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Purchase_Count

            REQUEST
            :param seller is the accounts ID of the seller (optional, default is all sellers)
            :param buyer is the accounts ID of the buyer (optional, default is all buyers)
            :param withPublicFeedbacksOnly : is true if purchase orders without public feedback are to be omitted (B) (O)
            :param completed : is true if only completed purchase orders are to be included (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return numberOfPurchases : (N) is the number of purchase orders associated with the seller and/or buyer
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
        self._buyer = buyer
        self._withPublicFeedbacksOnly = withPublicFeedbacksOnly
        self._completed = completed
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["seller"] = seller
        self.data["buyer"] = buyer

        if self.withPublicFeedbacksOnly:
            self.data["withPublicFeedbacksOnly"] = withPublicFeedbacksOnly
        if self.completed:
            self.data["completed"] = completed

        super(GetDGSPurchaseCount, self).__init__(rt = "getDGSPurchaseCount", data=self.data, rb=self.rb)

    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        self._seller = value

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        self._buyer = value

    @property
    def withPublicFeedbacksOnly(self):
        return self._withPublicFeedbacksOnly

    @withPublicFeedbacksOnly.setter
    def withPublicFeedbacksOnly(self, value):
        self._withPublicFeedbacksOnly = value

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value):
        self._completed = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetDGSPurchaseCount, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSPurchaseCount, self).getData(key)             # calls 'BaseGet.getData()'