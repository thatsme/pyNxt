# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class DeleteCurrency(Parent):
    def __init__(self, currency=None):
        """
            Delete a deletable currency (refer to Can Delete Currency). POST only.

            DeleteCurrency take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Delete_Currency

            REQUEST
            :param currency : is the currency ID (S)

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

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency

        super(DeleteCurrency, self).__init__(rt="deleteCurrency", data=self.data)

    def run(self):
        super(DeleteCurrency, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(DeleteCurrency, self).getData(key)  # calls 'BasePost.getData()'
