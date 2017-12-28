# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class EncodeQRCode(Parent):
    def __init__(self, qrCodeData=None, width=None, height=None):
        """
            Encodes a UTF-8 string to a base64-encoded jpeg. POST only.

            EncodeQRCode take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Encode_QR_Code

            REQUEST
            :param qrCodeData : is a UTF-8 text string to be encoded
            :param width : is the width of the output image (O)
            :param height : is the height of the output image (O)

            RESPONSE
            :return qrCodeBase64 : (S) is a base64 string encoding a jpeg image of the QR code
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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
        self._qrCodeData = qrCodeData
        self._width = width
        self._height = height

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["qrCodeData"] = self.qrCodeData
        if self.width:
            self.data["width"] = self.width
        if self.height:
            self.data["height"] = self.height

        super(EncodeQRCode, self).__init__(rt="encodeQRCode", data=self.data)

    @property
    def qrCodeBase64(self):
        return self._qrCodeBase64

    @qrCodeBase64.setter
    def qrCodeBase64(self, value):
        self._qrCodeBase64 = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def run(self):
        super(EncodeQRCode, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(EncodeQRCode, self).getData(key)  # calls 'BasePost.getData()'

