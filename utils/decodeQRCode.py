# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class DecodeQRCode(Parent):
    def __init__(self, qrCodeBase64=None):
        """
            Decodes a base64-encoded jpeg to a UTF-8 string. POST only.

            DecodeQRCode take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Decode_QR_Code

            REQUEST
            :param qrCodeBase64 is a base64-encoded jpeg string to be decoded

            RESPONSE
            :return qrCodeData : (S) is a UTF-8 string containing the decoded data from the base64 string
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
        self.qrCodeBase64 = qrCodeBase64

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["qrCodeBase64"] = self.qrCodeBase64

        super(DecodeQRCode, self).__init__(rt="decodeQRCode", data=self.data)

    def run(self):
        super(DecodeQRCode, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(DecodeQRCode, self).getData(key)  # calls 'BasePost.getData()'

