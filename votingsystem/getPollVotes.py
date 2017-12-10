# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPollVotes(Parent):

    def __init__(self, poll=None, account=None, includeWeights=False, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):
        """
            Get all votes on a poll in reverse chronological order.

            GetPollVotes take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Poll_Votes

            REQUEST
            :param poll : is the poll ID
            :param includeWeights : is true to calculate and return the weight assigned to each vote (B) (O)
            :param firstIndex is a zero-based index to the first vote to retrieve (O)
            :param lastIndex is a zero-based index to the last vote to retrieve (O)
            :param requireBlock is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return votes : (A) is an array of vote objects (refer to Get Poll Vote for details)
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

            Note: Votes are deleted from the database 1441 blocks after the poll is finished.
            Only aggregate results are kept (refer to Get Poll Result).

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

        self.poll = poll
        self.account = account
        self.includeWeights = includeWeights
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["poll"] = self.poll
        self.data["account"] = self.account
        self.data["includeWeights"] = self.includeWeights


        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetPollVotes, self).__init__(rt = "getPollVotes", data=self.data)

    def run(self):
        super(GetPollVotes, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPollVotes, self).getData(key)               # calls 'BaseGet.getData()

