# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class CanDeleteCurrency(Parent):

    def __init__(self, account=None, currency=None, rb=None ):
        """
            Decrypt an AES-encrypted message.

            CanDeleteCurrency take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Can_Delete_Currency

            REQUEST
            :param account : is the account ID (S)
            :param currency : is the currency ID (S)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return canDelete (B) is true if the currency can be deleted, false otherwise
            :return lastBlock (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
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
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["currency"] = self.currency

        super(CanDeleteCurrency, self).__init__(rt = "canDeleteCurrency", data=self.data, rb=self.rb)

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
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(CanDeleteCurrency, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(CanDeleteCurrency, self).getData(key)             # calls 'BaseGet.getData()'