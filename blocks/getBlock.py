# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBlock(Parent):
    def __init__(self, block = None, height=None, timestamp=0, includeTransactions=False, includeExecutedPhased=False, rb=None ):
        """
            Get a block object given a block ID or block height.

            GetBlock take a default 1/3 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Block

            REQUEST
            :param block : is the block ID (S) (O)
            :param height : is the block height (N) (optional if block provided)
            :param timestamp : is the timestamp (N) (in seconds since the genesis block) of the block (optional if height provided)
            :param includeTransactions : is true to include transaction details (B) (O)
            :param includeExecutedPhased : is true to include approved and executed phased transactions (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return previousBlockHash : is the 32-byte hash of the previous block (S)
            :return payloadLength : is the length (in bytes) of all transactions included in the block (N)
            :return totalAmountNQT : is the total amount (in NQT) of the transactions in the block (S)
            :return generationSignature : is the 32-byte generation signature of the generating accounts (S)
            :return generator : is the generating accounts number (S)
            :return generatorPublicKey : is the 32-byte public key of the generating accounts (S)
            :return baseTarget : is the base target for the next block generation (S)
            :returns payloadHash : is the 32-byte hash of the payload (all transactions) (S)
            :return generatorRS : is the Reed-Solomon address of the generating accounts (S)
            :return nextBlock : is the next block ID (S)
            :return numberOfTransactions : is the number of transactions in the block (N)
            :return blockSignature : is the 64-byte block signature (S)
            :return transactions : is an array of transaction IDs or transaction objects (A)
                            (if includeTransactions provided, refer to Get Transaction for details)
            :return executedPhasedTransactions : is an array (A) of transaction IDs or transaction objects
                            (if includeExecutedPhased provided, refer to Get Transaction for details)
            :return version : is the block version (N)
            :return totalFeeNQT : is the total fee (in NQT) of the transactions in the block (S)
            :return previousBlock : is the previous block ID (S)
            :return cumulativeDifficulty : is the cumulative difficulty for the next block generation (S)
            :return block : is the block ID (S)
            :return height : is the zero-based block height (N)
            :return timestamp : is the timestamp (in seconds since the genesis block) of the block (N)
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
        self._block = block
        self._height = height
        self._timestamp = timestamp
        self._includeTransactions = includeTransactions
        self._includeExecutedPhased = includeExecutedPhased
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["block"] = self.block
        if self.height:
            self.data["height"] = self.height
        if self.timestamp:
            self.data["timestamp"] = self.timestamp
        if self.includeTransactions:
            self.data["includeTransactions"] = self.includeTransactions
        if self.includeExecutedPhased:
            self.data["includeExecutedPhased"] = self.includeExecutedPhased

        super(GetBlock, self).__init__(rt="getBlock", data=self.data, rb=self.rb)

    @property
    def block(self):
        return self._block

    @block.setter
    def block(self, value):
        self._block = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

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
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetBlock, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBlock, self).getData(key)                           # calls 'BaseGet.getData()'
