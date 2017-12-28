# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class PublishExchangeOffer(Parent):
    def __init__(self, currency=None, buyRateNQT=None, sellRateNQT=None, totalBuyLimit=0, totalSellLimit=0, initialBuySupply=0, initialSellSupply=0, expirationHeight=None, publicKey = None, secretPhrase=None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=True, phasing = None, message=None, rec=None ):
        """
            Publish an exchange offer for an exchangeable currency. POST only.

            PublishExchangeOffer take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Publish_Exchange_Offer

            REQUEST
            :param currency : is the currency ID (S)
            :param buyRateNQT : is the offered buy rate (in NQT per QNT) (N)
            :param sellRateNQT : is the offered sell rate (in NQT per QNT) (N)
            :param totalBuyLimit : is the cumulative limit (in QNT) of currency buys (N)
            :param totalSellLimit : is the cumulative limit (in QNT) of currency sells (N)
            :param initialBuySupply : is the initial amount (in QNT) of currency offered to buy, cannot exceed totalBuyLimit
            :param initialSellSupply : is the initial amount (in QNT) of currency offered to sell, cannot exceed totalSellLimit
            :param expirationHeight : is the blockchain height for expiration of the offer

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

            Notes: Each time currency is bought in response to an exchange request to sell currency (refer to Currency Sell),
            totalBuyLimit is reduced and the supply of currency offered to sell increases by the amount bought.
            When totalBuyLimit becomes zero, the buy offer is withdrawn. These same notes apply if buy and sell are interchanged.
            Only the most recent offer associated with an account is valid, even if an earlier offer by that account has not yet
            expired or reached its limits.

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
        self._buyRateNQT = buyRateNQT
        self._sellRateNQT = sellRateNQT
        self._totalBuyLimit = totalBuyLimit
        self._totalSellLimit = totalSellLimit
        self._initialBuySupply = initialBuySupply
        self._initialSellSupply = initialSellSupply
        self._expirationHeight = expirationHeight

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
        self.data["buyRateNQT"] = self.buyRateNQT
        self.data["sellRateNQT"] = self.sellRateNQT
        self.data["totalBuyLimit"] = self.totalBuyLimit
        self.data["totalSellLimit"] = self.totalSellLimit
        self.data["initialBuySupply"] = self.initialBuySupply
        self.data["initialSellSupply"] = self.initialSellSupply
        self.data["expirationHeight"] = self.expirationHeight

        if self.publicKey:
            self.data["publicKey"] = self.publicKey

        if self.secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase

        if self.referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash

        self.data["broadcast"] = self.broadcast
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline

        super(PublishExchangeOffer, self).__init__(rt="publishExchangeOffer", data=self.data, rec=self.rec)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    @property
    def buyRateNQT(self):
        return self._buyRateNQT

    @buyRateNQT.setter
    def buyRateNQT(self, value):
        self._buyRateNQT = value

    @property
    def sellRateNQT(self):
        return self._sellRateNQT

    @sellRateNQT.setter
    def sellRateNQT(self, value):
        self._sellRateNQT = value

    @property
    def totalBuyLimit(self):
        return self._totalBuyLimit

    @totalBuyLimit.setter
    def totalBuyLimit(self, value):
        self._totalBuyLimit = value

    @property
    def totalSellLimit(self):
        return self._totalSellLimit

    @totalSellLimit.setter
    def totalSellLimit(self, value):
        self._totalSellLimit = value

    @property
    def initialBuySupply(self):
        return self._initialBuySupply

    @initialBuySupply.setter
    def initialBuySupply(self, value):
        self._initialBuySupply = value

    @property
    def initialSellSupply(self):
        return self._initialSellSupply

    @initialSellSupply.setter
    def initialSellSupply(self, value):
        self._initialSellSupply = value

    @property
    def expirationHeight(self):
        return self._expirationHeight

    @expirationHeight.setter
    def expirationHeight(self, value):
        self._expirationHeight = value

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
        super(PublishExchangeOffer, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(PublishExchangeOffer, self).getData(key)  # calls 'BasePost.getData()'
