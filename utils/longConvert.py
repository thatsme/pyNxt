# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class LongConvert(Parent):

    def __init__(self, id=None):
        """
            Converts a text string into a UTF-8 hex string and if the text input is already a hex string, also into text.

            LongConvert take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Long_Convert

            REQUEST
            :param id : is a numerical ID, in decimal form but equivalent to an 8-byte unsigned integer as produced by SHA-256 hashing

            RESPONSE
            :return stringId : (S) is the numerical ID
            :return longId : (S) is the signed long integer (8-bytes) representation of the ID used internally, returned as a string
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

            Note: Java does not support unsigned integers, so any unsigned ID (such as a block ID) visible in the
            NRS client is represented internally as a signed integer.

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

        self._id = id

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["id"] = self.id


        super(LongConvert, self).__init__(rt = "longConvert", data=self.data)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def run(self):
        super(LongConvert, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(LongConvert, self).getData(key)               # calls 'BaseGet.getData()'