# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent


class LeaseBalance(Parent):
    def __init__(self, period=1440, recipient=None, recipientPublicKey=None, secretPhrase=None, feeNQT=None, deadline=0,
                 referencedTransactionFullHash=None, broadcast=True, phasing=None, message=None, rec=None):
        """
            Lease the entire guaranteed balance of NXT to another account, after 1440 confirmations

            LeaseBalance take a default 5 parameter as explained in NXT API Documentation

            API is working with POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request


            https://nxtwiki.org/wiki/The_Nxt_API#Lease_Balance

            REQUEST

            :param recipient : is the lessee (recipient) account
            :param period : (N) is the lease period (in number of blocks, 1440 minimum)
            :param recipientPublicKey : is the public key of the lessee (recipient) account (optional, enhances security of a new account)
            :param secretPhrase **: secret Phrase of sender accounts
            :param feeNQT : fee for sending transaction (R) if 0 minimum is set ( 100000000 NQT )
            :param deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            :param referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            :param broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            :param phasing : phasing object ( check base/Phasing.py ) (O) (WP)
            :param message : message object ( check base/message.py ) (O) (WP)
            :param rec : rec object ( check base/Rec.py) (WP)

            RESPONSE
            :return signatureHash : is a SHA-256 hash of the transaction signature (S)
            :return unsignedTransactionBytes : are the unsigned transaction bytes (S)
            :return transactionJSON : is a transaction object (O)  (refer to Get Transaction for details)
            :return broadcasted : is true if the transaction was broadcast, false otherwise (B)
            :return requestProcessingTime : is the API request processing time (in millisec)  (N)
            :return transactionBytes :  are the signed transaction bytes (S)
            :return fullHash : is the full hash of the signed transaction (S)
            :return transaction : is the ID of the newly created transaction (S)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

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
        self.period = period
        self.recipient = recipient
        self.recipientPublicKey = recipientPublicKey
        self.secretPhrase = secretPhrase
        self.referencedTransactionFullHash = referencedTransactionFullHash
        self.broadcast = broadcast

        if self.period < 1440:
            self.period = 1440

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
        self.rec = rec

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["recipient"] = self.recipient
        self.data["period"] = self.period
        if self.recipientPublicKey:
            self.data["recipientPublicKey"] = self.recipientPublicKey
        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        if referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline
        self.data["broadcast"] = self.broadcast

        # self.data["message"] = self.message
        super(LeaseBalance, self).__init__(rt="leaseBalance", data=self.data, phasing=self.phasing, message=self.message, rec=self.rec)

    def run(self):
        super(LeaseBalance, self).run()  # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(LeaseBalance, self).getData(key)  # calls 'BasePost.getData()'

