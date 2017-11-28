# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountPhasedTransactions(Parent):

    def __init__(self, account=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):
        """
            Get pending phased transactions associated with an account given the account ID in reverse chronological creation order.

            GetAccountPhasedTransactions take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Phased_Transactions

            REQUEST
            account : is the id of account (S) (R)
            firstIndex : is a zero-based index to the first block to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block to retrieve (N) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            sender : is the account ID of the sender (S)
            senderRS : is the Reed-Solomon address of the sender (S)
            feeNQT : is the fee (in NQT) of the transaction (S)
            amountNQT : is the amount (in NQT) of the transaction (S)
            transactionIndex : is a zero-based index giving the order of the transaction in its block (N)
            timestamp : is the time (in seconds since the genesis block) of the transaction (N)
            referencedTransactionFullHash : is the full hash of a transaction referenced by this one, omitted if no previous transaction is referenced (S)
            confirmations : is the number of transaction confirmations (N)
            subtype : is the transaction subtype (refer to Get Constants for a current list of subtypes) (N)
            block : is the ID of the block containing the transaction (S)
            blockTimestamp : is the timestamp (in seconds since the genesis block) of the block (N)
            height : is the height of the block in the blockchain
            senderPublicKey : is the public key of the sending account for the transaction (S)
            type : is the transaction type (refer to Get Constants for a current list of types) (N)
            deadline : is the deadline (in minutes) for the transaction to be confirmed (N)
            signature : is the digital signature of the transaction (S)
            recipient : is the account number of the recipient, if applicable (S)
            recipientRS : is the Reed-Solomon address of the recipient, if applicable (S)
            fullHash : is the full hash of the signed transaction (S)
            signatureHash : is a SHA-256 hash of the transaction signature (S)
            approved : is a boolean indicating if the transaction is approved  (B) (only included when includePhasingResult is true and the transaction is phased)
            result : is a string containing the result of the transaction (S) (only included when includePhasingResult is true and the transaction is phased)
            executionHeight : is the height the transaction was executed (N) (only included when includePhasingResult is true and the transaction is phased)
            transaction : is the transaction ID (S)
            version : is the transaction version number (N)
            phased : is true if the transaction is phased, false otherwise (B)
            ecBlockId : is the economic clustering block ID (N)
            ecBlockHeight : is the economic clustering block height (N)
            attachment : is an object containing any additional data needed for the transaction, if applicable (O)
            lastBlock : is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock) (S)
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

        """

        self.account = account
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountPhasedTransactions, self).__init__(rt = "getAccountPhasedTransactions", data=self.data)

    def run(self):
        super(GetAccountPhasedTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountPhasedTransactions, self).getData(key)    # calls 'BaseGet.getData()'