# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class SearchTaggedData(Parent):

    def __init__(self, query=None, tag=None, channel=None, account=None, includeData=False, ri=None, rb=None ):
        """
            Full text search on available tagged data name, description and tags; optionally filtered by tag,
            channel or uploading account; return in reverse relevance order.

            SearchTaggedData take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Search_Tagged_Data

            REQUEST
            :param query : is a full text query on the metadata fields name (S), description (S) and tags (S) in the standard Lucene syntax
            :param tag : is a word in the tags string (S) (O)
            :param channel : is a channel string (S) (O)
            :param account : is an account ID (S) (O)
            :param includeData : is true to include data (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return data : (A) is an array of tagged data objects (refer to Get Tagged Data with hash omitted for details)
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
        self._query = query
        self._tag = tag
        self._channel = channel
        self._account = account
        self._includeData = includeData
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        super(SearchTaggedData, self).__init__(rt = "searchTaggedData", data=self.data, rb=self.rb)

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def includeData(self):
        return self._includeData

    @includeData.setter
    def includeData(self, value):
        self._includeData = value

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
        super(SearchTaggedData, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(SearchTaggedData, self).getData(key)    # calls 'BaseGet.getData()'