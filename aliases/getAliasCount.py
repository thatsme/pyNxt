# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAliasCount(Parent):
    def __init__(self, account = None, requireBlock=None, requireLastBlock=None ):
        """
            GetAliasCount take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Alias_Count

            REQUEST
            account : is the account
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (S) (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (S) (O)

            RESPONSE
            numberOfAliases : is the number of aliases owned by the account (N)
            lastBlock : is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            RequestProcessingTime (N) is the API request processing time (in millisec) (S)

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
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["account"] = self.account

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAliasCount, self).__init__(rt="getAliasCount", data=self.data)

    def run(self):
        super(GetAliasCount, self).run()                                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(GetAliasCount, self).getData(key)                           # calls 'BasePost.getData()'
