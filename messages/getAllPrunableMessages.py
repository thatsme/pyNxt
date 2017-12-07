# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAllPrunableMessages(Parent):

    def __init__(self, timestamp=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get all available prunable messages in reverse block timestamp order.

            GetAllPrunableMessages take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_All_Prunable_Messages

            REQUEST
            :param timestamp is the earliest message (in seconds since the genesis block) to retrieve (optional)
            :param firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            :param lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            :param requireBlock : is theblock ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return prunableMessages : is an array (A) of prunable messages (refer to Get Prunable Message)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
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

        self.timestamp = timestamp
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["timestamp"] = self.timestamp

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock


        super(GetAllPrunableMessages, self).__init__(rt = "getAllPrunableMessages", data=self.data)

    def run(self):
        super(GetAllPrunableMessages, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAllPrunableMessages, self).getData(key)             # calls 'BaseGet.getData()'