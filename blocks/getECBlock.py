# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetECBlock(Parent):
    def __init__(self, timestamp=0, rb=None ):
        """
            Get Economic Cluster block data.

            GetECBlock take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_ECBlock

            REQUEST
            :param timestamp : is the timestamp (in seconds since the genesis block) of the EC block
                        (optional, default (or zero) is the current timestamp)
            :param rb : rb object ( check base/Rb.py) (WP)

            Note: If timestamp is more than 15 seconds before the timestamp of the last block on the blockchain, errorCode 4 is returned.

            RESPONSE
            :return ecBlockHeight (N) is the EC block height
            :return ecBlockId (S) is the EC block ID
            :return timestamp : is the timestamp (in seconds since the genesis block) of the EC block (N)
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
        self._timestamp = timestamp
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["timestamp"] = self.timestamp

        super(GetECBlock, self).__init__(rt="getECBlock", data=self.data, rb=self.rb)

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetECBlock, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetECBlock, self).getData(key)                           # calls 'BaseGet.getData()'
