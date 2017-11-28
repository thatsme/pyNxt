# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAliases(Parent):
    def __init__(self, account = None, timestamp=0, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get information on aliases owned by a given account in alias name order.

            GetAliases take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with POST method only , and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request


            https://nxtwiki.org/wiki/The_Nxt_API#Get_Aliases

            REQUEST
            account : is the ID of the account that owns the aliases (S)
            timestamp : is the earliest creation time (in seconds since the genesis block) of the aliases (S) (O)
            firstIndex : is a zero-based index to the first alias to retrieve (O)
            lastIndex : is a zero-based index to the last alias to retrieve (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (optional)

            RESPONSE
            aliases : is an array (A) of alias objects (refer to Get Alias for details)
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            requestProcessingTime : is the API request processing time (in millisec) (N)

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

        # Required parameters
        self.account = account
        self.timestamp = timestamp
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
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

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAliases, self).__init__(rt="getAliases", data=self.data)

    def run(self):
        super(GetAliases, self).run()                                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(GetAliases, self).getData(key)                           # calls 'BasePost.getData()'
