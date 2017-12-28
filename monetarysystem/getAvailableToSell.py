# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAvailableToSell(Parent):
    def __init__(self, currency=None, unit=0, rb=None ):
        """
            Calculates the rate required in order to completely fill an exchange request.

            GetAvailableToSell take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Available_To_Sell

            REQUEST
            :param currency : is the currency ID (S)
            :param units : is the number of units to buy (N)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return amountNQT : (S) is the total amount needed to fill the exchange request
            :return units : (S) is the number of units
            :return rateNQT : (S) is the rate for the currency units
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
        self._currency = currency
        self._unit = unit
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["currency"] = self.currency
        self.data["unit"] = self.unit

        super(GetAvailableToSell, self).__init__(rt="getAvailableToSell", data=self.data, rb=self.rb)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetAvailableToSell, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAvailableToSell, self).getData(key)                           # calls 'BaseGet.getData()'
