# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrencyFounders(Parent):
    def __init__(self, currency=None, account = None, ri=None, rb=None ):
        """
            Get a reservable currency's founders.

            GetCurrencyFounders take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currency_Founders

            REQUEST
            :param currency : is the currency ID (S)
            :param account : is an account ID (S)(O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        # Required parameters
        self._currency  = currency
        self._account = account
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["account"] = self.account

        super(GetCurrencyFounders, self).__init__(rt="getCurrencyFounders", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

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
        super(GetCurrencyFounders, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetCurrencyFounders, self).getData(key)                           # calls 'BaseGet.getData()'
