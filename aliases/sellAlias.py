# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class SellAlias(Parent):
    def __init__(self, alias = None, aliasName=None, priceNQT=None, secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing = None, message=None, recipientPublicKey=None, rec=None ):
        """
            Buy or sell an alias

            SellAlias take a default 5 parameter as explained in NXT API Documentation

            API is working with  post method, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request


            https://nxtwiki.org/wiki/The_Nxt_API#Sell_Alias

            REQUEST
            :param alias °: is the id of alias (S)
            :param aliasName °: is the name of alias (S)
            :param priceNQT : is the asking price (in NQT) of the alias (sellAlias only)
            :param secretPhrase *: secret Phrase of accounts where we want remove a property ( required or at least ** )
            :param publicKey **: publicKey of accounts where we want remove a property ( does not get in broadcast ) ( required or at least *)
            :param feeNQT : fee for sending transaction if 0 minimum is set ( 100000000 NQT )
            :param deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            :param referencedTransactionFullHash :  creates a chained transaction, meaning that the current transaction
                                            cannot be confirmed unless the referenced transaction is also confirmed (O)
            :param broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            :param phasing : see base/Phasing.py class
            :param message : see base/Message.py class
            :param recipientPublicKey : is the public key of the recipient accounts (O)
                                (only applicable if recipient provided; enhances security of a new accounts)
            :param rec : rec object ( check base/Rec.py) (WP)

            Note: An alias can be transferred rather than sold by setting priceNQT to zero.
            A pending sale can be canceled by selling again to self for a price of zero.

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
        self._alias = alias
        self._aliasName = aliasName
        self._priceNQT = priceNQT
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
        self._recipientPublicKey = recipientPublicKey

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

        super(SellAlias, self).__init__(rt="sellAlias", data=self.data, phasing=self.phasing, message=self.message, rec=self.rec)

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value

    @property
    def aliasName(self):
        return self._aliasName

    @aliasName.setter
    def aliasName(self, value):
        self._aliasName = value

    @property
    def priceNQT(self):
        return self._priceNQT

    @priceNQT.setter
    def priceNQT(self, value):
        self._priceNQT = value

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
        super(SellAlias, self).run()                                     # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(SellAlias, self).getData(key)                       # calls 'BasePost.getData()'
