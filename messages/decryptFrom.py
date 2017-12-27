# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class DecryptFrom(Parent):

    def __init__(self, secretPhrase=None, account=None, idata=None, nonce=None, decryptedMessageIsText=False, uncompressDecryptedMessage=False ):
        """
            Decrypt an AES-encrypted message.

            DecryptFrom take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Decrypt_From

            REQUEST
            :param secretPhrase : is the secret passphrase of the recipient (S)
            :param accounts : is the accounts ID of the recipient (S)
            :param idata : is AES-encrypted data
            :param nonce : is the unique nonce associated with the encrypted data
            :param decryptedMessageIsText is false if the decrypted message is a hex string, otherwise the decrypted message is text (S) (O)
            :param uncompressDecryptedMessage : is false to prevent gzip uncompression after decryption (B) (O)

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

        self._account = account
        self._secretPhrase = secretPhrase
        self._idata = idata
        self._nonce = nonce
        self._decryptedMessageIsText = decryptedMessageIsText
        self._uncompressDectyptedMessage = uncompressDecryptedMessage

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["secretPhrase"] = self.secretPhrase
        self.data["data"] = self.idata
        self.data["nonce"] = self.nonce
        self.data["decryptedMessageIsText"] = self.decryptedMessageIsText
        self.data["uncompressDecryptedMessage"] = self.uncompressDectyptedMessage

        super(DecryptFrom, self).__init__(rt = "decryptFrom", data=self.data)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def idata(self):
        return self._idata

    @idata.setter
    def idata(self, value):
        self._idata = value

    @property
    def nonce(self):
        return self._nonce

    @nonce.setter
    def nonce(self, value):
        self._nonce = value

    @property
    def decryptedMessageIsText(self):
        return self._decryptedMessageIsText

    @decryptedMessageIsText.setter
    def decryptedMessageIsText(self, value):
        self._decryptedMessageIsText = value

    @property
    def uncompressDectyptedMessage(self):
        return self._uncompressDectyptedMessage

    @uncompressDectyptedMessage.setter
    def uncompressDectyptedMessage(self, value):
        self._uncompressDectyptedMessage = value

    def run(self):
        super(DecryptFrom, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(DecryptFrom, self).getData(key)             # calls 'BaseGet.getData()'