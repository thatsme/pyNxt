# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetSharedKey(Parent):

    def __init__(self, account=None, secretPhrase=None, nonce=None ):
        """
            Get the one-time shared key used for encryption of messages.

            GetSharedKey take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Shared_Key

            REQUEST
            :param account : (S) is the recipient account ID (R)
            :param secretPhrase : (S) is the secret phrase of the sender (R)
            :param nonce : (S) is the 32-byte pseudorandom nonce (R)

            RESPONSE
            :return sharedKey (S) is shared key as a hexadecimal string
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
        self._secretPhrase = secretPhrase
        self._nonce = nonce

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        self.data["secretPhrase"] = self.secretPhrase
        self.data["nonce"] = self.nonce

        super(GetSharedKey, self).__init__(rt = "getSharedKey", data=self.data)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def nonce(self):
        return self._nonce

    @nonce.setter
    def nonce(self, value):
        self._nonce = value

    def run(self):
        super(GetSharedKey, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetSharedKey, self).getData(key)             # calls 'BaseGet.getData()'