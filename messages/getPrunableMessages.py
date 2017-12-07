# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPrunableMessages(Parent):

    def __init__(self, account=None,otherAccount=None,  secretPhrase=None, timestamp=0, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get all still-available prunable messages given an accounts id,
            optionally limiting to only those with another accounts as recipient or sender, in reverse chronological order.

            GetPrunableMessages take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Prunable_Messages

            REQUEST
            :param accounts : is the accounts ID (S)
            :param otherAccount : is another accounts ID, either sender or recipient, to limit the response (S)
            :param secretPhrase : is the secret passphrase used to decrypt the encrypted part of the message (O)
            :param timestamp : is the earliest prunable message (in seconds since the genesis block) to retrieve (optional)
            :param firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            :param lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            :param requireBlock : is theblock ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return prunableMessages : is an array (A) of prunable message objects (refer to Get Prunable Message for details)
            :return lastBlock : is the last block ID on the blockchain (S)(applies if requireBlock is provided but not requireLastBlock)
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

        self.account = account
        self.otherAccount = otherAccount
        self.secretPhrase = secretPhrase
        self.timestamp = timestamp
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.otherAccount:
            self.data["otherAccount"] = self.otherAccount

        self.data["secretPhrase"] = self.secretPhrase
        self.data["timestamp"] = self.timestamp

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock


        super(GetPrunableMessages, self).__init__(rt = "getPrunableMessages", data=self.data)

    def run(self):
        super(GetPrunableMessages, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetPrunableMessages, self).getData(key)             # calls 'BaseGet.getData()'