# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAliasCount(Parent):
    def __init__(self, account = None, requireBlock=None, requireLastBlock=None ):
        """
            GetAliasCount take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Alias_Count

            account : is the account
            requireBlock :
            requireLastBlock :

        """

        # Required parameters
        self.account = account
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["account"] = self.account

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAliasCount, self).__init__(rt="getAliasCount", data=self.data)

    def run(self):
        super(GetAliasCount, self).run()                                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(GetAliasCount, self).getData(key)                           # calls 'BasePost.getData()'
