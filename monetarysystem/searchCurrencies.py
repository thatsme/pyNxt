# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class SearchCurrencies(Parent):

    def __init__(self, query=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get currencies having a code that matches a given query in reverse relevance order.

            SearchCurrencies take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Search_Currencies

            REQUEST
            :param query : is a full text query on the currency field code in the standard Lucene syntax (S)
            :param firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            :param lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            :param includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

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
                (O) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self.query = query
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["query"] = query

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(SearchCurrencies, self).__init__(rt = "searchCurrencies", data=self.data)

    def run(self):
        super(SearchCurrencies, self).run()                   # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(SearchCurrencies, self).getData(key)     # calls 'BaseGet.getData()'