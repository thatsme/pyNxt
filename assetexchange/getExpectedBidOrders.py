# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetExpectedBidOrders(Parent):
    def __init__(self, asset=None, sortByPrice=False, showExpectedCancellations=False, ri=None, rb=None ):
        """
            Get bid/ask orders given an asset ID, in order of decreasing bid price or increasing ask price
            (if sortByPrice is true for expected orders, otherwise in the expected order of execution).

            GetExpectedBodOrders take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Expected_Bid_Orders

            REQUEST
            :param asset : is the asset ID (S)
            :param sortByPrice : is true to sort by price (optional, applies only to expected orders,
                        which are returned in expected order of execution by default) (B)
            :param showExpectedCancellations : is true to include orders that are expected to be cancelled in the next block,
                        based on the content of the unconfirmed transactions pool and the phased transactions
                        expected to finish in the next block (optional, does not apply to expected orders) (B)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return askOrders : is an array (A) of order objects (refer to Get Order for details) with the following additional field only for an expected order:
            > phased (B) is true if the order is phased, false otherwise
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)

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

        # Required parameters
        self.asset = asset
        self.sortByPrice = sortByPrice
        self.showExpectedCancellations = showExpectedCancellations
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["asset"] = self.asset
        if self.sortByPrice:
            self.data["sortByPrice"] = self.sortByPrice
        if self.showExpectedCancellations:
            self.data["showExpectedCancellations"] = self.showExpectedCancellations

        super(GetExpectedBidOrders, self).__init__(rt="getExpectedBidOrders", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetExpectedBidOrders, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetExpectedBidOrders, self).getData(key)                           # calls 'BaseGet.getData()'
