# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAliases(Parent):
    def __init__(self, account = None, timestamp=0, ri=None, rb=None ):
        """
            Get information on aliases owned by a given accounts in alias name order.

            GetAliases take a default 1/2 parameter as explained in NXT API Documentation

            API is working with POST method only , and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Aliases

            REQUEST
            :param accounts : is the ID of the accounts that owns the aliases (S)
            :param timestamp : is the earliest creation time (in seconds since the genesis block) of the aliases (S) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return aliases : is an array (A) of alias objects (refer to Get Alias for details)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)

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
        self._timestamp = timestamp
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["accounts"] = self.account
        self.data["timestamp"] = self.timestamp

        super(GetAliases, self).__init__(rt="getAliases", data=self.data, ri=self.ri, rb=self.rb)

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
        super(GetAliases, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAliases, self).getData(key)                           # calls 'BaseGet.getData()'
