# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBlocks(Parent):
    def __init__(self, timestamp=0, includeTransactions=False, includeExecutedPhased=False, ri=None, rb=None ):
        """
            Get blocks from the blockchain in reverse block height order.

            GetBlocks take a default 1/3 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Blocks

            REQUEST
            :param timestamp : is the timestamp (N) (in seconds since the genesis block) of the block (optional if height provided)
            :param includeTransactions : is true to include transaction details (B) (O)
            :param includeExecutedPhased : is true to include approved and executed phased transactions (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return blocks : is an array (A) of blocks retrieved (refer to Get Block for details)
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
        self._includeTransactions = includeTransactions
        self._includeExecutedPhased = includeExecutedPhased
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["timestamp"] = self.timestamp
        if self.includeTransactions:
            self.data["includeTransactions"] = self.includeTransactions
        if self.includeExecutedPhased:
            self.data["includeExecutedPhased"] = self.includeExecutedPhased

        super(GetBlocks, self).__init__(rt="getBlocks", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def includeTransactions(self):
        return self._includeTransactions

    @includeTransactions.setter
    def includeTransactions(self, value):
        self._includeTransactions = value

    @property
    def includeExecutedPhased(self):
        return self._includeExecutedPhased

    @includeExecutedPhased.setter
    def includeExecutedPhased(self, value):
        self._includeExecutedPhased = value

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
        super(GetBlocks, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBlocks, self).getData(key)                           # calls 'BaseGet.getData()'
