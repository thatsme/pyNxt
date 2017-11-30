# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBlockchainTransactions(Parent):

    def __init__(self,account=None, timestamp=0, type=None, subtype=None, firstIndex=None, lastIndex=None, numberOfConfirmations=0, withMessage=False, phasedOnly=False, nonPhasedOnly=False, includeExpiredPrunable=False, includePhasingResult=False, executeOnly=False, requireBlock=None, requireLastBlock=None ):
        """
            Get the transactions associated with an accounts in reverse block timestamp order.

            GetBlockchainTransactions take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Blockchain_Transactions

            REQUEST
            accounts : is accounts ID (S)
            timestamp : is the earliest block (in seconds since the genesis block) to retrieve (N) (O)
            type : is the type of transactions to retrieve (S) (O)
            subtype : is the subtype of transactions to retrieve (S) (O)
            firstIndex : is a zero-based index to the first transaction to retrieve (N) (O)
            lastIndex : is a zero-based index to the last transaction to retrieve (N) (O)
            numberOfConfirmations : is the required number of confirmations per transaction (B) (O)
            withMessage : is true to retrieve only only transactions having a message attachment, either non-encrypted or decryptable by the accounts (B) (O)
            phasedOnly : is true to retrieve only phased transactions (B) (O) (optional unless nonPhasedOnly provided)
            nonPhasedOnly : is true to retrieve only nonphased transactions (B) (O) (optional unless phasedOnly provided)
            includeExpiredPrunable : is true' to retrieve pruned data if available (B) (O)
            includePhasingResult : is true to retrieve execution status of each phased transaction (B) (O)
            executedOnly : is true to exclude phased transactions that are not yet executed (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            transactions : is an array (A) of transactions (refer to Get Transaction for details)
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            requestProcessingTime : is the API request processing time (N) (in millisec)

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

        self.account = account
        self.timestamp = timestamp
        self.type = type
        self.subtype = subtype
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.numberOfConfirmations = numberOfConfirmations
        self.withMessage = withMessage
        self.phasedOnly = phasedOnly
        self.nonPhasedOnly = nonPhasedOnly
        self.includeExpiredPrunable = includeExpiredPrunable
        self.includePhasingResult = includePhasingResult
        self.executeOnly = executeOnly
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["timestamp"] = self.timestamp
        self.data["numberOfConfirmations"] = self.numberOfConfirmations
        if self.type:
            self.data["type"] = self.type
        if self.subtype:
            self.data["subtype"] = self.subtype

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.withMessage:
            self.data["withMessage"] = self.withMessage
        if self.phasedOnly:
            self.data["phasedOnly"] = self.phasedOnly
        if self.nonPhasedOnly:
            self.data["nonPhasedOnly"] = self.nonPhasedOnly
        if self.includeExpiredPrunable:
            self.data["includeExpiredPrunable"] = self.includeExpiredPrunable
        if self.includePhasingResult:
            self.data["includePhasingResult"] = self.includePhasingResult
        if self.executeOnly:
            self.data["executeOnly"] = self.executeOnly
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetBlockchainTransactions, self).__init__(rt = "getBlockchainTransactions", data=self.data)

    def run(self):
        super(GetBlockchainTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBlockchainTransactions, self).getData(key)    # calls 'BaseGet.getData()'