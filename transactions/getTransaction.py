# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetTransaction(Parent):

    def __init__(self,transaction=None, fullHash = None, includePhasingResult = False, rb=None ):
        """
            Get a transaction object given a transaction ID.

            GetTransaction take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Transaction

            REQUEST
            :param transaction : is the transaction ID (S) (O)
            :param fullHash : is the full hash of the transaction (optional if transaction ID is provided)
            :param includePhasingResult : is true to retrieve execution status of each phased transaction (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return sender : (S) is the account ID of the sender
            :return senderRS : (S) is the Reed-Solomon address of the sender
            :return feeNQT : (S) is the fee (in NQT) of the transaction
            :return amountNQT : (S) is the amount (in NQT) of the transaction
            :return transactionIndex : (N) is a zero-based index giving the order of the transaction in its block
            :return timestamp : (N) is the time (in seconds since the genesis block) of the transaction
            :return referencedTransactionFullHash : (S) is the full hash of a transaction referenced by this one, omitted if no previous transaction is referenced
            :return confirmations : (N) is the number of transaction confirmations
            :return subtype : (N) is the transaction subtype (refer to Get Constants for a current list of subtypes)
            :return block : (S) is the ID of the block containing the transaction
            :return blockTimestamp : (N) is the timestamp (in seconds since the genesis block) of the block
            :return height : (N) is the height of the block in the blockchain
            :return senderPublicKey : (S) is the public key of the sending account for the transaction
            :return type : (N) is the transaction type (refer to Get Constants for a current list of types)
            :return deadline : (N) is the deadline (in minutes) for the transaction to be confirmed
            :return signature : (S) is the digital signature of the transaction
            :return recipient : (S) is the account number of the recipient, if applicable
            :return recipientRS : (S) is the Reed-Solomon address of the recipient, if applicable
            :return fullHash : (S) is the full hash of the signed transaction
            :return signatureHash : (S) is a SHA-256 hash of the transaction signature
            :return approved : (B) is a boolean indicating if the transaction is approved (only included when includePhasingResult is true and the transaction is phased)
            :return result : (S) is a string containing the result of the transaction (only included when includePhasingResult is true and the transaction is phased)
            :return executionHeight : (N) is the height the transaction was executed (only included when includePhasingResult is true and the transaction is phased)
            :return transaction : (S) is the transaction ID
            :return version : (N) is the transaction version number
            :return phased : (B) is true if the transaction is phased, false otherwise
            :return ecBlockId : (N) is the economic clustering block ID
            :return ecBlockHeight : (N) is the economic clustering block height
            :return attachment : (O) is an object containing any additional data needed for the transaction, if applicable
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self._transaction = transaction
        self._fullHash = fullHash
        self._includePhasingResult = includePhasingResult
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["transaction"]  = self.transaction
        self.data["fullHash"]  = self.fullHash
        self.data["includePhasingResult"] = self.includePhasingResult

        super(GetTransaction, self).__init__(rt = "getTransaction", data=self.data, rb=self.rb)

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, value):
        self._transaction = value

    @property
    def fullHash(self):
        return self._fullHash

    @fullHash.setter
    def fullHash(self, value):
        self._fullHash = value

    @property
    def includePhasingResult(self):
        return self._includePhasingResult

    @includePhasingResult.setter
    def includePhasingResult(self, value):
        self._includePhasingResult = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetTransaction, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetTransaction, self).getData(key)    # calls 'BaseGet.getData()'