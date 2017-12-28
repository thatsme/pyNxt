# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAllExchanges(Parent):
    def __init__(self, timestamp=None, includeCurrencyInfo=False, ri=None, rb=None ):
        """
            Get all currency exchanges in reverse chronological order.

            GetAllExchanges take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_All_Exchanges

            REQUEST
            :param timestamp : is the earliest timestamp to retrieve (O)
            :param includeCurrencyInfo : is true to include some currency details (B) (O)
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
        self._timestamp = timestamp
        self._includeCurrencyInfo = includeCurrencyInfo
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["timestamp"] = self.timestamp
        if self.includeCurrencyInfo:
            self.data["includeCurrencyInfo"] = self.includeCurrencyInfo


        super(GetAllExchanges, self).__init__(rt="getAllExchanges", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def includeCurrencyInfo(self):
        return self._includeCurrencyInfo

    @includeCurrencyInfo.setter
    def includeCurrencyInfo(self, value):
        self._includeCurrencyInfo = value

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
        super(GetAllExchanges, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAllExchanges, self).getData(key)                           # calls 'BaseGet.getData()'
