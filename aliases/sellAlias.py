# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class SellAlias(Parent):
    def __init__(self, alias = None, aliasName=None, priceNQT=None, secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing = None, message=None, recipientPublicKey=None, ecBlockId=None, ecBlockHeight=None ):
        """
            Buy or sell an alias

            SellAlias take a default 5 parameter as explained in NXT API Documentation

            Class is working with  post method, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request


            https://nxtwiki.org/wiki/The_Nxt_API#Sell_Alias

            REQUEST
            ° alias : is the id of alias (S)
            ° aliasName : is the name of alias (S)
            priceNQT : is the asking price (in NQT) of the alias (sellAlias only)
            * secretPhrase : secret Phrase of account where we want remove a property ( required or at least ** )
            ** publicKey : publicKey of account where we want remove a property ( does not get in broadcast ) ( required or at least *)
            *** feeNQT : fee for sending transaction if 0 minimum is set ( 100000000 NQT )
            deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            referencedTransactionFullHash :  creates a chained transaction, meaning that the current transaction
                                            cannot be confirmed unless the referenced transaction is also confirmed (O)
            broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            phasing : see base/Phasing.py class
            message : see base/Message.py class
            recipientPublicKey : is the public key of the recipient account (O)
                                (only applicable if recipient provided; enhances security of a new account)
            ecBlockId :
            ecBlockHeight :

            Note: An alias can be transferred rather than sold by setting priceNQT to zero.
            A pending sale can be canceled by selling again to self for a price of zero.

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
        """

        # Required parameters
        self.alias = alias
        self.aliasName = aliasName
        self.priceNQT = priceNQT
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

        self.recipientPublicKey = recipientPublicKey
        self.ecBlockId = ecBlockId
        self.ecBlockHeight = ecBlockHeight

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["alias"] = self.alias
        self.data["aliasName"] = self.aliasName
        self.data["priceNQT"] = self.priceNQT
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

        if self.recipientPublicKey:
            self.data["recipientPublicKey"] = self.recipientPublicKey

        if self.ecBlockId:
            self.data["ecBlockId"] = self.ecBlockId

        if self.ecBlockHeight:
            self.data["ecBlockHeight"] = self.ecBlockHeight

        super(SellAlias, self).__init__(rt="sellAlias", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(SellAlias, self).run()                                     # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(SellAlias, self).getData(key)                       # calls 'BasePost.getData()'
