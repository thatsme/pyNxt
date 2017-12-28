# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class SearchCurrencies(Parent):

    def __init__(self, query=None, ri=None, rb=None ):
        """
            Get currencies having a code that matches a given query in reverse relevance order.

            SearchCurrencies take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Search_Currencies

            REQUEST
            :param query : is a full text query on the currency field code in the standard Lucene syntax (S)
            :param includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return currencies (A) is an array of currency objects (refer to Get Currency for details)
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
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["query"] = query

        super(SearchCurrencies, self).__init__(rt = "searchCurrencies", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value

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
        super(SearchCurrencies, self).run()                   # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(SearchCurrencies, self).getData(key)     # calls 'BaseGet.getData()'