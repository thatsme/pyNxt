# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class ReadMessage(Parent):

    def __init__(self, transaction=None, secretPhrase=None, sharedKey=None, retrieve=False, rb=None ):
        """
            Get a message given a transaction ID.

            ReadMessage take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Read_Message

            REQUEST
            :param transaction : is the transaction ID of the message
            :param secretPhrase : is the secret passphrase of the account that received the message (S) (O)
            :param sharedKey : is the shared key used to decrypt the message (optional) (see Get Shared Key)
            :param retrieve : is true to retrieve pruned data from archival nodes (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return messageIsPrunable : (B) is true if there is a plain message and it is prunable, false if it is not prunable
            :return message : (S) is the plain message, if applicable
            :return encryptedMessageIsPrunable : (B) is true if there is an encrypted message and it is prunable, false if it is not prunable
            :return  decryptedMessage : (S) is the decrypted message, if applicable and only if the provided secretPhrase belongs to either
                                the sender or receiver of the transaction
            :return decryptedMessageToSelf : (S) is the decrypted message sent to self, if applicable and only if the provided secretPhrase
                                belongs to the sender of transaction
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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
        self.data["retrieve"] = self.retrieve

        super(ReadMessage, self).__init__(rt = "readMessage", data=self.data, rb=self.rb)

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
        super(ReadMessage, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(ReadMessage, self).getData(key)             # calls 'BaseGet.getData()'