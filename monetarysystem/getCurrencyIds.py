# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrencyIds(Parent):
    def __init__(self, ri=None, rb=None ):
        """
            Get all currency IDs in reverse chronological creation order.

            GetCurrencyIds take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currency_Ids

            REQUEST
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return currencyIds(A) is an array of currency IDs
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
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        super(GetCurrencyIds, self).__init__(rt="getCurrencyIds", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetCurrencyIds, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetCurrencyIds, self).getData(key)                           # calls 'BaseGet.getData()'
