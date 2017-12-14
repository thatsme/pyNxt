# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSExpiredPurchases(Parent):

    def __init__(self, seller=None, ri=None, rb=None ):
        """
            Get purchase orders which have expired without being delivered, given a seller ID, in reverse chronological order.

            GetDGSExpiredPurchases take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Expired_Purchases

            REQUEST
            :param seller : is the accounts ID of the product seller (S)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return purchases (A) is an array of purchase orders (refer to Get DGS Purchase for details)
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
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["seller"] = seller

        super(GetDGSExpiredPurchases, self).__init__(rt = "getDGSExpiredPurchases", data=self.data, ri = self.ri, rb=self.rb)

    def run(self):
        super(GetDGSExpiredPurchases, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSExpiredPurchases, self).getData(key)             # calls 'BaseGet.getData()'