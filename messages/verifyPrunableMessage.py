# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class VerifyPrunableMessage(Parent):

    def __init__(self, message=None, messageIsText=False, encryptedMessageData=None, encryptedMessageNonce=None, messageToEncryptIsText=False, compressMessageToEncrypt=False, rb=None  ):
        """
            Verify that a prunable message obtained from any source, when hashed, matches the hash of the original prunable message.

            VerifyPrunableMessage take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Verify_Prunable_Message

            REQUEST
            :param message : is the plain message, if applicable (O)
            :param messageIsText : (B) is false if the provided plain message is a hex string (O)
            :param encryptedMessageData : is the data part of the encrypted data-nonce pair (optional if message provided)
            :param encryptedMessageNonce : is the nonce part of the encrypted data-nonce pair (required if encryptedMessageData provided)
            :param messageToEncryptIsText : (B) is false if the encrypted message was a hex string before encryption (O)
            :param compressMessageToEncrypt : (B) is false if the encrypted message was not compressed before encryption (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            Note: The hash is computed from the message itself plus its associated flag(s) isText and isCompressed
            (encrypted only); therefore the flag(s) must be provided for verification if different from the default(s).
            The original encryptedMessageData-encryptedMessageNonce pair used to compute the original hash must be provided
            again to recompute the hash for verification of a prunable encrypted message.

            RESPONSE
            :return version.PrunablePlainMessage or version.PrunableEncryptedMessage (N) is 1, the version number
            :return verify : (B) is true if the original hash matches the hash computed from the provided values
            :return message (S) or encryptedMessage (O) is the prunable plain message or the prunable encrypted message object
                            containing the fields:
            :return > data (S)
            :return > nonce (B)
            :return > isText (B)
            :return > isCompressed (B)
            :return messageIsText : (B) is true if the plain message is text, false if it is a hex string, if applicable
            :return  messageHash or encryptedMessageHash (S) is the hash
            :return lastBlock (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime (N) is the API request processing time (in millsec)

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

        self.message = message
        self.messageIsText = messageIsText
        self.encryptedMessageData = encryptedMessageData
        self.encryptedMessageNonce = encryptedMessageNonce
        self.messageToEncryptIsText = messageToEncryptIsText
        self.compressMessageToEncrypt = compressMessageToEncrypt
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["message"] = self.message
        self.data["messageIsText"] = self.messageIsText
        if self.encryptedMessageData:
            self.data["encryptedMessageData"] = self.encryptedMessageData

        if self.encryptedMessageData and not self.encryptedMessageNonce:
            return "Error"
        else:
            self.data["encryptedMessageNonce"] = self.encryptedMessageNonce

        self.data["messageToEncryptIsText"] = self.messageToEncryptIsText
        self.data["messageToEncryptIsText"] = self.messageToEncryptIsText


        self.data["nonce"] = self.nonce
        self.data["decryptedMessageIsText"] = self.decryptedMessageIsText
        self.data["compressMessageToEncrypt"] = self.compressMessageToEncrypt

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(VerifyPrunableMessage, self).__init__(rt = "verifyPrunableMessage", data=self.data, rb=self.rb)

    def run(self):
        super(VerifyPrunableMessage, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(VerifyPrunableMessage, self).getData(key)             # calls 'BaseGet.getData()'