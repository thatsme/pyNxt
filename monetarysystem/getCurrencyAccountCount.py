# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrencyAccountCount(Parent):
    def __init__(self, currency=None, height = None, rb=None ):
        """
            Get the number of accounts that hold a given currency.

            GetCurrencyAccountCount take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currency_Account_Count

            REQUEST
            :param currency is the currency ID (S)
            :param height : is the blockchain height at which the response applies (optional, default is the current height)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return numberOfAccounts : (N) is the number of accounts that hold the currency
            :return requestProcessingTime : (N) is the API request processing time (in millisec)
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)

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
        self._currency  = currency
        self._height = height
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["height"] = self.height

        super(GetCurrencyAccountCount, self).__init__(rt="getCurrencyAccountCount", data=self.data, rb=self.rb)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetCurrencyAccountCount, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetCurrencyAccountCount, self).getData(key)                           # calls 'BaseGet.getData()'
