# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class EncryptTo(Parent):

    def __init__(self, secretPhrase=None, recipient=None, messageToEncrypt=None, messageToEncryptIsText=True, compressMessageToEncrypt=False ):
        """
            Encrypt a message using AES without sending it.

            EncryptTo take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Encrypt_To

            REQUEST
            :param secretPhrase : is the secret passphrase of the sender (S)
            :param recipient : is the accounts ID of the recipient (S)
            :param messageToEncrypt is either UTF-8 text or a string of hex digits to be compressed and converted
                            into a 1000 byte maximum bytecode then encrypted using AES
            :param messageToEncryptIsText : is false if the message to encrypt is a hex string, otherwise the message to encrypt is text (B) (O)
            :param compressMessageToEncrypt : is false to prevent gzip compression before encryption (B) (O)


            RESPONSE
            :return data : (S) is the AES-encrypted data
            :return nonce : (S) is a 32-byte pseudorandom nonce
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
                (O) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self.recipient = recipient
        self.secretPhrase = secretPhrase
        self.messageToEncrypt = messageToEncrypt
        self.messageToEncryptIsText = messageToEncryptIsText
        self.compressMessageToEncrypt = compressMessageToEncrypt

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["recipient"] = self.recipient
        self.data["secretPhrase"] = self.secretPhrase

        self.data["messageToEncrypt"] = self.messageToEncrypt
        self.data["messageToEncryptIsText"] = self.messageToEncryptIsText
        self.data["compressMessageToEncrypt"] = self.compressMessageToEncrypt


        super(EncryptTo, self).__init__(rt = "encryptTo", data=self.data)

    def run(self):
        super(EncryptTo, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(EncryptTo, self).getData(key)             # calls 'BaseGet.getData()'