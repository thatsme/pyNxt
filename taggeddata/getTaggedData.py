# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetTaggedData(Parent):

    def __init__(self, transaction=None, includeData=False, retrieve=False, ri=None, rb=None ):
        """
            Get available tagged data given a transaction ID.

            GetTaggedData take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Tagged_Data

            REQUEST
            :param transaction : is the transaction ID (S)
            :param includeData : is true to include data (B) (O)
            :param retrieve : is true to retrieve pruned data from other nodes if not available (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return data : (S) is the tagged data
            :return hash : (S) is the hash of the tagged data
            :return filename : (S) is the metadata filename field
            :return name : (S) is the metadata name field
            :return description : (S) is the metadata description field
            :return tags : (S) is the metadata tags field
            :return parsedTags : (A) is an array of tag words (S) parsed from tags
            :return type : (S) is the metadata type field
            :return channel : (S) is the metadata channel field
            :return isText : (B) is the metadata isText field
            :return account : (S) is the number of the account that originally uploaded the tagged data
            :return accountRS : (S) is the Reed-Solomon address of the uploading account
            :return transaction : (S) is the transaction ID
            :return transactionTimestamp : (N) is the transaction timestamp (in seconds since the genesis block)
            :return blockTimestamp : (N) is the block timestamp (in seconds since the genesis block)
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
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
        self._transaction = transaction
        self._includeData = includeData
        self._retrieve = retrieve
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        super(GetTaggedData, self).__init__(rt = "getTaggedData", data=self.data, rb=self.rb)

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, value):
        self._transaction = value

    @property
    def includeData(self):
        return self._includeData

    @includeData.setter
    def includeData(self, value):
        self._includeData = value

    @property
    def retrieve(self):
        return self._retrieve

    @retrieve.setter
    def retrieve(self, value):
        self._retrieve = value

    @property
    def ri(self):
        return self._ri

    @ri.setter
    def ri(self, value):
        self._ri = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetTaggedData, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetTaggedData, self).getData(key)    # calls 'BaseGet.getData()'