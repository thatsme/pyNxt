# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class ScheduleCurrencyBuy(Parent):
    def __init__(self, currency=None, rateNQT=None, units=None, offerIssuer=None, transactionJSON=None, transactionBytes=None, prunableAttachmentJSON=None, adminPassword=None, publicKey = None, secretPhrase=None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=True, phasing = None, message=None, rec=None ):
        """
            Publish an exchange offer for an exchangeable currency. POST only.

            ScheduleCurrencyBuy take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Schedule_Currency_Buy ( NO DOC )

            REQUEST
            :param currency : is the currency ID (S)
            :param rateNQT :
            :param units :
            :param offerIssuer :
            :param transactionJSON :
            :param transactionBytes :
            :param prunableAttachmentJSON :

            :param publicKey *: publicKey of sender accounts ( does not get in broadcast )
            :param secretPhrase **: secret Phrase of sender accounts
            :param feeNQT : fee for sending transaction (R) if 0 minimum is set ( 100000000 NQT )
            :param deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            :param referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            :param broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            :param phasing : phasing object ( check base/Phasing.py ) (O) (WP)
            :param message : message object ( check base/message.py ) (O) (WP)
            :param rec : rec object ( check base/Rec.py) (WP)

            Response: Refer to Create Transaction Response. The transaction ID is also the offer ID.

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
        self._currency = currency
        self._rateNQT = rateNQT
        self._units = units
        self._offerIssuer = offerIssuer
        self._transactionJSON = transactionJSON
        self._transactionBytes = transactionBytes
        self._prunableAttachmentJSON = prunableAttachmentJSON
        self._adminPassword = adminPassword

        self._publicKey = publicKey
        self._secretPhrase = secretPhrase
        self._referencedTransactionFullHash = referencedTransactionFullHash
        self._broadcast = broadcast

        self._feeNQT = feeNQT
        self._deadline = deadline
        self._phasing = phasing
        self._message = message
        self._rec = rec

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["rateNQT"] = self.rateNQT
        self.data["units"] = self.units
        self.data["offerIssuer"] = self.offerIssuer
        self.data["transactionJSON"] = self.transactionJSON
        self.data["transactionBytes"] = self.transactionBytes
        self.data["prunableAttachmentJSON"] = self.prunableAttachmentJSON
        self.data["adminPassword"] = self.adminPassword

        if self.publicKey:
            self.data["publicKey"] = self.publicKey

        if self.secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase

        if self.referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash

        self.data["broadcast"] = self.broadcast
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline

        super(ScheduleCurrencyBuy, self).__init__(rt="scheduleCurrencyBuy", data=self.data, rec=self.rec)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    @property
    def rateNQT(self):
        return self._rateNQT

    @rateNQT.setter
    def rateNQT(self, value):
        self._rateNQT = value

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value):
        self._units = value

    @property
    def offerIssuer(self):
        return self._offerIssuer

    @offerIssuer.setter
    def offerIssuer(self, value):
        self._offerIssuer = value

    @property
    def transactionJSON(self):
        return self._transactionJSON

    @transactionJSON.setter
    def transactionJSON(self, value):
        self._transactionJSON = value

    @property
    def transactionBytes(self):
        return self._transactionBytes

    @transactionBytes.setter
    def transactionBytes(self, value):
        self._transactionBytes = value

    @property
    def prunableAttachmentJSON(self):
        return self._prunableAttachmentJSON

    @prunableAttachmentJSON.setter
    def prunableAttachmentJSON(self, value):
        self._prunableAttachmentJSON = value

    @property
    def adminPassword(self):
        return self._adminPassword

    @adminPassword.setter
    def adminPassword(self, value):
        self._adminPassword = value

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
        super(ScheduleCurrencyBuy, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(ScheduleCurrencyBuy, self).getData(key)  # calls 'BasePost.getData()'
