# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class SearchAssets(Parent):

    def __init__(self, query=None, includeCounts=False, ri=None, rb=None ):
        """
            Get assets having a name or description that match a given query in reverse relevance order.

            SearchAssets take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Search_Assets

            REQUEST
            :param query : is a full text query on the asset fields name (S) and description (S) in the standard Lucene syntax
            :param includeCounts : is true if the fields beginning with numberOf... are to be included (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return assets (A) is an array of asset objects (refer to Get Asset)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

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
        self._includeCounts = includeCounts
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["query"] = query

        super(SearchAssets, self).__init__(rt = "searchAssets", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value

    @property
    def includeCounts(self):
        return self._includeCounts

    @includeCounts.setter
    def includeCounts(self, value):
        self._includeCounts = value

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
        super(SearchAssets, self).run()                   # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(SearchAssets, self).getData(key)     # calls 'BaseGet.getData()'