# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class SendMessage(Parent):
    def __init__(self, recipient = None, recipientPublicKey=None,  secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing = None, message=None, rec=None ):
        """
            SendMessage take a default 5 parameter as explained in NXT API Documentation

            API is working with POST method only, and create a transaction, for more info about transactions please refer to

            https://nxtwiki.org/wiki/The_Nxt_API#Send_Message

            REQUEST
            :param recipient : is the account ID of the recipient (O)
            :param publicKey : is the public key of the account (optional if secretPhrase provided)
            :param recipientPublicKey * publicKey of recipient accounts ( does not get in broadcast )
            :param secretPhrase **: secret Phrase of sender accounts
            :param feeNQT : fee for sending transaction (R) if 0 minimum is set ( 100000000 NQT )
            :param deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            :param referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            :param broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            :param phasing : phasing object ( check base/Phasing.py ) (O) (WP)
            :param message : message object ( check base/message.py ) (O) (WP)
            :param rec : rec object ( check base/Rec.py) (WP)

            RESPONSE (Create transaction response)
            :return signatureHash : is a SHA-256 hash of the transaction signature (S)
            :return unsignedTransactionBytes : are the unsigned transaction bytes (S)
            :return transactionJSON : is a transaction object (refer to Get Transaction for details) (O)
            :return broadcasted : is true if the transaction was broadcast, false otherwise (B)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)
            :return transactionBytes : are the signed transaction bytes (S)
            :return fullHash : is the full hash of the signed transaction (S)
            :return transaction : is the ID of the newly created transaction (S)

            Note:
            Any combination (including none or all) of the three options plain message, messageToEncrypt, and messageToEncryptToSelf
            will be included in the transaction. However, one and only one prunable message may be included in a single transaction
            if there is not already a message of the same type (either plain or encrypted).

            The encryptedMessageData-encryptedMessageNonce pair or the encryptToSelfMessageData-encryptToSelfMessageNonce pair can be
            the output of Encrypt To


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
        self._recipient = recipient
        self._publicKey = publicKey
        self._secretPhrase = secretPhrase
        self._feeNQT = feeNQT
        self._deadline = deadline

        # Optional parameters
        self._referencedTransactionFullHash = referencedTransactionFullHash
        self._broadcast = broadcast

        self._phasing = phasing
        self._message = message
        self._recipientPublicKey = recipientPublicKey
        self._rec = rec

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["recipient"] = self.recipient
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

        super(SendMessage, self).__init__(rt="sendMessage", data=self.data, phasing=self.phasing, message=self.message, rec=self.rec)

    @property
    def recipient(self):
        return self._recipient

    @recipient.setter
    def recipient(self, value):
        self._recipient = value

    @property
    def publicKey(self):
        return self._publicKey

    @publicKey.setter
    def publicKey(self, value):
        self._publicKey = value

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def referencedTransactionFullHash(self):
        return self._referencedTransactionFullHash

    @referencedTransactionFullHash.setter
    def referencedTransactionFullHash(self, value):
        self._referencedTransactionFullHash = value

    @property
    def broadcast(self):
        return self._broadcast

    @broadcast.setter
    def broadcast(self, value):
        self._broadcast = value

    @property
    def feeNQT(self):
        return self._feeNQT

    @feeNQT.setter
    def feeNQT(self, value):
        if value == 0:
            self._feeNQT = 100000000
        else:
            self._feeNQT = value

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        if value == 0:
            self._deadline = 60
        else:
            self._deadline = value

    @property
    def phasing(self):
        return self._phasing

    @phasing.setter
    def phasing(self, value):
        self._phasing = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def rec(self):
        return self._rec

    @rec.setter
    def rec(self, value):
        self._rec = value

    @property
    def recipientPublicKey(self):
        return self._recipientPublicKey

    @recipientPublicKey.setter
    def recipientPublicKey(self, value):
        self._recipientPublicKey = value


    def run(self):
        super(SendMessage, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(SendMessage, self).getData(key)  # calls 'BasePost.getData()'
