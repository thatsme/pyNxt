# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAliases(Parent):
    def __init__(self, account = None, timestamp=0, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            GetAliases take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Aliases

            account : is the account
            timestamp :
            firstIndex :
            lastIndex :
            requireBlock :
            requireLastBlock :

        """

        # Required parameters
        self.account = account
        self.timestamp = timestamp
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["account"] = self.account
        self.data["timestamp"] = self.timestamp

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex

        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAliases, self).__init__(rt="getAliases", data=self.data)

    def run(self):
        super(GetAliases, self).run()                                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(GetAliases, self).getData(key)                           # calls 'BasePost.getData()'
