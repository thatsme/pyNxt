# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountBlockCount(Parent):

    def __init__(self, account=None, rb=None):
        """
            GetAccountBlockCount take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Block_Count

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return numberOfBlocks : is the number of blocks forged by the accounts (N)
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
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account

        super(GetAccountBlockCount, self).__init__(rt = "getAccountBlockCount", data=self.data, rb=self.rb)

    def run(self):
        super(GetAccountBlockCount, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountBlockCount, self).getData(key)               # calls 'BaseGet.getData()'