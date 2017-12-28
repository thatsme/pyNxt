# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class CurrencyReserveIncrease(Parent):
    def __init__(self, currency=None, amountPerUnitNQT=0, publicKey=None, secretPhrase=None, feeNQT=0, deadline=0, referencedTransactionFullHash=None, broadcast=True, phasing=None, message=None, rec=None):
        """
            Increase the currency reserve of an unissued reservable currency. POST only.

            CurrencyReserveIncrease take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Currency_Reserve_Increase

            REQUEST
            :param currency : is the currency ID (S)
            :param amountPerUnitNQT : (N) is the additional amount (in NQT per QNT of reserveSupply) to reserve (refer to Issue Currency)
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

            Note: An additional amountPerUnitNQT * reserveSupply NQT (beyond what has previously been reserved)
            will be locked until the issuanceHeight is reached. Upon issuance, if the currency is claimable the NQT
            will remain locked until claimed; otherwise the NQT will transfer to the issuing account.
            Also upon issuance, a portion of the reserveSupply QNT will be transfered to each reserving account in
            proportion to the NQT that was contributed.

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
        self._amountPerUnitNQT = amountPerUnitNQT
        self._publicKey = publicKey
        self._secretPhrase = secretPhrase
        self._feeNQT = feeNQT
        self._deadline = deadline

        self._referencedTransactionFullHash = referencedTransactionFullHash
        self._broadcast = broadcast
        self._phasing = phasing
        self._message = message
        self._rec = rec

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["amountPerUnitNQT"] = self.amountPerUnitNQT
        if publicKey:
            self.data["publicKey"] = self.publicKey
        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        if referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash

        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline
        self.data["broadcast"] = self.broadcast


        super(CurrencyReserveIncrease, self).__init__(rt="currencyReserveIncrease", data=self.data, phasing=self.phasing, message=self.message, rec=self.rec)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    @property
    def amountPerUnitNQT(self):
        return self._amountPerUnitNQT

    @amountPerUnitNQT.setter
    def amountPerUnitNQT(self, value):
        self._amountPerUnitNQT = value

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
        super(CurrencyReserveIncrease, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(CurrencyReserveIncrease, self).getData(key)  # calls 'BasePost.getData()'
