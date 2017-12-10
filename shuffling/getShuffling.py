# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetShuffling(Parent):

    def __init__(self, shuffling=None, includeHoldingInfo=False, requireBlock=None, requireLastBlock=None ):
        """
            Retrieves info about a shuffling.

            GetShuffling take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Shuffling

            REQUEST
            :param shuffling : is the shuffling ID
            :param includeHoldingInfo : is true to include holding info (B) (O)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return blocksRemaining : (N) number of blocks remaining until current stage is finished.
            :return amount : (S) the amount of holdingType to be shuffled
            :return shufflingStateHash : (S) state hash of the shuffling
            :return shufflingFullHash : (S) the full hash of the shuffling
            :return issuer : (S) is the issuer account ID
            :return issuerRS : (S) is the Reed-Solomon address of the issuer account
            :return assignee : (S) is the current assignee account ID
            :return assigneeRS : (S) is the Reed-Solomon address of the current assignee account
            :return shuffling : (S) is the shuffling ID
            :return holding : (S) is the asset or currency ID
            :return holdingType : (N) is the holding type (See Get Constants for type definitions)
            :return stage : (N) is the current stage of the shuffling (See Get Constants for type definitions)
            :return participantCount : (N) is the number of participants required to start the shuffling
            :return registrantCount : (N) is the number of registrered participants
            :return recipientPublicKeys : (A) is an array of recipient public keys
            :return holdingInfo : (A) is an array containing the asset or currency info (if includeHoldingInfo is true and holdingType is not NXT)
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

        self.shuffling = shuffling
        self.includeHoldingInfo = includeHoldingInfo
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["shuffling"] = self.shuffling
        self.data["includeHoldingInfo"] = self.includeHoldingInfo

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetShuffling, self).__init__(rt = "getShuffling", data=self.data)

    def run(self):
        super(GetShuffling, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetShuffling, self).getData(key)               # calls 'BaseGet.getData()