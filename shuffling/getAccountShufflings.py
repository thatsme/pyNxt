# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountShufflings(Parent):

    def __init__(self, account=None, includeFinished=False, includeHoldingInfo=False, firstIndex=None, lastIndex=None, adminPassword=None, requireBlock=None, requireLastBlock=None):
        """
            Retrieves info about shufflings for a specific account.

            GetAccountShufflings take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Shufflings

            REQUEST
            :param account : is the account ID (S)
            :param includeFinished : is true to include completed shufflings (B) (O)
            :param includeHoldingInfo is true to include holding info (B) (O)
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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self.account = account
        self.includeFinished = includeFinished
        self.includeHoldingInfo = includeHoldingInfo
        self.adminPassword = adminPassword
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["includeFinished"] = self.includeFinished
        self.data["includeHoldingInfo"] = self.includeHoldingInfo

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


        super(GetAccountShufflings, self).__init__(rt = "getAccountShufflings", data=self.data)

    def run(self):
        super(GetAccountShufflings, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountShufflings, self).getData(key)               # calls 'BaseGet.getData()'