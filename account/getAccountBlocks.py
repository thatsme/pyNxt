# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountBlocks(Parent):

    def __init__(self, account=None, timestamp=0, firstIndex=None, lastIndex=None,includeTransactions=False, requireBlock=None, requireLastBlock=None):
        """
            GetAccountBlocks take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Blocks

            REQUEST
            account : is the id of account (S) (R)
            timestamp : is the earliest block (in seconds since the genesis block) to retrieve (N) (O)
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            includeTransactions : is true to retrieve transaction details, otherwise only transaction IDs are retrieved (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            blocks : is an array (A) of blocks (refer to Get Block for details)
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

        self.account = account
        self.timestamp = timestamp
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.includeTransactions = includeTransactions
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        self.data["timestamp"] = self.timestamp
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.includeTransactions:
            self.data["includeTransactions"] = self.includeTransactions
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountBlocks, self).__init__(rt = "getAccountBlocks", data=self.data)

    def run(self):
        super(GetAccountBlocks, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountBlocks, self).getData(key)    # calls 'BaseGet.getData()'