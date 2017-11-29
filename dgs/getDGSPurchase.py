# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSPurchase(Parent):

    def __init__(self, purchase=None, sharedKey=None, requireBlock=None, requireLastBlock=None ):
        """
            Get a purchase order given a purchase order ID.

            GetDGSPurchase take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Purchase

            REQUEST
            purchase : is the purchase order ID (S)
            sharedKey : is the shared key used to decrypt the message (O) (see Get Shared Key)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)


            RESPONSE
            seller : (S) is the account number of the seller
            quantity : (N) is the quantity of the product to be purchased
            feedbackNotes : is an array (A) of AES-encrypted objects, each with data (S) and nonce (S) fields,
                            in reverse chronological order, if applicable
            publicFeedbacks : is an array (A) of feedback strings in reverse chronological order if applicable
            pending : is true if the deliveryDeadline has not passed, false otherwise (B)
            purchase : is the purchase order ID (S)
            goods : is the ID of the product (S)
            sellerRS : is the Reed-Solomon address of the seller (S)
            buyer : is the account number of the buyer (S)
            priceNQT : is the price (in NQT) of the product (S)
            deliveryDeadlineTimestamp : is the timestamp (N) (in seconds since the genesis block) by which the product must be delivered
            goodsIsText : is false if the message is a hex string, otherwise the message is text (B) (O)
            buyerRS : is the Reed-Solomon address of the buyer (S)
            refundNQT : is the amount (in NQT) refunded, if applicable (S)
            name : is the name of the product (S)
            goodsData : is an object with the two fields data (S) (the encrypted product hex string) and nonce (S),
                        if the product has been delivered (O)
            timestamp : is the timestamp (in seconds since the genesis block) of the purchase order(N)
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

        self.purchase = purchase
        self.sharedKey = sharedKey
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["purchase"] = self.purchase

        if self.sharedKey:
            self.data["sharedKey"] = self.sharedKey
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetDGSPurchase, self).__init__(rt = "getDGSPurchase", data=self.data)

    def run(self):
        super(GetDGSPurchase, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSPurchase, self).getData(key)             # calls 'BaseGet.getData()'