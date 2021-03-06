# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountBlocks(Parent):

    def __init__(self, account=None, timestamp=0, includeTransactions=False, ri=None, rb=None):
        """
            GetAccountBlocks take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Blocks

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param timestamp : is the earliest block (in seconds since the genesis block) to retrieve (N) (O)
            :param includeTransactions : is true to retrieve transaction details, otherwise only transaction IDs are retrieved (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return blocks : is an array (A) of blocks (refer to Get Block for details)
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
        self._timestamp = timestamp
        self._includeTransactions = includeTransactions
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["timestamp"] = self.timestamp
        if self.includeTransactions:
            self.data["includeTransactions"] = self.includeTransactions

        super(GetAccountBlocks, self).__init__(rt = "getAccountBlocks", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def includeTransactions(self):
        return self._includeTransactions

    @includeTransactions.setter
    def includeTransactions(self, value):
        self._includeTransactions = value

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
        super(GetAccountBlocks, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountBlocks, self).getData(key)    # calls 'BaseGet.getData()'