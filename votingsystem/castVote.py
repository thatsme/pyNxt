# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class CastVote(Parent):
    def __init__(self, transactionFullHash=None, revealedSecret = None, revealedSecretIsText=None, publicKey = None, secretPhrase=None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=True, phasing = None, message=None ):
        """
            Cast a vote on a poll. POST only.

            CastVote take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Cast_Vote

            REQUEST
            :param poll is the poll ID
            :param vote00 is an integer within the allowed range to vote for option (answer) 0 (optional if minNumberOfOptions met, default is -128)
            :param vote01 is an integer within the allowed range to vote for option (answer) 1 (optional if minNumberOfOptions met, default is -128)
            :param vote02 is an integer within the allowed range to vote for option (answer) 2 (optional if minNumberOfOptions met, default is -128)
            :param publicKey *: publicKey of sender accounts ( does not get in broadcast )
            :param secretPhrase **: secret Phrase of sender accounts
            :param feeNQT : fee for sending transaction (R) if 0 minimum is set ( 100000000 NQT )
            :param deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            :param referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            :param broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            :param phasing : phasing object ( check base/Phasing.py ) (O) (WP)
            :param message : message object ( check base/message.py ) (O) (WP)

            Note: The allowed vote values are integers between minRangeValue and maxRangeValue, inclusive.
            This range, along with the minimum and maximum number of options that can and must be voted on are specified
            when the poll is created. Refer to Create Poll.

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
        self.transactionFullHash = transactionFullHash
        self.revealedSecret = revealedSecret
        self.revealedSecretIsText = revealedSecretIsText

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
        self.data["transactionFullHash"] = self.transactionFullHash
        self.data["revealedSecret"] = self.revealedSecret
        self.data["revealedSecretIsText"] = self.revealedSecretIsText

        self.data["publicKey"] = self.publicKey
        self.data["secretPhrase"] = self.secretPhrase
        self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash
        self.data["broadcast"] = self.broadcast
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline


        super(CastVote, self).__init__(rt="castVote", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(CastVote, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(CastVote, self).getData(key)  # calls 'BasePost.getData()'
