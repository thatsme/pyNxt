# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class DecodeHallmark(Parent):

    def __init__(self, hallmark=None):
        """
            Decode a node hallmark.

            DecodeHallmark take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Decode_Hallmark

            REQUEST
            :param hallmark is the hallmark value

            RESPONSE
            :return valid : (B) is true if host is less than 100 characters, weight > 0 and the embedded signature is verified
            :return weight : (N) is the weight assigned to the hallmark
            :return host : (S) is the IP address or domain name associated with the hallmark
            :return account : (S) is the account number associated with the hallmark
            :return accountRS : (S) is the Reed-Solomon address of the account
            :return date : (S) is the date the hallmark was created, in YYYY-MM-DD format
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

        self._hallmark = hallmark

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["hallmark"] = self.hallmark

        super(DecodeHallmark, self).__init__(rt = "decodeHallmark", data=self.data)

    @property
    def hallmark(self):
        return self._hallmark

    @hallmark.setter
    def hallmark(self, value):
        self._hallmark = value

    def run(self):
        super(DecodeHallmark, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(DecodeHallmark, self).getData(key)               # calls 'BaseGet.getData()'