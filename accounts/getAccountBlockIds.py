# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountBlockIds(Parent):

    def __init__(self, account=None, timestamp=0, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):
        """
            GetAccountBlockIds take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Block_Ids

            REQUEST
            accounts : is the id of accounts (S) (R)
            timestamp : is the earliest block (in seconds since the genesis block) to retrieve (N) (O)
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            blockIds : is an array (A) of block IDs
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
                (WP) Wrapper specific parameter

        """

        self.account = account
        self.timestamp = timestamp
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["timestamp"] = self.timestamp
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountBlockIds, self).__init__(rt = "getAccountBlockIds", data=self.data)

    def run(self):
        super(GetAccountBlockIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountBlockIds, self).getData(key)    # calls 'BaseGet.getData()'