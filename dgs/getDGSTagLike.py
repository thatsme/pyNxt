# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSTagsLike(Parent):

    def __init__(self, tagPrefix=None, firstIndex=None, lastIndex=None, inStockOnly=False, requireBlock=None, requireLastBlock=None ):
        """
            Get all tags starting with a given prefix (at least 2 characters long) in reverse inStockCount, reverse totalCount, tag order.

            GetDGSTagsLike take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Tags_Like

            REQUEST
            tagPrefix : is the prefix (at least 2 characters long) of the tag
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            inStockOnly : is false if out-of-stock products (zero quantity) are to be retrieved (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)


            RESPONSE
            tags (A) is an array of tag objects with the following fields for each tag:
            > inStockCount (N) is the number of products available for sale as tagged
            > tag (S) is the tag word
            > totalCount (N) is the total number of products as tagged
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            requestProcessingTime : is the API request processing time (N) (in millisec)

            Note: The ...Count fields refer to the number of distinct products tagged, regardless of the quantity of each.

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
        self.tagPrefix = tagPrefix
        self.inStockOnly = inStockOnly
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}
        self.data["tagPrefix"] = tagPrefix

        ## Create data dictionary

        if self.inStockOnly:
            self.data["inStockOnly"] = inStockOnly

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetDGSTagsLike, self).__init__(rt = "getDGSTagsLike", data=self.data)

    def run(self):
        super(GetDGSTagsLike, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSTagsLike, self).getData(key)             # calls 'BaseGet.getData()'
