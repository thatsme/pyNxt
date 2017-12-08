# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class CurrencyBuy(Parent):
    def __init__(self, currency=None, rateNQT=0, unit=0):
        """
            Make an exchange request to buy or sell an exchangeable currency. POST only.

            CurrencyBuy take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Currency_Buy

            REQUEST
            :param currency : is the currency ID (S)
            :param rateNQT : is the exchange rate (in NQT per QNT) (N)
            :param units : is the amount of the currency to buy or sell (in QNT) (N)
            :param publicKey *: publicKey of sender accounts ( does not get in broadcast )
            :param secretPhrase **: secret Phrase of sender accounts
            :param feeNQT : fee for sending transaction (R) if 0 minimum is set ( 100000000 NQT )
            :param deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            :param referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            :param broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            :param phasing : phasing object ( check base/Phasing.py ) (O) (WP)
            :param message : message object ( check base/message.py ) (O) (WP)

            Note: An exchange request is immediately executed once accepted onto the blockchain based only on currently
            available offers (refer to Publish Exchange Offer). The request then expires, regardless of the amount of
            currency exchanged; the request may be completely filled, partially filled, or expire without any exchange
            if no matching offers are found.

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
                (O) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        # Required parameters
        self.currency = currency
        self.rateNQT = rateNQT
        self.unit = unit

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["rateNQT"] = self.rateNQT
        self.data["unit"] = self.unit

        super(CurrencyBuy, self).__init__(rt="currencyBuy", data=self.data)

    def run(self):
        super(CurrencyBuy, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(CurrencyBuy, self).getData(key)  # calls 'BasePost.getData()'
