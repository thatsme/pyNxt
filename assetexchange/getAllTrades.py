# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAllTrades(Parent):
    def __init__(self, timestamp=0, includeAssetInfo=False, ri=None, rb=None ):
        """
            Get all trades since a given timestamp in reverse block height order.

            GetAllTrades take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_All_Trades

            REQUEST
            :param timestamp : is the timestamp (in seconds since the genesis block) to begin retrieving trades (optional, default 0)
            :param includeAssetInfo : is true if asset information is to be included in the result (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return assets : is an array (A) of asset objects (refer to Get Asset)
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
        self.timestamp = timestamp
        self.includeAssetInfo = includeAssetInfo
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["timestamp"] = self.timestamp
        if self.includeAssetInfo:
            self.data["includeAssetInfo"] = self.includeAssetInfo

        super(GetAllTrades, self).__init__(rt="getAllTrades", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetAllTrades, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAllTrades, self).getData(key)                           # calls 'BaseGet.getData()'
