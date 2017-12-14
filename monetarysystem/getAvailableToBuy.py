# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAvailableToBuy(Parent):
    def __init__(self, currency=None, unit=0, rb=None ):
        """
            Calculates the rate required in order to completely fill an exchange request.

            GetAvailableToBuy take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Available_To_Buy

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
        self.currency = currency
        self.unit = unit
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["currency"] = self.currency
        self.data["unit"] = self.unit

        super(GetAvailableToBuy, self).__init__(rt="getAvailableToBuy", data=self.data, rb=self.rb)

    def run(self):
        super(GetAvailableToBuy, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAvailableToBuy, self).getData(key)                           # calls 'BaseGet.getData()'
