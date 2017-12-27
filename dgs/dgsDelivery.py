 # -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class DgsDelivery(Parent):
    def __init__(self, purchase = None, discountNQT=0, goodsToEncrypt=None, goodsIsText=False, goodsData=None, goodsNonce=None, secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing = None, message=None, rec=None ):
        """
            Deliver a product.

            DgsDelivery take a default 5 parameter as explained in NXT API Documentation

            API is working with POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request

            https://nxtwiki.org/wiki/The_Nxt_API#Dgs_Delivery

            REQUEST
            :param purchase : is the purchase order ID (S)
            :param discountNQT : is a discount (in NQT) off the selling price (N) (O) (optional, default is zero)
            :param goodsToEncrypt : is the product, a text or a hex string to be encrypted (S) (optional if goodsData provided)
            :param goodsIsText : is false if goodsToEncrypt is a hex string (B) (O)
            :param goodsData : is AES-encrypted (using Encrypt To) goodsToEncrypt, up to 1000 bytes long (required only if secretPhrase is omitted)
            :param goodsNonce : is the unique nonce associated with the encrypted data (required only if secretPhrase is omitted)
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

            Note: If the encrypted goods data is longer than 1000 bytes, use a prunable encrypted message to deliver the goods.

            RESPONSE (Create transaction response)
            :return signatureHash : is a SHA-256 hash of the transaction signature (S)
            :return unsignedTransactionBytes : are the unsigned transaction bytes (S)
            :return transactionJSON : is a transaction object (refer to Get Transaction for details) (O)
            :return broadcasted : is true if the transaction was broadcast, false otherwise (B)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)
            :return transactionBytes : are the signed transaction bytes (S)
            :return fullHash : is the full hash of the signed transaction (S)
            :return transaction : is the ID of the newly created transaction (S)

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
        self._purchase = purchase
        self._discountNQT = discountNQT
        self._goodsToEncrypt = goodsToEncrypt
        self._goodsIsText = goodsIsText
        self._goodsData = goodsData
        self._goodsNonce = goodsNonce
        self._publicKey = publicKey
        self._secretPhrase = secretPhrase
        self._feeNQT = feeNQT
        self._deadline = deadline

        # Optional parameters
        self._referencedTransactionFullHash = referencedTransactionFullHash
        self._broadcast = broadcast

        self._phasing = phasing
        self._message = message
        self._rec = rec

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["purchase"] = self.purchase
        self.data["discountNQT"] = self.discountNQT

        if self.goodsToEncrypt:
            self.data["goodsToEncrypt"] = self.goodsToEncrypt
        if self.goodsIsText:
            self.data["goodsIsText"] = self.goodsIsText
        if self.goodsData:
            self.data["goodsData"] = self.goodsData

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

        super(DgsDelivery, self).__init__(rt="dgsDelivery", data=self.data, phasing=self.phasing, message=self.message, rec=self.rec)

    @property
    def purchase(self):
        return self._purchase

    @purchase.setter
    def purchase(self, value):
        self._purchase = value

    @property
    def discountNQT(self):
        return self._discountNQT

    @discountNQT.setter
    def discountNQT(self, value):
        self._discountNQT = value

    @property
    def goodsToEncrypt(self):
        return self._goodsToEncrypt

    @goodsToEncrypt.setter
    def goodsToEncrypt(self, value):
        self._goodsToEncrypt = value

    @property
    def goodsIsText(self):
        return self._goodsIsText

    @goodsIsText.setter
    def goodsIsText(self, value):
        self._goodsIsText = value

    @property
    def goodsData(self):
        return self._goodsData

    @goodsData.setter
    def goodsData(self, value):
        self._goodsData = value

    @property
    def goodsNonce(self):
        return self._goodsNonce

    @goodsNonce.setter
    def goodsNonce(self, value):
        self._goodsNonce = value

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

    def run(self):
        super(DgsDelivery, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(DgsDelivery, self).getData(key)  # calls 'BasePost.getData()'
