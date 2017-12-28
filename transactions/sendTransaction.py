# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class SendTransaction(Parent):
    def __init__(self, transactionBytes = None, transactionJSON = None, prunableAttachementsJSON = None, adminPassword = None ):
        """
            It broadcasts a transaction to the network without validating it,
            without re-broadcasting it and without adding it locally as unconfirmed transaction.
            Specially intended for roaming or light clients to send transactions to remote peers.

            SendTransaction take a default 4 parameter as explained in NXT API Documentation

            API is working with POST method only

            https://nxtwiki.org/wiki/The_Nxt_API#Send_Transaction

            REQUEST
            :param transactionBytes : is the bytecode of a signed transaction (O)
            :param transactionJSON : is the transaction object (optional if transactionBytes provided)
            :param prunableAttachmentJSON : is the attachment object embedded in transactionJSON containing a prunable message (required if transactionJSON not provided because transactionBytes never includes prunable data)
            :param adminPassword : is a string with the admin password (O)

            RESPONSE
            :return fullHash : (S) is the full hash of the signed transaction
            :return transaction : (S) is the transaction ID
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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
        self._transactionBytes = transactionBytes
        self._transactionJSON = transactionJSON
        self._prunableAttachmentJSON = prunableAttachementsJSON
        self._adminPassword = adminPassword

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["transactionBytes"] = self.transactionBytes
        self.data["transactionJSON"] = self.transactionJSON
        self.data["prunableAttachmentJSON"] = self.prunableAttachmentJSON
        self.data["adminPassword"] = self.adminPassword

        super(SendTransaction, self).__init__(rt="sendTransaction", data=self.data, phasing=self.phasing, message=self.message)

    @property
    def transactionBytes(self):
        return self._transactionBytes

    @transactionBytes.setter
    def transactionBytes(self, value):
        self._transactionBytes = value

    @property
    def transactionJSON(self):
        return self._transactionJSON

    @transactionJSON.setter
    def transactionJSON(self, value):
        self._transactionJSON = value

    @property
    def adminPassword(self):
        return self._adminPassword

    @adminPassword.setter
    def adminPassword(self, value):
        self._adminPassword = value

    @property
    def prunableAttachmentJSON(self):
        return self._prunableAttachmentJSON

    @prunableAttachmentJSON.setter
    def prunableAttachmentJSON(self, value):
        self._prunableAttachmentJSON = value

    def run(self):
        super(SendTransaction, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(SendTransaction, self).getData(key)  # calls 'BasePost.getData()'
