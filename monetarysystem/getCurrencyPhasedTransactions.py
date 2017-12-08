# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrencyPhasedTransactions(Parent):
    def __init__(self, currency=None, account=None, firstIndex=None, lastIndex=None, withoutWitelist=False, requireBlock=None, requireLastBlock=None ):
        """
            Get pending phased transactions based on a currency in reverse chronological creation order.
            These transactions can be considered transaction approval requests.

            GetCurrencyPhasedTransactions take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currency_Phased_Transactions

            REQUEST
            currency is the currency ID (S)
            account : is an account ID of the account that created the phased transactions (S) (O)
            firstIndex : is a zero-based index to the first accounts to retrieve (N) (O)
            lastIndex : is a zero-based index to the last accounts to retrieve (N) (O)
            withoutWhitelist : is true to omit phased transactions that include a whitelist (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            sender : (S) is the accounts ID of the sender
            senderRS : (S) is the Reed-Solomon address of the sender
            feeNQT : (S) is the fee (in NQT) of the transaction
            amountNQT : (S) is the amount (in NQT) of the transaction
            transactionIndex : (N) is a zero-based index giving the order of the transaction in its block
            timestamp : (N) is the time (in seconds since the genesis block) of the transaction
            referencedTransactionFullHash : (S) is the full hash of a transaction referenced by this one, omitted if no previous transaction is referenced
            confirmations : (N) is the number of transaction confirmations
            subtype : (N) is the transaction subtype (refer to Get Constants for a current list of subtypes)
            block : (S) is the ID of the block containing the transaction
            blockTimestamp : (N) is the timestamp (in seconds since the genesis block) of the block
            height : (N) is the height of the block in the blockchain
            senderPublicKey : (S) is the public key of the sending accounts for the transaction
            type : (N) is the transaction type (refer to Get Constants for a current list of types)
            deadline : (N) is the deadline (in minutes) for the transaction to be confirmed
            signature : (S) is the digital signature of the transaction
            recipient : (S) is the accounts number of the recipient, if applicable
            recipientRS : (S) is the Reed-Solomon address of the recipient, if applicable
            fullHash : (S) is the full hash of the signed transaction
            signatureHash : (S) is a SHA-256 hash of the transaction signature
            approved : (B) is a boolean indicating if the transaction is approved
                        (only included when includePhasingResult is true and the transaction is phased)
            result : (S) is a string containing the result of the transaction
                        (only included when includePhasingResult is true and the transaction is phased)
            executionHeight : (N) is the height the transaction was executed
                        (only included when includePhasingResult is true and the transaction is phased)
            transaction : (S) is the transaction ID
            version : (N) is the transaction version number
            phased : (B) is true if the transaction is phased, false otherwise
            ecBlockId : (N) is the economic clustering block ID
            ecBlockHeight : (N) is the economic clustering block height
            attachment : (O) is an object containing any additional data needed for the transaction, if applicable
            lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            requestProcessingTime : (N) is the API request processing time (in millisec)

            Note: The block, blockTimestamp and confirmations fields are omitted for unconfirmed transactions.
            Double-spending transactions are not retrieved.

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
                (WP) Wrapper Meta-parameter


        """

        # Required parameters
        self.currency = currency
        self.account = account
        self.withoutWitelist = withoutWitelist
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["accounts"] = self.account

        if self.withoutWitelist:
            self.data["withoutWitelist"] = self.withoutWitelist

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetCurrencyPhasedTransactions, self).__init__(rt="getCurrencyPhasedTransactions", data=self.data)

    def run(self):
        super(GetCurrencyPhasedTransactions, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetCurrencyPhasedTransactions, self).getData(key)                           # calls 'BaseGet.getData()'
