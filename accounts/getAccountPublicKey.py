# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountPublicKey(Parent):

    def __init__(self, account=None, rb=None):
        """
            Get the public key associated with an accounts ID.

            GetAccountPublicKey take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Public_Key

            REQUEST
            :param accounts : is the accounts ID (S)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return publicKey : is the 32-byte public key associated with the accounts, returned as a hex string (S)
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

        super(GetAccountPublicKey, self).__init__(rt = "getAccountPublicKey", data=self.data, rb=self.rb)

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
        super(GetAccountPublicKey, self).run()                  # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountPublicKey, self).getData(key)    # calls 'BaseGet.getData()'