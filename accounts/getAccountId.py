# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class GetAccountId(Parent):

    def __init__(self, publicKey=None, secretPhrase=None):
        """
            Get an accounts ID given a secret passphrase or public key. POST only.

            GetAccountId take a default 1 parameter as explained in NXT API Documentation
            API is working with POST method only

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Id

            REQUEST
            :param secretPhrase : is the secret passphrase of the accounts (S) (O)
            :param publicKey : is the public key of the accounts (S) (optional if secretPhrase provided)

            RESPONSE
            :return accountRS : is the Reed-Solomon address of the accounts (S)
            :return publicKey : is the public key of the accounts (S)
            :return accounts : is the accounts number (S)
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

        self._publicKey = publicKey
        self._secretPhrase = secretPhrase

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["publicKey"] = self.publicKey
        self.data["secretPhrase"] = self.secretPhrase

        super(GetAccountId, self).__init__(rt = "getAccountId", data=self.data)

    @property
    def publicKey(self):
        return self._publicKey

    @publicKey.setter
    def publicKey(self, value):
        self._publicKey = value

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    def run(self):
        super(GetAccountId, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountId, self).getData(key)       # calls 'BaseGet.getData()'