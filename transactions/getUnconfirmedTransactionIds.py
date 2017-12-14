# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetUnconfirmedTransactionIds(Parent):

    def __init__(self,account=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get a list of unconfirmed transaction IDs associated with an account.

            GetUnconfirmedTransactionIds take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Unconfirmed_Transaction_Ids

            REQUEST
            :param account : is array (A) of accounts ID's (S) / Multiaccount parameters (3)
            :param firstIndex is a zero-based index to the first transaction ID to retrieve (optional)
            :param lastIndex is a zero-based index to the last transaction ID to retrieve (optional)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return unconfirmedTransactionIds : (A) is an array of unconfirmed transaction IDs
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

        self.accounts = [None]*3
        for a in account[:3]:
            self.accounts.append(a)

        self.firstIndex = firstIndex
        self.lastIndex = lastIndex

        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        for a in self.accounts:
            self.data["accounts"] = a

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetUnconfirmedTransactionIds, self).__init__(rt = "getUnconfirmedTransactionIds", data=self.data)

    def run(self):
        super(GetUnconfirmedTransactionIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetUnconfirmedTransactionIds, self).getData(key)    # calls 'BaseGet.getData()'