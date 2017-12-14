# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSPendingPurchases  (Parent):

    def __init__(self, seller=None, ri=None, rb=None ):
        """
            Get pending purchase orders given a seller ID in reverse chronological order.

            GetDGSPendingPurchases take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Pending_Purchases

            REQUEST
            :param seller : is the accounts ID of the seller
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            Note: If none of the optional parameters are specified, all in-stock products in the blockchain
            are retrieved at once, which may take a long time.

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
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["seller"] = seller

        super(GetDGSPendingPurchases, self).__init__(rt = "getDGSPendingPurchases", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetDGSPendingPurchases, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSPendingPurchases, self).getData(key)             # calls 'BaseGet.getData()'