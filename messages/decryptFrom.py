# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class DecryptFrom(Parent):

    def __init__(self, secretPhrase=None, account=None, data=None, nonce=None, decryptedMessageIsText=False, uncompressDecryptedMessage=False ):
        """
            Decrypt an AES-encrypted message.

            DecryptFrom take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Decrypt_From

            REQUEST
            :param secretPhrase : is the secret passphrase of the recipient (S)
            :param accounts : is the accounts ID of the recipient (S)
            :param data : is AES-encrypted data
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

        self.account = account
        self.secretPhrase = secretPhrase
        self.data = data
        self.nonce = nonce
        self.decryptedMessageIsText = decryptedMessageIsText
        self.uncompressDectyptedMessage = uncompressDecryptedMessage

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["secretPhrase"] = self.secretPhrase
        self.data["data"] = self.data
        self.data["nonce"] = self.nonce
        self.data["decryptedMessageIsText"] = self.decryptedMessageIsText
        self.data["uncompressDecryptedMessage"] = self.uncompressDectyptedMessage

        super(DecryptFrom, self).__init__(rt = "decryptFrom", data=self.data)

    def run(self):
        super(DecryptFrom, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(DecryptFrom, self).getData(key)             # calls 'BaseGet.getData()'