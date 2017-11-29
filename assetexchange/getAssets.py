# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssets(Parent):

    def __init__(self,asset=None, firstIndex=None, lastIndex=None, includeCounts=False, requireBlock=None, requireLastBlock=None ):
        """
            Get asset information given multiple asset IDs

            GetAssets take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Assets

            REQUEST
            account : is array (A) of asset ID's (S) / Multiaccount parameters (3)
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            assets : is an array (A) of asset objects (refer to Get Asset)
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

        self.assets = [None]*3
        for a in asset[:3]:
            self.assets.append(a)

        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.includeCounts = includeCounts
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        for a in self.assets:
            self.data["asset"] = a

        if firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.includeCounts:
            self.data["includeCounts"] = self.includeCounts
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAssets, self).__init__(rt = "getAssets", data=self.data)

    def run(self):
        super(GetAssets, self).run()                                # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssets, self).getData(key)                  # calls 'BaseGet.getData()'