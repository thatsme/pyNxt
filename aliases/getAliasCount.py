# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAliasCount(Parent):
    def __init__(self, account = None, rb=None ):
        """
            GetAliasCount take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Alias_Count

            REQUEST
            :param accounts : is the accounts
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return numberOfAliases : is the number of aliases owned by the accounts (N)
            :return lastBlock : is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return RequestProcessingTime (N) is the API request processing time (in millisec) (S)

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
        self._account = account
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["accounts"] = self.account

        super(GetAliasCount, self).__init__(rt="getAliasCount", data=self.data, rb=self.rb)

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
        super(GetAliasCount, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAliasCount, self).getData(key)                           # calls 'BaseGet.getData()'
