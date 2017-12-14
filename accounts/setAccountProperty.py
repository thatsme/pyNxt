# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class SetAccountProperty(Parent):
    def __init__(self, recipient = None, property=None, value=None, secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing = None, message=None, rec=None ):
        """
            Set accounts property.

            SetAccountProperty take a default 5 parameter as explained in NXT API Documentation

            API is working with  POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request

            https://nxtwiki.org/wiki/The_Nxt_API#Set_Account_Property

            REQUEST
            :param property : is the name of the property (S) (R)
            :param recipient : is the accounts where a property should be removed (S) (O)
            :param setter : is the accounts who did set the property (S) (S)
            :param secretPhrase *: secret Phrase of accounts where we want remove a property ( required or at lease ** )
            :param publicKey **: publicKey of accounts where we want remove a property ( does not get in broadcast ) ( required or at least *)
            :param feeNQT : fee for sending transaction if 0 minimum is set ( 100000000 NQT ) (N)
            :param deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
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
        self.recipient = recipient
        self.property = property
        self.publicKey = publicKey
        self.secretPhrase = secretPhrase
        if feeNQT == 0:
            self.feeNQT = 100000000
        else:
            self.feeNQT = feeNQT

        if deadline == 0:
            self.deadline = 60
        else:
            self.deadline = deadline

        # Optional parameters
        self.referencedTransactionFullHash = referencedTransactionFullHash
        self.broadcast = broadcast
        self.value = value

        self.phasing = phasing
        self.message = message
        self.rec = rec

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["recipient"] = self.recipient
        self.data["value"] = self.value
        self.data["property"] = self.property
        self.data["broadcast"] = self.broadcast

        if publicKey:
            self.data["publicKey"] = self.publicKey
        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline
        if self.referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash

        super(SetAccountProperty, self).__init__(rt="setAccountProperty", data=self.data, phasing=self.phasing, message=self.message, rec=self.rec)

    def run(self):
        super(SetAccountProperty, self).run()                           # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(SetAccountProperty, self).getData(key)             # calls 'BasePost.getData()'
