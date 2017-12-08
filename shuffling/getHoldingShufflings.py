# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetHoldingShufflings(Parent):

    def __init__(self, holding=False, stage=None, includeFinished=False, firstIndex=None, lastIndex=None, adminPassword=None, requireBlock=None, requireLastBlock=None):
        """
            Retrieves info about shufflings for a specific holding and/or stage.

            GetHoldingShufflings take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Holding_Shufflings

            REQUEST
            :param holding : is the holding ID (S) (O)
            :param stage : is the stage of the shuffling (See Get Constants for type definitions) (O)
            :param includeFinished : is true to include completed shufflings (B) (O)
            :param firstIndex is a zero-based index to the first tagged data to retrieve (O)
            :param lastIndex is a zero-based index to the last tagged data to retrieve (O)
            :param adminPassword is a string with the admin password (O)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return shufflings : (A) is an array containing the shuffling object (refer to Get Shuffling)
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
                (O) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self.holding = holding
        self.stage = stage
        self.includeFinished = includeFinished
        self.adminPassword = adminPassword
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["holding"] = self.holding
        self.data["stage"] = self.stage
        self.data["includeFinished"] = self.includeFinished

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.adminPassword:
            self.data["adminPassword"] = self.adminPassword

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock


        super(GetHoldingShufflings, self).__init__(rt = "getHoldingShufflings", data=self.data)

    def run(self):
        super(GetHoldingShufflings, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetHoldingShufflings, self).getData(key)               # calls 'BaseGet.getData()