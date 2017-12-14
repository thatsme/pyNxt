# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetExpectedAssetDeletes(Parent):
    def __init__(self, asset=None, account=None, timestamp=0, includeAssetInfo=False, ri=None, rb=None ):
        """
            Gets asset deletes which are expected to be executed in the next block.

            GetExpectedAssetDeletes take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Expected_Asset_Deletes

            REQUEST
            :param asset : is the asset ID (S)
            :param accounts : is the accounts ID (optional if asset is provided)
            :param timestamp : is the earliest deletion (in seconds since the genesis block) to retrieve (N) (O)
            :param includeAssetInfo : is true if asset information is to be included (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return deletes : is an array (A) of asset delete objects with following properties:
            > quantityQNT : (S) is the number of shares that was deleted
            > assetDelete : (S) is the transaction ID
            > accounts : (S) is the accounts ID
            > accountRS : (S) is the accounts Reed Solomon address
            > asset : (S) is the asset ID
            > height : (N) is the block height of the delete
            > timestamp : (N) is the block timestamp of the delete
            > decimals : (N) is the number of decimal places used by the asset (if includeAssetInfo is true)
            > name : (S) is the asset name (if includeAssetInfo is true)
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

        if self.includeAssetInfo:
            self.data["includeAssetInfo"] = self.includeAssetInfo

        super(GetExpectedAssetDeletes, self).__init__(rt="getExpectedAssetDeletes", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetExpectedAssetDeletes, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetExpectedAssetDeletes, self).getData(key)                           # calls 'BaseGet.getData()'
