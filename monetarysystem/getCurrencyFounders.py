# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrencyFounders(Parent):
    def __init__(self, currency=None, account = None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get a reservable currency's founders.

            GetCurrencyFounders take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currency_Founders

            REQUEST
            :param currency : is the currency ID (S)
            :param account : is an account ID (S)(O)
            :param firstIndex is a zero-based index to the first account to retrieve (O)
            :param lastIndex is a zero-based index to the last account to retrieve (O)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return founders : (A) is an array of founder objects each of which has the following fields:
            :return > accountRS (S) is the Reed-Solomon address of the founding account
            :return > amountPerUnitNQT (S) is the amount (in NQT per QNT of reserveSupply) reserved by the founder
            :return > currency (S) is the currency ID
            :return > account (S) is the founding account number
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
        self.account = account
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["account"] = self.account

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex

        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetCurrencyFounders, self).__init__(rt="getCurrencyFounders", data=self.data)

    def run(self):
        super(GetCurrencyFounders, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetCurrencyFounders, self).getData(key)                           # calls 'BaseGet.getData()'
