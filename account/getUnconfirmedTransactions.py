# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetUnconfirmedTransactions(Parent):

    def __init__(self, account=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):
        """
            Get a list of unconfirmed transactions associated with an account.

            GetUnconfirmetTransactions take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Unconfirmed_Transactions

            REQUEST
            account : is array (A) of account ID's (S) / Multiaccount parameters (3)
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            unconfirmedTransactions : is an array (A) of unconfirmed transactions (refer to Get Transaction for details)
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
            self.data["account"] = a

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetUnconfirmedTransactions, self).__init__(rt = "getUnconfirmedTransactions", data=self.data)

    def run(self):
        super(GetUnconfirmedTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetUnconfirmedTransactions, self).getData(key)    # calls 'BaseGet.getData()'