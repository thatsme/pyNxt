# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetUnconfirmedTransactions(Parent):

    def __init__(self,accounts=None, ri=None, rb=None ):
        """
            Get a list of unconfirmed transaction IDs associated with an account.

            GetUnconfirmedTransactions take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Unconfirmed_Transactions

            REQUEST
            :param accounts : is array (A) of accounts ID's (S) / Multiaccount parameters (3)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return unconfirmedTransactions : (A) is an array of unconfirmed transactions (refer to Get Transaction for details)
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
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
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        for a in self.accounts:
            self.data["accounts"] = a

        super(GetUnconfirmedTransactions, self).__init__(rt = "getUnconfirmedTransactions", data=self.data, ri=self.ri, rb=self.rb)

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
        super(GetUnconfirmedTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetUnconfirmedTransactions, self).getData(key)    # calls 'BaseGet.getData()'