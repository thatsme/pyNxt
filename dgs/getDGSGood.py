# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDGSGood(Parent):

    def __init__(self, goods=None, includeCounts=False, ri=None, rb=None ):
        """
            Get a DGS product given a goods ID.

            GetDGSGood take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_DGS_Good

            REQUEST
            :param goods is the goods ID of the product
            :param includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return seller : (S) is the seller's accounts ID
            :return quantity : (N) is the quantity of the product remaining for sale
            :return goods : (S) is the ID of the product
            :return description : (S) is the description of the product
            :return sellerRS : (S) is the Reed-Solomon address of the seller's accounts
            :return delisted : (B) is true if the product has been delisted, false otherwise
            :return parsedTags : (A) is an array of up to three tag strings, parsed from the tags field
            :return tags : (S) is the comma separated list of tags provided by the seller when the listing was created
            :return priceNQT : (S) is the current price of the product
            :return numberOfPublicFeedbacks : (N) is the number of public feedbacks given for the product
            :return name : (S) is the name of the product
            :return numberOfPurchases : (N) is the number of purchases of the product
            :return timestamp : (N) is the timestamp (in seconds since the genesis block) of the creation of the product listing
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

        self.goods = goods
        self.includeCounts = includeCounts
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["goods"] = goods

        if self.includeCounts:
            self.data["includeCounts"] = includeCounts

        super(GetDGSGood, self).__init__(rt = "getDGSGood", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetDGSGood, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetDGSGood, self).getData(key)             # calls 'BaseGet.getData()'