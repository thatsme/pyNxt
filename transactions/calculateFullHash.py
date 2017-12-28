# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class CalculateFullHash(Parent):


    def __init__(self, unsignedTransactionJSON=None, unsignedTransactionBytes=None, signatureHash=None):
        """
            Calculate the full hash of a transaction.

            CalculateFullHash take a default 1 parameter as explained in NXT API Documentation ( is deadLine requested or not ? )

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Calculate_Full_Hash

            REQUEST
            :param unsignedTransactionJSON : is the unsigned transaction JSON object (O)
            :param unsignedTransactionBytes : are the unsigned bytes of a transaction (optional if unsignedTransactionJSON is provided)
            :param signatureHash : is a SHA-256 hash of the transaction signature (S)

            RESPONSE
            :return requestProcessingTime : (N) is the API request processing time (in millisec)
            :return fullHash : (S) is the full hash of the signed transaction

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




        # is the block ID of a block that must be present in the blockchain during execution (optional)

        self._unsignedTransactionJSON = unsignedTransactionJSON
        self._unsignedTransactionBytes = unsignedTransactionBytes
        self._signatureHash = signatureHash

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["signatureHash"] = self.signatureHash

        if self.unsignedTransactionJSON:
            self.data["unsignedTransactionJSON"] = self.unsignedTransactionJSON
        if self.unsignedTransactionBytes:
            self.data["unsignedTransactionBytes"] = self.unsignedTransactionBytes

        super(CalculateFullHash, self).__init__(rt = "calculateFullHash", data=self.data)

    @property
    def unsignedTransactionJSON(self):
        return self._unsignedTransactionJSON

    @unsignedTransactionJSON.setter
    def unsignedTransactionJSON(self, value):
        self._unsignedTransactionJSON = value

    @property
    def unsignedTransactionBytes(self):
        return self._unsignedTransactionBytes

    @unsignedTransactionBytes.setter
    def unsignedTransactionBytes(self, value):
        self._unsignedTransactionBytes = value

    @property
    def signatureHash(self):
        return self._signatureHash

    @signatureHash.setter
    def signatureHash(self, value):
        self._signatureHash = value

    def run(self):
        """
        Run rest request
        """
        super(CalculateFullHash, self).run()                               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(CalculateFullHash, self).getData(key)                 # calls 'BaseGet.getData()'

    def phelp(self):
        print(CalculateFullHash.__doc__)

