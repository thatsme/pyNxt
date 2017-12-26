# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountCurrencies(Parent):

    def __init__(self, account=None, currency=None, height=None, includeCurrencyInfo=False, rb=None):
        """
            GetAccountCurrencies take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Currencies

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param currency : is a currency ID filter (S) (O)
            :param height : is the blockchain height at which the response applies (N) (O) (default is the current height)
            :param includeCurrencyInfo : is true if several currency information properties is to be included (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return accountCurrencies : is an array (A)  of currency objects with the following fields:
            > code (S) is the currency code
            > unconfirmedUnits (S) is the amount of unconfirmed currency units (in QNT)
            > decimals (N) is the number of currency decimal places
            > name (S) is the currency name
            > currency (S) is the currency ID
            > units (S) is the amount of currency (in QNT)
            > issuanceHeight (N) is the blockchain height of issuance for a reservable currency
            > type (N) is the currency type bitmask (refer to Get Currency)
            > issuerAccountRS (S) is the Reed-Solomon address of the issuer accounts
            > issuerAccount (S) is the issuer accounts ID
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

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

        self._account = account
        self._currency = currency
        self._height = height
        self._includeCurrencyInfo = includeCurrencyInfo
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.currency:
            self.data["currency"] = self.currency
        if self.includeCurrencyInfo:
            self.data["includeCurrencyInfo"] = self.includeCurrencyInfo
        if self.height:
            self.data["height"] = self.height

        super(GetAccountCurrencies, self).__init__(rt = "getAccountCurrencies", data=self.data, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

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
    def includeCurrencyInfo(self):
        return self._includeCurrencyInfo

    @includeCurrencyInfo.setter
    def includeCurrencyInfo(self, value):
        self._includeCurrencyInfo = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetAccountCurrencies, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountCurrencies, self).getData(key)               # calls 'BaseGet.getData()'