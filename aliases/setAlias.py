# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class SetAlias(Parent):
    def __init__(self, aliasName = None, aliasURI=None, secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing = None, message=None, recipientPublicKey=None, ecBlockId=None, ecBlockHeight=None ):
        """
            Create and/or assign an alias.

            SetAlias take a default 5 parameter as explained in NXT API Documentation ( is deadLine requested or not ? )

            Class is working with POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Response


            https://nxtwiki.org/wiki/The_Nxt_API#Set_Alias

            REQUEST
            aliasName : is the name of the alias ( required )
            aliasURI : is the URI associated within the aliasName (optional)
            * secretPhrase : secret Phrase of account where we want remove a property ( required or at lease ** )
            ** publicKey : publicKey of account where we want remove a property ( does not get in broadcast ) ( required or at least *)
            *** feeNQT : fee for sending transaction if 0 minimum is set ( 100000000 NQT )
            deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            referencedTransactionFullHash :
            broadcast :
            phasing :
            message :
            recipientPublicKey :
            ecBlockId : is the EC (Economic Cluster) block height (N)
            ecBlockHeight : is the EC (Economic Cluster) block id (S)

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

            NB. The transaction ID is also the alias ID.

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
        self.aliasName = aliasName
        self.aliasURI = aliasURI
        self.publicKey = publicKey
        self.secretPhrase = secretPhrase
        if feeNQT == 0:
            self.feeNQT = 200000000
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

        self.data["aliasURI"] = self.aliasURI
        self.data["aliasName"] = self.aliasName
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

        super(SetAlias, self).__init__(rt="setAlias", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(SetAlias, self).run()                                     # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(SetAlias, self).getData(key)                       # calls 'BasePost.getData()'
