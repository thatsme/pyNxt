# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrencies(Parent):
    def __init__(self, currencies=None, includeCounts=False, rb=None ):
        """
            Get currencies given multiple currency IDs.

            GetCurrencies take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currencies

            REQUEST
            :param currencies : is one of multiple currency IDs
            :param includeCounts : (B) is true to include numberOf... fields (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return currencies (A) is an array of currency objects (refer to Get Currency for details)
            :return lastBlock (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
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
        self._currencies = currencies
        self._includeCounts = includeCounts
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["currencies"] = self.currencies
        self.data["includeCounts"] = self.includeCounts

        super(GetCurrencies, self).__init__(rt="getCurrencies", data=self.data, rb=self.rb)

    @property
    def currencies(self):
        return self._currencies

    @currencies.setter
    def currencies(self, value):
        self._tcurries = [None]*3
        for a in value[:3]:
            self._tcurries.append(a)
        self._currencies = self._tcurries

    @property
    def includeCounts(self):
        return self._includeCounts

    @includeCounts.setter
    def includeCounts(self, value):
        self._includeCounts = value

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
        super(GetCurrencies, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetCurrencies, self).getData(key)                           # calls 'BaseGet.getData()'
