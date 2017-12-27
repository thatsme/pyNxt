# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetExpectedAssetTransfers(Parent):
    def __init__(self, asset=None, account=None, timestamp=0, includeAssetInfo=False, ri=None, rb=None ):
        """
            Get transfers associated with a given asset and/or accounts in reverse block height order
            (or in the expected order of execution for expected transfers).

            GetExpectedAssetTransfers take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Expected_Asset_Transfers

            REQUEST
            :param asset : is the asset ID (S)
            :param accounts : is the accounts ID (optional if asset is provided)
            :param timestamp : is the earliest deletion (in seconds since the genesis block) to retrieve (N) (O)
            :param includeAssetInfo : is true if asset information is to be included (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return transfers : is an array (A) of transfer objects with the following fields for each transfer:
            > quantityQNT (S) is the quantity (in QNT) of the asset traded
            > senderRS (S) is the Reed-Solomon address of the sender
            > assetTransfer (S) is the transaction ID of the asset transfer
            > sender (S) is the accounts number of the sender
            > recipientRS (S) is the Reed-Solomon address of the recipient
            > decimals (N) is the number of decimal places used by the asset (if includeAssetInfo is true)
            > recipient (S) is the accounts number of the recipient
            > name (S) is the name of the asset (if includeAssetInfo is true)
            > asset (S) is the asset ID
            > height (N) is the height of the transfer block
            > timestamp (N) is the timestamp (in seconds since the genesis block) of the transfer block, does not apply to an expected transfer
            > phased (B) is true if the transaction is phased, false otherwise, applies only to an expected transfer
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

        super(GetExpectedAssetTransfers, self).__init__(rt="getExpectedAssetTransfers", data=self.data, ri=self.ri, rb=self.rb)

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
        super(GetExpectedAssetTransfers, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetExpectedAssetTransfers, self).getData(key)                           # calls 'BaseGet.getData()'
