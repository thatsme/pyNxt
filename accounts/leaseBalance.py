# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class LeaseBalance(Parent):
    def __init__(self, recipient=None, period=0, publicKey=None, secretPhrase=None, feeNQT=None, deadline=0, referencedTransactionFullHash=None, broadcast=True, phasing=None, message=None):
        """
            Lease the entire guaranteed balance of NXT to another accounts, after 1440 confirmations

            LeaseBalance take a default 5 parameter as explained in NXT API Documentation

            Class is working with POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request


            https://nxtwiki.org/wiki/The_Nxt_API#Lease_Balance

            REQUEST
            recipient : accounts id of recipient (R)
            period is the lease period (in number of blocks, 1440 minimum)
            recipientPublicKey is the public key of the lessee (recipient) accounts (optional, enhances security of a new accounts)
            * publicKey : publicKey of sender accounts ( does not get in broadcast )
            ** secretPhrase : secret Phrase of sender accounts
            feeNQT : fee for sending transaction (R) if 0 minimum is set ( 100000000 NQT )
            deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            phasing : phasing object ( check base/Phasing.py )
            message : message object ( check base/message.py )

            RESPONSE
            signatureHash : is a SHA-256 hash of the transaction signature (S)
            unsignedTransactionBytes : are the unsigned transaction bytes (S)
            transactionJSON : is a transaction object (O)  (refer to Get Transaction for details)
            broadcasted : is true if the transaction was broadcast, false otherwise (B)
            requestProcessingTime : is the API request processing time (in millisec)  (N)
            transactionBytes :  are the signed transaction bytes (S)
            fullHash : is the full hash of the signed transaction (S)
            transaction : is the ID of the newly created transaction (S)
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

        # Required parameters
        self.recipient = recipient
        self.period = period
        self.publicKey = publicKey
        self.secretPhrase = secretPhrase
        self.referencedTransactionFullHash = referencedTransactionFullHash
        self.broadcast = broadcast

        if feeNQT == 0:
            self.feeNQT = 100000000
        else:
            self.feeNQT = feeNQT

        if deadline == 0:
            self.deadline = 60
        else:
            self.deadline = deadline

        self.phasing = phasing
        self.message = message

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["recipient"] = self.recipient
        self.data["period"] = self.period
        if publicKey:
            self.data["publicKey"] = self.publicKey
        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        if referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline
        self.data["broadcast"] = self.broadcast

        super(LeaseBalance, self).__init__(rt="leaseBalance", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(LeaseBalance, self).run()                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(LeaseBalance, self).getData(key)           # calls 'BasePost.getData()'

