# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrencyAccounts(Parent):
    def __init__(self, currency=None, height = None, ri=None, rb=None ):
        """
            Get the accounts that hold a given currency in reverse units order.

            GetCurrencyAccounts take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currency_Accounts

            REQUEST
            :param currency is the currency ID (S)
            :param height : is the blockchain height at which the response applies (optional, default is the current height)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return accountCurrencies : (A) is an array of account objects with the following fields:
            :return > unconfirmedUnits : (S) is the amount of unconfirmed currency units (in QNT)
            :return > accountRS : (S) is the Reed-Solomon address of the account
            :return > currency : (S) is the currency ID
            :return > units : (S) is the amount of currency (in QNT)
            :return > account : (S) is the account number
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
        self.currency  = currency
        self.height = height
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["height"] = self.height

        super(GetCurrencyAccounts, self).__init__(rt="getCurrencyAccounts", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetCurrencyAccounts, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetCurrencyAccounts, self).getData(key)                           # calls 'BaseGet.getData()'
