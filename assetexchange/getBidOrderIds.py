# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBidOrderIds(Parent):
    def __init__(self, asset=None, ri=None, rb=None ):
        """
            Get bid/ask order IDs given an asset ID, in order of decreasing bid price or increasing ask price.

            GetBidOrderIds take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Bid_Order_Ids

            REQUEST
            :param asset : is the asset ID (S)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return bidOrderIds : is an array (A) of order IDs
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
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["asset"] = self.asset

        super(GetBidOrderIds, self).__init__(rt="getBidOrderIds", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, value):
        self._asset = value

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
        super(GetBidOrderIds, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBidOrderIds, self).getData(key)                           # calls 'BaseGet.getData()'
