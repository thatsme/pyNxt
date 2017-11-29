# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSPurchaseCount  (Parent):

    def __init__(self, seller=None, buyer=None, withPublicFeedbacksOnly=False, completed=False, requireBlock=None, requireLastBlock=None ):
        """
            Get the number of purchase orders given a seller and/or buyer ID, or all orders combined.

            GetDGSPurchaseCount take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Purchase_Count

            REQUEST
            seller is the account ID of the seller (optional, default is all sellers)
            buyer is the account ID of the buyer (optional, default is all buyers)
            withPublicFeedbacksOnly : is true if purchase orders without public feedback are to be omitted (B) (O)
            completed : is true if only completed purchase orders are to be included (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            numberOfPurchases : (N) is the number of purchase orders associated with the seller and/or buyer
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

        self.seller = seller
        self.buyer = buyer
        self.withPublicFeedbacksOnly = withPublicFeedbacksOnly
        self.completed = completed
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["seller"] = seller
        self.data["buyer"] = buyer

        if self.withPublicFeedbacksOnly:
            self.data["withPublicFeedbacksOnly"] = withPublicFeedbacksOnly
        if self.completed:
            self.data["completed"] = completed

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetDGSPurchaseCount, self).__init__(rt = "getDGSPurchaseCount", data=self.data)

    def run(self):
        super(GetDGSPurchaseCount, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSPurchaseCount, self).getData(key)             # calls 'BaseGet.getData()'