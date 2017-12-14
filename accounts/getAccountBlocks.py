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

        self.account = account
        self.timestamp = timestamp
        self.includeTransactions = includeTransactions
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["timestamp"] = self.timestamp
        if self.includeTransactions:
            self.data["includeTransactions"] = self.includeTransactions

        super(GetAccountBlocks, self).__init__(rt = "getAccountBlocks", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetAccountBlocks, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountBlocks, self).getData(key)    # calls 'BaseGet.getData()'