# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountPhasedTransactionCount(Parent):

    def __init__(self, account=None, rb=None):
        """
            Get the number of pending phased transactions associated with an accounts given the accounts ID.

            GetAccountPhasedTransactionCount take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Phased_Transaction_Count

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return numberOfPhasedTransactions (N) is the number of pending phased transactions
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
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account

        super(GetAccountPhasedTransactionCount, self).__init__(rt = "getAccountPhasedTransactionCount", data=self.data, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetAccountPhasedTransactionCount, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountPhasedTransactionCount, self).getData(key)       # calls 'BaseGet.getData()'