# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetOrderTrades(Parent):
    def __init__(self, askOrder=None, bidOrder=None, includeCounts=False, ri=None, rb=None ):
        """
            Get all trades that were executed as a result of a given askOrder and/or bidOrder in reverse block height order.

            GetOrderTrades take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Order_Trades

            REQUEST
            :param askOrder : is an ask order ID (N) (O)
            :param bidOrder : is a bid order ID (N) (optional if askOrder provided)
            :param includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return trades : is an array (A) of trade objects with the following fields for each trade:
            > seller (S) is the accounts number of the seller
            > quantityQNT (S) is the quantity (in QNT) of the asset traded
            > bidOrder (S) is the bid order ID
            > sellerRS (S) is the Reed-Solomon address of the seller
            > buyer (S) is the accounts number of the buyer
            > priceNQT (S) is the trade price (in NQT, the ask price for a buy or the bid price for a sell)
            > askOrder (S) is the ask order ID
            > buyerRS (S) is the Reed-Solomon address of the buyer
            > decimals (N) is the number of decimal places used by the asset
            > name (S) is the name of the asset (if includeAssetInfo is true)
            > block (S) is the block ID of the trade (if includeAssetInfo is true)
            > asset (S) is the asset ID
            > askOrderHeight (N) is the block height of the ask order
            > bidOrderHeight (N) is the block height of the bid order
            > tradeType (S) is the trade type (sell or buy, where buy implies that the bid occurred after the ask, or if in the same block, has a greater order ID)
            > timestamp (N) is the timestamp (in seconds since the genesis block) of the trade block
            > height (N) is the height of the trade block
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)

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

        # Required parameters
        self.askOrder = askOrder
        self.bidOrder = bidOrder
        self.includeCounts = includeCounts
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["askOrder"] = self.askOrder
        self.data["bidOrder"] = self.bidOrder

        if self.includeCounts:
            self.data["includeCounts"] = self.includeCounts

        super(GetOrderTrades, self).__init__(rt="getOrderTrades", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetOrderTrades, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetOrderTrades, self).getData(key)                           # calls 'BaseGet.getData()'
