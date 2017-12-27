# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetDeletes(Parent):
    def __init__(self, asset=None, account=None, timestamp=0, includeAssetInfo=False, ri=None, rb=None ):
        """
            Get asset deletions for a specific asset or accounts.

            GetAssetDeletes take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Deletes

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
        self._asset = asset
        self._account = account
        self._timestamp = timestamp
        self._includeAssetInfo = includeAssetInfo
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["asset"] = self.asset
        self.data["accounts"] = self.account

        if self.includeAssetInfo:
            self.data["includeAssetInfo"] = self.includeAssetInfo

        super(GetAssetDeletes, self).__init__(rt="getAssetDeletes", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, value):
        self._asset = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def includeAssetInfo(self):
        return self._includeAssetInfo

    @includeAssetInfo.setter
    def includeAssetInfo(self, value):
        self._includeAssetInfo = value

    @property
    def ri(self):
        return self._ri

    @ri.setter
    def ri(self, value):
        self._ri = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetAssetDeletes, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetDeletes, self).getData(key)                           # calls 'BaseGet.getData()'
