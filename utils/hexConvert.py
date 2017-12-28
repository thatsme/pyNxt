# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class HexConvert(Parent):

    def __init__(self, string=None):
        """
            Converts a text string into a UTF-8 hex string and if the text input is already a hex string, also into text.

            HexConvert take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Hex_Convert

            REQUEST
            :param string : is a text string, possibly a hex string

            RESPONSE
            :return binary : (S) is the converted UTF-8 hex string
            :return text : (S) is a text string converted from string if it is a valid UTF-8 hex string
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

        self._string = string

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["string"] = self.string

        super(HexConvert, self).__init__(rt = "hexConvert", data=self.data)

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value

    def run(self):
        super(HexConvert, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(HexConvert, self).getData(key)               # calls 'BaseGet.getData()'