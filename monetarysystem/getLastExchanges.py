# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetLastExchanges(Parent):
    def __init__(self, currencies=None, rb=None ):
        """
            Get the last exchange of each of multiple currencies.

            GetLastExchanges take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Last_Exchanges

            REQUEST
            :param currencies : is one of multiple currency IDs
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return exchanges : (A) is an array of exchange objects
                        (refer to Get Exchanges without name, decimals, code, issuanceHeight, type, issuerAccountRS and issuerAccount for details)
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
        self.currencies = [None]*3
        for a in currencies[:3]:
            self.currencies.append(a)

        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["currencies"] = self.currencies

        super(GetLastExchanges, self).__init__(rt="getLastExchanges", data=self.data, rb=self.rb)

    def run(self):
        super(GetLastExchanges, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetLastExchanges, self).getData(key)                           # calls 'BaseGet.getData()'
