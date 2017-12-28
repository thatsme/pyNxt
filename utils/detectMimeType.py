# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class DetectMimeType(Parent):
    def __init__(self, data=None, file=None, filename=None, isText=True):
        """
            DetectMimeType take a default 5 parameter as explained in NXT API Documentation

            Class is working with POST method only, and create a transaction, for more info about transactions please refer to

            https://nxtwiki.org/wiki/The_Nxt_API#Detect_Mime_Type

            REQUEST
            :param data : is the data (O)
            :param file : is the pathname of a data file to upload (optional if data provided)
            :param filename : is a filename to associate with data (optional if file uploaded in which case the uploaded filename is always used)
            :param isText : is false if data is a hex string (O)

            RESPONSE
            :return type : (S) is the mime type
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
        self._data = data
        self._file = file
        self._filename = filename
        self._isText = isText

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        if self.data:
            self.data["data"] = self.data
        if self.file:
            self.data["file"] = self.file
        if self.filename:
            self.data["filename"] = self.filename

        self.data["isText"] = self.isText

        super(DetectMimeType, self).__init__(rt="detectMimeType", data=self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    @property
    def isText(self):
        return self._isText

    @isText.setter
    def isText(self, value):
        self._isText = value

    def run(self):
        super(DetectMimeType, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(DetectMimeType, self).getData(key)  # calls 'BasePost.getData()'
