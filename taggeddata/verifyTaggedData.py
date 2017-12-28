# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class VerifyTaggedData(Parent):

    def __init__(self, transaction=None, data=False, file=False, filename=None, name=None, description=None, tags=None, type=None, channel=None, isText=False, rb=None ):
        """
            Verify expired tagged data downloaded from another node, against the hash in the blockchain.

            VerifyTaggedData take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Verify_Tagged_Data

            REQUEST
            :param transaction : is the transaction ID of the tagged data (S)
            :param data : is the tagged data (O)
            :param file : is the pathname of a data file to upload (optional if data provided)
            :param filename
            :param name
            :param description
            :param tags
            :param type
            :param channel
            :param isText
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return verify : (B) is true if the hash of the provided data and metadata matches the hash in the blockchain
            :return hash : (S) is the hash of the tagged data
            :return lastBlock (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)
            :return version.TaggedDataUpload : (N) is 1, the version number

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
        self._transaction = transaction
        self._data = data
        self._file = file
        self._filename = filename
        self._name = name
        self._description = description
        self._tags = tags
        self._type = type
        self._channel = channel
        self._isText = isText
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        super(VerifyTaggedData, self).__init__(rt = "verifyTaggedData", data=self.data, rb=self.rb)

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, value):
        self._transaction = value

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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    @property
    def isText(self):
        return self._isText

    @isText.setter
    def isText(self, value):
        self._isText = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(VerifyTaggedData, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(VerifyTaggedData, self).getData(key)    # calls 'BaseGet.getData()'