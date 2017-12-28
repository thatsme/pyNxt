# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class CurrencyMint(Parent):
    def __init__(self, currency=None, nonce=0, unit=0, counter=0, publicKey=None, secretPhrase=None, feeNQT=0, deadline=0, referencedTransactionFullHash=None, broadcast=True, phasing=None, message=None, rec=None):
        """
            Submit a valid computed nonce to the blockchain in return for newly minted currency. POST only.

            CurrencyMint take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Currency_Mint

            REQUEST
            :param currency : is the mintable currency ID (S)
            :param nonce : is the computed nonce (S)
            :param units : is the amount (in QNT) of currency to mint (S)
            :param counter : (N) is the counter associated with the minting account
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

            Note: The hash of nonce must be less than targetBytes provided by Get Minting Target for given
            units and counter. counter must be increased with each submission.

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
        self._nonce = nonce
        self._unit = unit
        self._counter = counter
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
        self.data["nonce"] = self.nonce
        self.data["unit"] = self.unit
        self.data["counter"] = self.counter
        if publicKey:
            self.data["publicKey"] = self.publicKey
        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        if referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash

        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline
        self.data["broadcast"] = self.broadcast

        super(CurrencyMint, self).__init__(rt="currencyMint", data=self.data, phasing=self.phasing, message=self.message, rec=self.rec)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    @property
    def nonce(self):
        return self._nonce

    @nonce.setter
    def nonce(self, value):
        self._nonce = value

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, value):
        self._counter = value

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
        super(CurrencyMint, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(CurrencyMint, self).getData(key)  # calls 'BasePost.getData()'
