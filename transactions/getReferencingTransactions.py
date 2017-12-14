# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetReferencingTransactions(Parent):

    def __init__(self,transaction=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Gets the transactions referencing a given transaction id.

            GetReferencingTransactions take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Referencing_Transactions

            REQUEST
            :param transaction : is one transaction ID (S)
            :param firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            :param lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return expectedTransactions : (A) is an array of expected transactions (refer to Get Transaction for details)
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

        self.transaction = transaction
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["transaction"]  = self.transaction

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetReferencingTransactions, self).__init__(rt = "getReferencingTransactions", data=self.data)

    def run(self):
        super(GetReferencingTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetReferencingTransactions, self).getData(key)    # calls 'BaseGet.getData()'