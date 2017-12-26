# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountLessors(Parent):

    def __init__(self, account=None, height=None, rb=None):
        """
            Get the lessors to an accounts.

            GetAccountLedgerLessor take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Lessor

            REQUEST
            :param accounts : is the ledger ID
            :param height : is the height of the blockchain to determine the lessors (N) (O) ( default is last block)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return accountRS (S) is the Reed-Solomon address of the accounts
            :return accounts (S) is the accounts number
            :return height : is the the block height associated with the event (N)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return lessors : is an array (A) of lessor objects including the fields:
            > lessorRS (S)
            > lessor (S)
            > guaranteedBalanceNQT (S)
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
        self._height = height
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.height:
            self.data["height"] = self.height

        super(GetAccountLessors, self).__init__(rt = "getAccountLessors", data=self.data, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetAccountLessors, self).run()                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountLessors, self).getData(key)           # calls 'BaseGet.getData()'