# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAllCurrencies(Parent):
    def __init__(self, includeCounts=False, ri=None, rb=None ):
        """
            Get all currencies in reverse creation order.

            GetAllCurrencies take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_All_Currencies

            REQUEST
            :param includeCounts : is true to include numberOf... fields (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return assets : is an array (A) of asset objects (refer to Get Asset)
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
        self._includeCounts = includeCounts
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        if self.includeCounts:
            self.data["includeCounts"] = self.includeCounts

        super(GetAllCurrencies, self).__init__(rt="getAllCurrencies", data=self.data, ri=self.ri, rb=self.rb)

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
        super(GetAllCurrencies, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAllCurrencies, self).getData(key)                           # calls 'BaseGet.getData()'
