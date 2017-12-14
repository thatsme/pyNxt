# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountPhasedTransactions(Parent):

    def __init__(self, account=None, ri=None, rb=None):
        """
            Get pending phased transactions associated with an accounts given the accounts ID in reverse chronological creation order.

            GetAccountPhasedTransactions take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Phased_Transactions

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return sender : is the accounts ID of the sender (S)
            :return senderRS : is the Reed-Solomon address of the sender (S)
            :return feeNQT : is the fee (in NQT) of the transaction (S)
            :return amountNQT : is the amount (in NQT) of the transaction (S)
            :return transactionIndex : is a zero-based index giving the order of the transaction in its block (N)
            :return timestamp : is the time (in seconds since the genesis block) of the transaction (N)
            :return referencedTransactionFullHash : is the full hash of a transaction referenced by this one, omitted if no previous transaction is referenced (S)
            :return confirmations : is the number of transaction confirmations (N)
            :return subtype : is the transaction subtype (refer to Get Constants for a current list of subtypes) (N)
            :return block : is the ID of the block containing the transaction (S)
            :return blockTimestamp : is the timestamp (in seconds since the genesis block) of the block (N)
            :return height : is the height of the block in the blockchain
            :return senderPublicKey : is the public key of the sending accounts for the transaction (S)
            :return type : is the transaction type (refer to Get Constants for a current list of types) (N)
            :return deadline : is the deadline (in minutes) for the transaction to be confirmed (N)
            :return signature : is the digital signature of the transaction (S)
            :return recipient : is the accounts number of the recipient, if applicable (S)
            :return recipientRS : is the Reed-Solomon address of the recipient, if applicable (S)
            :return fullHash : is the full hash of the signed transaction (S)
            :return signatureHash : is a SHA-256 hash of the transaction signature (S)
            :return approved : is a boolean indicating if the transaction is approved  (B) (only included when includePhasingResult is true and the transaction is phased)
            :return result : is a string containing the result of the transaction (S) (only included when includePhasingResult is true and the transaction is phased)
            :return executionHeight : is the height the transaction was executed (N) (only included when includePhasingResult is true and the transaction is phased)
            :return transaction : is the transaction ID (S)
            :return version : is the transaction version number (N)
            :return phased : is true if the transaction is phased, false otherwise (B)
            :return ecBlockId : is the economic clustering block ID (N)
            :return ecBlockHeight : is the economic clustering block height (N)
            :return attachment : is an object containing any additional data needed for the transaction, if applicable (O)
            :return lastBlock : is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock) (S)
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

        self.account = account
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account

        super(GetAccountPhasedTransactions, self).__init__(rt = "getAccountPhasedTransactions", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetAccountPhasedTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountPhasedTransactions, self).getData(key)    # calls 'BaseGet.getData()'