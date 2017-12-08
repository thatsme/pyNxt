# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrencyAccountCount(Parent):
    def __init__(self, currency=None, height = None, requireBlock=None, requireLastBlock=None ):
        """
            Get the number of accounts that hold a given currency.

            GetCurrencyAccountCount take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currency_Account_Count

            REQUEST
            :param currency is the currency ID (S)
            :param height : is the blockchain height at which the response applies (optional, default is the current height)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

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
                (O) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        # Required parameters
        self.currency  = currency
        self.height = height
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["height"] = self.height

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetCurrencyAccountCount, self).__init__(rt="getCurrencyAccountCount", data=self.data)

    def run(self):
        super(GetCurrencyAccountCount, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetCurrencyAccountCount, self).getData(key)                           # calls 'BaseGet.getData()'
