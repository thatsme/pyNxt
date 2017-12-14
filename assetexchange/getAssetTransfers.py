# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetTransfers(Parent):
    def __init__(self, asset=None, account=None, timestamp=0, includeAssetsInfo=False, ri=None, rb=None ):
        """
            Get transfers associated with a given asset and/or accounts in reverse block height order
            (or in the expected order of execution for expected transfers).

            GetAssetTransfers take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Transfers

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
        self.asset = asset
        self.account = account
        self.timestamp = timestamp
        self.includeAssetInfo = includeAssetsInfo
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

        super(GetAssetTransfers, self).__init__(rt="getAssetTransfers", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetAssetTransfers, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetTransfers, self).getData(key)                           # calls 'BaseGet.getData()'
