# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class SearchPolls(Parent):

    def __init__(self, query=None, includeFinished=False, ri=None, rb=None):
        """
            Search for poll details given a name/description query string.

            SearchPolls take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Search_Polls

            REQUEST
            :param query : is a full text query on the poll fields name (S) and description (S) in the standard Lucene syntax (O)
            :param includeFinished : is true to include completed polls (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return polls : (A) is an array of polls (refer to Get Poll for details)
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
        self._includeFinished = includeFinished
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["query"] = self.query
        self.data["includeFinished"] = self.includeFinished

        super(SearchPolls, self).__init__(rt = "searchPolls", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value

    @property
    def includeFinished(self):
        return self._includeFinished

    @includeFinished.setter
    def includeFinished(self, value):
        self._includeFinished = value

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
        super(SearchPolls, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(SearchPolls, self).getData(key)               # calls 'BaseGet.getData()

