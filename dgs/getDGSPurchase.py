# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSPurchase(Parent):

    def __init__(self, purchase=None, sharedKey=None, rb=None ):
        """
            Get a purchase order given a purchase order ID.

            GetDGSPurchase take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Purchase

            REQUEST
            :param purchase : is the purchase order ID (S)
            :param sharedKey : is the shared key used to decrypt the message (O) (see Get Shared Key)
            :param rb : rb object ( check base/Rb.py) (WP)


            RESPONSE
            :return seller : (S) is the accounts number of the seller
            :return quantity : (N) is the quantity of the product to be purchased
            :return feedbackNotes : is an array (A) of AES-encrypted objects, each with data (S) and nonce (S) fields,
                            in reverse chronological order, if applicable
            :return publicFeedbacks : is an array (A) of feedback strings in reverse chronological order if applicable
            :return pending : is true if the deliveryDeadline has not passed, false otherwise (B)
            :return purchase : is the purchase order ID (S)
            :return goods : is the ID of the product (S)
            :return sellerRS : is the Reed-Solomon address of the seller (S)
            :return buyer : is the accounts number of the buyer (S)
            :return priceNQT : is the price (in NQT) of the product (S)
            :return deliveryDeadlineTimestamp : is the timestamp (N) (in seconds since the genesis block) by which the product must be delivered
            :return goodsIsText : is false if the message is a hex string, otherwise the message is text (B) (O)
            :return buyerRS : is the Reed-Solomon address of the buyer (S)
            :return refundNQT : is the amount (in NQT) refunded, if applicable (S)
            :return name : is the name of the product (S)
            :return goodsData : is an object with the two fields data (S) (the encrypted product hex string) and nonce (S),
                                if the product has been delivered (O)
            :return timestamp : is the timestamp (in seconds since the genesis block) of the purchase order(N)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self.purchase = purchase
        self.sharedKey = sharedKey
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["purchase"] = self.purchase

        if self.sharedKey:
            self.data["sharedKey"] = self.sharedKey

        super(GetDGSPurchase, self).__init__(rt = "getDGSPurchase", data=self.data, rb=self.rb)

    def run(self):
        super(GetDGSPurchase, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSPurchase, self).getData(key)             # calls 'BaseGet.getData()'