# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class SearchAccounts(Parent):

    def __init__(self, query=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get accounts having a name or description that match a given query in reverse relevance order.

            SearchAccounts take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Search_Accounts

            REQUEST
            query : is a full text query on the account fields name (S) and description (S) in the standard Lucene syntax
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            accounts (A) is an array of account objects with the following fields:
            > account (S) is the account number
            > accountRS (S) is the Reed-Solomon address of the account
            > name (S) is the name of the account
            > description (S) is the description of the account (if applicable)
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            requestProcessingTime : is the API request processing time (N) (in millisec)

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

        super(SearchAccounts, self).__init__(rt = "searchAccounts", data=self.data)

    def run(self):
        super(SearchAccounts, self).run()                   # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(SearchAccounts, self).getData(key)     # calls 'BaseGet.getData()'