# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class FullHashToId(Parent):

    def __init__(self, fullHash=False):
        """
            Converts a full hash to an ID.

            FullHashToId take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Full_Hash_To_Id

            REQUEST
            :param fullHash : is the full hash 64-digit (32-byte) hex string

            RESPONSE
            :return stringId : (S) is the ID corresponding to the hash, in the form of an decimal string
            :return longId : (S) is the signed long integer (8-bytes) representation of the ID used internally, returned as a string
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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

        self._fullHash = fullHash

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["fullHash"] = self.fullHash

        super(FullHashToId, self).__init__(rt = "fullHashToId", data=self.data)

    @property
    def fullHash(self):
        return self._fullHash

    @fullHash.setter
    def fullHash(self, value):
        self._fullHash = value

    def run(self):
        super(FullHashToId, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(FullHashToId, self).getData(key)               # calls 'BaseGet.getData()'