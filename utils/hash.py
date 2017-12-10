# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class Hash(Parent):

    def __init__(self, hashAlgorithm=2, secret=None, secretIsText=True):
        """
            Calculates the hash of a secret for use in phased transactions with voting model 5 (Vote By Secret).

            Hash take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Hash

            REQUEST
            :param hashAlgorithm : is the hash function used: 2 for SHA256, 3 for SHA3, 5 for SCRYPT, 6 for RIPEMD160,
                                    25 for Keccack25 and 62 for SHA256 followed by RIPEMD160, according to Get Constants
            :param secret : is a secret phrase in text form or hex string form
            :param secretIsText : is true if secret is text, false if it is a hex string (optional)

            Note: secret is converted from a hex string to a byte array, which is what the hash algorithm expects,
            unless secretIsText is true, in which case secret is first converted from text to a UTF-8 hex string as by Hex Convert.

            RESPONSE
            hash : (S) is the hash of the secret, in the form of a hex string
            requestProcessingTime : (N) is the API request processing time (in millisec)

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

        self.hashAlgorithm = hashAlgorithm
        self.secret = secret
        self.secretIsText = secretIsText

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["hashAlgorithm"] = self.hashAlgorithm
        self.data["secret"] = self.secret
        self.data["secretIsText"] = self.secretIsText


        super(Hash, self).__init__(rt = "hash", data=self.data)

    def run(self):
        super(Hash, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(Hash, self).getData(key)               # calls 'BaseGet.getData()'