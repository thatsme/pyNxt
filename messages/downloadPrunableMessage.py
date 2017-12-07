# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class DownloadPrunableMessage(Parent):

    def __init__(self, transaction=None, secretPhrase=None, sharedKey=None, retrieve=False, requireBlock=None, requireLastBlock=None ):
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
            :param requireBlock : is theblock ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

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
                (O) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self.transaction = transaction
        self.secretPhrase = secretPhrase
        self.sharedKey = sharedKey
        self.retrieve = retrieve
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["transaction"] = self.transaction
        self.data["secretPhrase"] = self.secretPhrase
        self.data["sharedKey"] = self.sharedKey
        if self.retrieve:
            self.data["retrieve"] = self.retrieve
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock


        super(DownloadPrunableMessage, self).__init__(rt = "downloadPrunableMessage", data=self.data)

    def run(self):
        super(DownloadPrunableMessage, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(DownloadPrunableMessage, self).getData(key)             # calls 'BaseGet.getData()'