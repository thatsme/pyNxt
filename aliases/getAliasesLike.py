# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAliasesLike(Parent):
    def __init__(self, aliasPrefix = None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get all aliases starting with a given prefix in alias name order.

            GetAliases take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Aliases_Like

            REQUEST
            aliasPrefix : is the prefix (at least 2 characters long) of the aliasName (S) (R)
            firstIndex : is a zero-based index to the first alias to retrieve (S) (O)
            lastIndex : is a zero-based index to the last alias to retrieve (S) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (S) (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (S) (O)

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
        self.aliasPrefix = aliasPrefix

        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["aliasPrefix"] = self.aliasPrefix

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex

        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAliasesLike, self).__init__(rt="getAliasesLike", data=self.data)

    def run(self):
        super(GetAliasesLike, self).run()                                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(GetAliasesLike, self).getData(key)                           # calls 'BasePost.getData()'
