# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetLastTrades(Parent):

    def __init__(self,assets=None, rb=None ):
        """
            Get asset information given multiple asset IDs

            GetLastTrades take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Last_Trades

            REQUEST
            :param assets : is array (A) of asset ID's (S) / Multiaccount parameters (3)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return trades : is an array (A) of trade objects (refer to Get Trades without name and decimals for details)
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

        self._assets = assets
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        for a in self.assets:
            self.data["asset"] = a

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetLastTrades, self).__init__(rt = "getLastTrades", data=self.data)

    @property
    def assets(self):
        return self._assets

    @assets.setter
    def assets(self, value):
        self._tassets = [None]*3
        for a in value[:3]:
            self.tassets.append(a)
        self._assets = self._tassetss

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value


    def run(self):
        super(GetLastTrades, self).run()                                # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetLastTrades, self).getData(key)                  # calls 'BaseGet.getData()'