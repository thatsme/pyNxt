# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class DgsFeedback(Parent):
    def __init__(self, purchase = None, fmessage=None, secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing = None, message=None, rec=None ):
        """
            Give feedback about a purchased product after delivery.

            DgsFeedback take a default 5 parameter as explained in NXT API Documentation

            API is working with POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request

            https://nxtwiki.org/wiki/The_Nxt_API#Dgs_Feedback

            REQUEST
            :param purchase : is the purchase order ID (S)
            :param message is unencrypted (public) feedback text up to 1000 bytes
            :param * secretPhrase : secret Phrase of accounts where we want remove a property ( required or at least ** )
            :param ** publicKey : publicKey of accounts where we want remove a property ( does not get in broadcast ) ( required or at least *)
            :param feeNQT : fee for sending transaction if 0 minimum is set ( 100000000 NQT )
            :param deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            :param referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            :param broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            :param phasing : phasing object ( check base/Phasing.py ) (WP)
            :param message : message object ( check base/message.py ) (WP)
            :param rec : rec object ( check base/Rec.py) (WP)

            Note: The unencrypted message parameter is used for public feedback, but in addition or instead,
            an encrypted message can be used for private feedback to the seller and/or an encrypted message can be sent to self (buyer)
            although the current NRS client does not recognize non-public feedback messages.

            RESPONSE (Create transaction response)
            :param signatureHash : is a SHA-256 hash of the transaction signature (S)
            :param unsignedTransactionBytes : are the unsigned transaction bytes (S)
            :param transactionJSON : is a transaction object (refer to Get Transaction for details) (O)
            :param broadcasted : is true if the transaction was broadcast, false otherwise (B)
            :param requestProcessingTime : is the API request processing time (in millisec) (N)
            :param transactionBytes : are the signed transaction bytes (S)
            :param fullHash : is the full hash of the signed transaction (S)
            :param transaction : is the ID of the newly created transaction (S)

            Legenda
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
        self.purchase = purchase
        self.fmessage = fmessage
        self.publicKey = publicKey
        self.secretPhrase = secretPhrase
        if feeNQT == 0:
            self.feeNQT = 100000000
        else:
            self.feeNQT = feeNQT

        # Optional parameters
        self.referencedTransactionFullHash = referencedTransactionFullHash
        self.broadcast = broadcast

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

        self.data["purchase"] = self.purchase
        self.data["message"] = self.fmessage

        if publicKey:
            self.data["publicKey"] = self.publicKey
        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline
        if self.referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash
        if self.broadcast:
            self.data["broadcast"] = self.broadcast

        super(DgsFeedback, self).__init__(rt="dgsFeedback", data=self.data, phasing=self.phasing, message=self.message, rec=self.rec)

    def run(self):
        super(DgsFeedback, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(DgsFeedback, self).getData(key)  # calls 'BasePost.getData()'
