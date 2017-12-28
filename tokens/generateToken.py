# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class GenerateToken(Parent):
    def __init__(self, website=None, secretPhrase=None):
        """
            Generate a token. POST only.

            GenerateToken take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Generate_Token

            REQUEST
            :param secretPhrase : is the passphrase of the account generating the token
            :param website : is a web site URL for which authorization should be granted, or general text to be digitally signed

            Note: website is typically a URL (with the leading http:// unnecessary) that an account owner signs with his secretPhrase
            (private key) to bind the account to the URL, but website can be any text that the owner wishes to sign.

            RESPONSE
            :return token (S) is a 160 character string representing the 100-byte token which consists of a 32-byte public key, a 4-byte timestamp, and a 64-byte signature
            :return account (S) is the account number corresponding to secretPhrase
            :return accountRS (S) is the Reed-Solomon address of the account
            :return timestamp (N) is the time (in seconds since the genesis block) that the token was generated
            :return valid (B) is true if token is valid, false otherwise
            :return requestProcessingTime (N) is the API request processing time (in millisec)

            Legenda
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
        self._secretPhrase = secretPhrase
        self._website = website

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["website"] = self.website
        self.data["secretPhrase"] = self.secretPhrase

        super(GenerateToken, self).__init__(rt="generateToken", data=self.data)

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, value):
        self._website = value

    def run(self):
        super(GenerateToken, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GenerateToken, self).getData(key)  # calls 'BasePost.getData()'

