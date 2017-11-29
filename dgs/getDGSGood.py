# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSGood(Parent):

    def __init__(self, goods=None, firstIndex=None, lastIndex=None, includeCounts=False, requireBlock=None, requireLastBlock=None ):
        """
            Get a DGS product given a goods ID.

            GetDGSGood take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Good

            REQUEST
            goods is the goods ID of the product
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            seller : (S) is the seller's account ID
            quantity : (N) is the quantity of the product remaining for sale
            goods : (S) is the ID of the product
            description : (S) is the description of the product
            sellerRS : (S) is the Reed-Solomon address of the seller's account
            delisted : (B) is true if the product has been delisted, false otherwise
            parsedTags : (A) is an array of up to three tag strings, parsed from the tags field
            tags : (S) is the comma separated list of tags provided by the seller when the listing was created
            priceNQT : (S) is the current price of the product
            numberOfPublicFeedbacks : (N) is the number of public feedbacks given for the product
            name : (S) is the name of the product
            numberOfPurchases : (N) is the number of purchases of the product
            timestamp : (N) is the timestamp (in seconds since the genesis block) of the creation of the product listing
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

        self.goods = goods
        self.includeCounts = includeCounts
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["goods"] = goods

        if self.includeCounts:
            self.data["includeCounts"] = includeCounts

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetDGSGood, self).__init__(rt = "getDGSGood", data=self.data)

    def run(self):
        super(GetDGSGood, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSGood, self).getData(key)             # calls 'BaseGet.getData()'