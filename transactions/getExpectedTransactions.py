# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetExpectedTransactions(Parent):

    def __init__(self,accounts=None, rb=None ):
        """
            Returns the non-phased unconfirmed transactions expected to be included in the next block (only),
            plus the phased transactions scheduled to finish in that block (whether approved or not).

            GetExpectedTransactions take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Expected_Transactions

            REQUEST
            :param accounts : is array (A) of accounts ID's (S) / Multiaccount parameters (3)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return expectedTransactions : (A) is an array of expected transactions (refer to Get Transaction for details)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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

        self._accounts = accounts
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        for a in self.accounts:
            self.data["accounts"] = a

        super(GetExpectedTransactions, self).__init__(rt = "getExpectedTransactions", data=self.data, rb=self.rb)

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, value):
        self._taccounts = [None]*3
        for a in value[:3]:
            self.taccounts.append(a)
        self._accounts = self._taccounts

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetExpectedTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetExpectedTransactions, self).getData(key)    # calls 'BaseGet.getData()'