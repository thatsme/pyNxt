# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class DownloadPrunableMessage(Parent):

    def __init__(self, transaction=None, secretPhrase=None, sharedKey=None, retrieve=False, rb=None ):
        """
            Downloading a prunable message attachments directly as binary data. An optional secretPhrase parameter is supported,
            to allow decryption and downloading of the encrypted part of the message instead of the plain text part.

            DownloadPrunableMessage take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Download_Prunable_Message

            REQUEST
            :param transaction : is the transaction ID (S)
            :param secretPhrase : is the secret passphrase used to decrypt the encrypted part of the message (O)
            :param sharedKey : is the shared key used to decrypt the message (O) (see Get Shared Key)
            :param retrieve : is true to retrieve the message from achival node if needed (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return decryptedMessage : (S) is the decrypted message
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

        self._transaction = transaction
        self._secretPhrase = secretPhrase
        self._sharedKey = sharedKey
        self._retrieve = retrieve
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["transaction"] = self.transaction
        self.data["secretPhrase"] = self.secretPhrase
        self.data["sharedKey"] = self.sharedKey
        if self.retrieve:
            self.data["retrieve"] = self.retrieve

        super(DownloadPrunableMessage, self).__init__(rt = "downloadPrunableMessage", data=self.data, rb=self.rb)

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, value):
        self._transaction = value

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def sharedKey(self):
        return self._sharedKey

    @sharedKey.setter
    def sharedKey(self, value):
        self._sharedKey = value

    @property
    def retrieve(self):
        return self._retrieve

    @retrieve.setter
    def retrieve(self, value):
        self._retrieve = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value


    def run(self):
        super(DownloadPrunableMessage, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(DownloadPrunableMessage, self).getData(key)             # calls 'BaseGet.getData()'