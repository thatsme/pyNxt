# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class GenerateFileToken(Parent):
    def __init__(self, file=None, secretPhrase=None):
        """
            Generate a file token. POST only.

            GenerateToken take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Generate_File_Token

            REQUEST
            :param secretPhrase : is the passphrase of the account generating the token
            :param file is the path to the file to be signed

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
        self.secretPhrase = secretPhrase
        self.file = file

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["file"] = self.file
        self.data["secretPhrase"] = self.secretPhrase

        super(GenerateFileToken, self).__init__(rt="generateFileToken", data=self.data)

    def run(self):
        super(GenerateFileToken, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GenerateFileToken, self).getData(key)  # calls 'BasePost.getData()'

