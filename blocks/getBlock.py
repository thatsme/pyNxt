# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBlock(Parent):
    def __init__(self, block = None, height=None, timestamp=0, includeTransactions=False, includeExecutedPhased=False, requireBlock=None, requireLastBlock=None ):
        """
            Get a block object given a block ID or block height.

            GetBlock take a default 1/3 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Block

            REQUEST
            block : is the block ID (S) (O)
            height : is the block height (N) (optional if block provided)
            timestamp : is the timestamp (N) (in seconds since the genesis block) of the block (optional if height provided)
            includeTransactions : is true to include transaction details (B) (O)
            includeExecutedPhased : is true to include approved and executed phased transactions (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (optional)

            RESPONSE
            previousBlockHash : is the 32-byte hash of the previous block (S)
            payloadLength : is the length (in bytes) of all transactions included in the block (N)
            totalAmountNQT : is the total amount (in NQT) of the transactions in the block (S)
            generationSignature : is the 32-byte generation signature of the generating account (S)
            generator : is the generating account number (S)
            generatorPublicKey : is the 32-byte public key of the generating account (S)
            baseTarget : is the base target for the next block generation (S)
            payloadHash : is the 32-byte hash of the payload (all transactions) (S)
            generatorRS : is the Reed-Solomon address of the generating account (S)
            nextBlock : is the next block ID (S)
            numberOfTransactions : is the number of transactions in the block (N)
            blockSignature : is the 64-byte block signature (S)
            transactions : is an array of transaction IDs or transaction objects (A)
                            (if includeTransactions provided, refer to Get Transaction for details)
            executedPhasedTransactions : is an array (A) of transaction IDs or transaction objects
                            (if includeExecutedPhased provided, refer to Get Transaction for details)
            version : is the block version (N)
            totalFeeNQT : is the total fee (in NQT) of the transactions in the block (S)
            previousBlock : is the previous block ID (S)
            cumulativeDifficulty : is the cumulative difficulty for the next block generation (S)
            block : is the block ID (S)
            height : is the zero-based block height (N)
            timestamp : is the timestamp (in seconds since the genesis block) of the block (N)
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            requestProcessingTime : is the API request processing time (in millisec) (N)

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
                (O) Object
                >   Array Element
                (WP) Wrapper specific parameter

        """

        # Required parameters
        self.block = block
        self.height = height
        self.timestamp = timestamp
        self.includeTransactions = includeTransactions
        self.includeExecutedPhased = includeExecutedPhased
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

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
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetBlock, self).__init__(rt="getBlock", data=self.data)

    def run(self):
        super(GetBlock, self).run()                                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(GetBlock, self).getData(key)                           # calls 'BasePost.getData()'
