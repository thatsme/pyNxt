# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetDividends(Parent):
    def __init__(self, asset=None, timestamp=0, adminPassword=None, ri=None, rb=None ):
        """
            Get the dividend payment history for a specific asset.

            GetAssetDividends take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Dividends

            REQUEST
            :param asset : is the asset ID (S)
            :param accounts : is the accounts ID (optional if asset is provided)
            :param timestamp : is the earliest deletion (in seconds since the genesis block) to retrieve (N) (O)
            :param adminPassword is a string with the admin password  (S) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return dividends : is an array (A) of dividend transactions with the following properties:
            > assetDividend : (S) is the dividend payment transaction ID
            > numberOfAccounts : (N) is the number of accounts that received a dividend
            > amountNQTPerQNT : (S) is the amount of NXT (in NQT) paid per quantity (in QNT) of the asset
            > totalDividend : (S) is the total amount of NXT (in NQT) sent in the dividend payment
            > dividendHeight : (N) is the block height of the dividend calculation
            > asset : (S) is the asset ID
            > height : (N) is the block height of the dividend payment
            > timestamp : (N) is the block timestamp of the dividend payment
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
        self.timestamp = timestamp
        self.adminPassword = adminPassword
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset
        self.data["timestamp"] = self.timestamp

        if self.adminPassword:
            self.data["adminPassword"] = self.adminPassword

        super(GetAssetDividends, self).__init__(rt="getAssetDividends", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetAssetDividends, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetDividends, self).getData(key)                           # calls 'BaseGet.getData()'
