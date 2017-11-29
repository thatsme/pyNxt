# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class PlaceBidOrder(Parent):
    def __init__(self, asset = None, quantityQNT=0, priceNQT=0, secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing = None, message=None ):
        """
            Place an asset order.

            PlaceBidOrder take a default 5 parameter as explained in NXT API Documentation

            Class is working with POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request


            https://nxtwiki.org/wiki/The_Nxt_API#Place_Bid_Order

            REQUEST
            asset : is the asset ID of the asset being ordered
            quantityQNT : is the amount (in QNT) of the asset being ordered
            priceNQT : is the bid/ask price (in NQT)
            * secretPhrase : secret Phrase of account where we want remove a property ( required or at least ** )
            ** publicKey : publicKey of account where we want remove a property ( does not get in broadcast ) ( required or at least *)
            feeNQT : fee for sending transaction if 0 minimum is set ( 100000000 NQT )
            deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            phasing : phasing object ( check base/Phasing.py )
            message : message object ( check base/message.py )

            RESPONSE (Create transaction response)
            signatureHash : is a SHA-256 hash of the transaction signature (S)
            unsignedTransactionBytes : are the unsigned transaction bytes (S)
            transactionJSON : is a transaction object (refer to Get Transaction for details) (O)
            broadcasted : is true if the transaction was broadcast, false otherwise (B)
            requestProcessingTime : is the API request processing time (in millisec) (N)
            transactionBytes : are the signed transaction bytes (S)
            fullHash : is the full hash of the signed transaction (S)
            transaction : is the ID of the newly created transaction (S)

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
                (O) Object
                >   Array Element
                (WP) Wrapper specific parameter


        """

        # Required parameters
        self.asset = asset
        self.quantityQNT = quantityQNT
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

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["asset"] = self.asset
        self.data["quantityQNT"] = self.quantityQNT
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

        super(PlaceBidOrder, self).__init__(rt="placeBidOrder", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(PlaceBidOrder, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(PlaceBidOrder, self).getData(key)  # calls 'BasePost.getData()'
