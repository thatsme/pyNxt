# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAlias(Parent):
    def __init__(self, alias = None, aliasName=None, requireBlock=None, requireLastBlock=None ):
        """
            Get information about a given alias

            GetAlias take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with POST method only , and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request


            https://nxtwiki.org/wiki/The_Nxt_API#Get_Alias

            REQUEST
            alias : is the ID of the account that owns the aliases (S)
            aliasName : is the earliest creation time (in seconds since the genesis block) of the aliases (S) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (optional)

            RESPONSE
            timestamp : is the time (in seconds since the genesis block) when the alias was created or last transferred (N)
            aliasName : is the name of the alias (S)
            account : is the number of the account that owns the alias (S)
            accountRS : is the Reed-Solomon address of the account that owns the alias (S)
            aliasURI : is what the alias points to, in URI format (S)
            alias : is the alias ID (S)
            priceNQT : is the asking price (in NQT) of the alias if it is for sale (S)
            buyer : is the account number of the buyer if the alias is for sale and a buyer is specified (S)
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
        self.alias = alias
        self.aliasName = aliasName
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["alias"] = self.alias
        self.data["aliasName"] = self.aliasName

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAlias, self).__init__(rt="getAlias", data=self.data)

    def run(self):
        super(GetAlias, self).run()                                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(GetAlias, self).getData(key)                           # calls 'BasePost.getData()'
