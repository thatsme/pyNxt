# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetTrades(Parent):
    def __init__(self, asset=None, account=None, timestamp=0, includeAssetInfo=False, ri=None, rb=None ):
        """
            Get trades associated with a given asset and/or accounts in reverse block height order.

            GetTrades take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Trades

            REQUEST
            :param asset : is the asset ID (S) (O)
            :param accounts : is the accounts ID (S) (optional if asset provided)
            :param timestamp : is the earliest block (in seconds since the genesis block) to retrieve (N) (O)
            :param includeAssetInfo : is true if the decimals and name fields are to be included (B) (O)
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
        self.asset = asset
        self.account = account
        self.timestamp = timestamp
        self.includeAssetInfo = includeAssetInfo
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset
        self.data["accounts"] = self.account
        self.data["timestamp"] = self.timestamp

        if self.includeAssetInfo:
            self.data["includeAssetInfo"] = self.includeAssetInfo

        super(GetTrades, self).__init__(rt="getTrades", data=self.data)

    def run(self):
        super(GetTrades, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetTrades, self).getData(key)                           # calls 'BaseGet.getData()'
