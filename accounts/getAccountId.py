# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class GetAccountId(Parent):

    def __init__(self, publicKey=None, secretPhrase=None):
        """
            Get an accounts ID given a secret passphrase or public key. POST only.

            GetAccountId take a default 1 parameter as explained in NXT API Documentation
            Class is working with POST method only

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Id

            REQUEST
            secretPhrase : is the secret passphrase of the accounts (S) (O)
            publicKey : is the public key of the accounts (S) (optional if secretPhrase provided)

            RESPONSE
            accountRS : is the Reed-Solomon address of the accounts (S)
            publicKey : is the public key of the accounts (S)
            accounts : is the accounts number (S)
            requestProcessingTime : is the API request processing time (N) (in millisec)

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
                (O) Object
                >   Array Element
                (WP) Wrapper specific parameter

        """

        self.publicKey = publicKey
        self.secretPhrase = secretPhrase

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["publicKey"] = self.publicKey
        self.data["secretPhrase"] = self.secretPhrase

        super(GetAccountId, self).__init__(rt = "getAccountId", data=self.data)

    def run(self):
        super(GetAccountId, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountId, self).getData(key)       # calls 'BaseGet.getData()'