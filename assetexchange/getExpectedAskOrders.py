# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetExpectedAskOrders(Parent):
    def __init__(self, asset=None, sortByPrice=False, showExpectedCancellations=False, ri=None, rb=None ):
        """
            Get bid/ask orders given an asset ID, in order of decreasing bid price or increasing ask price
            (if sortByPrice is true for expected orders, otherwise in the expected order of execution).

            GetExpectedAskOrders take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Expected_Ask_Orders

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
        self._asset = asset
        self._sortByPrice = sortByPrice
        self._showExpectedCancellations = showExpectedCancellations
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["asset"] = self.asset
        if self.sortByPrice:
            self.data["sortByPrice"] = self.sortByPrice
        if self.showExpectedCancellations:
            self.data["showExpectedCancellations"] = self.showExpectedCancellations

        super(GetExpectedAskOrders, self).__init__(rt="getExpectedAskOrders", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, value):
        self._asset = value

    @property
    def sortByPrice(self):
        return self._sortByPrice

    @sortByPrice.setter
    def sortByPrice(self, value):
        self._sortByPrice = value

    @property
    def showExpectedCancellations(self):
        return self._showExpectedCancellations

    @showExpectedCancellations.setter
    def showExpectedCancellations(self, value):
        self._showExpectedCancellations = value

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
        super(GetExpectedAskOrders, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetExpectedAskOrders, self).getData(key)                           # calls 'BaseGet.getData()'
