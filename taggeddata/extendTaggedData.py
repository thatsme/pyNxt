# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class ExtendTaggedData(Parent):
    def __init__(self, transaction=None, data=None, file=None, filename=None, name=None, description=None, tags=None, type=None, channel=None, isText=None, secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing=None, message=None, rec=None ):
        """
            ExtendTaggedData take a default 5 parameter as explained in NXT API Documentation

            API is working with POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Response

            https://nxtwiki.org/wiki/The_Nxt_API#Extend_Tagged_Data

            REQUEST
            :param transaction : is the transaction ID of the tagged data
            :param data : is the tagged data (O)
            :param file : is the pathname of a data file to upload (optional if data provided)
            :param filename
            :param name
            :param description
            :param tags
            :param type
            :param channel
            :param isText
            :param secretPhrase * : secret Phrase of accounts  ( required or at least ** )
            :param publicKey ** : publicKey of accounts ( does not get in broadcast ) ( required or at least *)
            :param feeNQT : fee for sending transaction if 0 minimum is set ( 100000000 NQT )
            :param deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            :param referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            :param broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            :param phasing : phasing object ( check base/Phasing.py ) (WP)
            :param message : message object ( check base/message.py ) (WP)
            :param rec : rec object ( check base/Rec.py) (WP)

            Note: The data and metadata (filename, name, description, tags, type, channel and isText) parameters can be
            omitted if the tagged data has not yet expired; otherwise, the tagged data can be restored to the blockchain
            only if these fields have exactly the same values as when the data was uploaded (refer to Upload Tagged Data
            https://nxtwiki.org/wiki/The_Nxt_API#Upload_Tagged_Data ).

            Note: Anyone can submit an extension, not only the original uploader. Each extend transaction increases
            the expiration deadline by two weeks (24 hours on Testnet). Extending an existing tagged data from another
            account does not change the original submitter account ID by which it is indexed and searchable.

            RESPONSE (Create transaction response)

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

        self._publicKey = publicKey
        self._secretPhrase = secretPhrase
        self._feeNQT = feeNQT
        self._deadline = deadline

        # Optional parameters
        self._referencedTransactionFullHash = referencedTransactionFullHash
        self._broadcast = broadcast

        self._phasing = phasing
        self._message = message
        self._rec = rec

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["transaction"] = self.transaction
        if self.data:
            self.data["data"] = self.data
        if self.file:
            self.data["file"] = self.file
        if self.filename:
            self.data["filename"] = self.filename
        if self.name:
            self.data["name"] = self.name
        if self.description:
            self.data["description"] = self.description
        if self.tags:
            self.data["tags"] = self.tags
        if self.type:
            self.data["type"] = self.type
        if self.channel:
            self.data["channel"] = self.channel
        if self.isText:
            self.data["isText"] = self.isText

        if publicKey:
            self.data["publicKey"] = self.publicKey
        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline
        if self.referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash
        if self.broadcast:
            self.data["broadcast"] = self.broadcast

        super(ExtendTaggedData, self).__init__(rt="extendTaggedData", data=self.data, phasing=self.phasing, message=self.message)

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
    def publicKey(self):
        return self._publicKey

    @publicKey.setter
    def publicKey(self, value):
        self._publicKey = value

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def referencedTransactionFullHash(self):
        return self._referencedTransactionFullHash

    @referencedTransactionFullHash.setter
    def referencedTransactionFullHash(self, value):
        self._referencedTransactionFullHash = value

    @property
    def broadcast(self):
        return self._broadcast

    @broadcast.setter
    def broadcast(self, value):
        self._broadcast = value

    @property
    def feeNQT(self):
        return self._feeNQT

    @feeNQT.setter
    def feeNQT(self, value):
        if value == 0:
            self._feeNQT = 100000000
        else:
            self._feeNQT = value

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        if value == 0:
            self._deadline = 60
        else:
            self._deadline = value

    @property
    def phasing(self):
        return self._phasing

    @phasing.setter
    def phasing(self, value):
        self._phasing = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def rec(self):
        return self._rec

    @rec.setter
    def rec(self, value):
        self._rec = value

    def run(self):
        super(ExtendTaggedData, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(ExtendTaggedData, self).getData(key)  # calls 'BasePost.getData()'
