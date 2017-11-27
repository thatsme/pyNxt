# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAliasesLike(Parent):
    def __init__(self, aliasPrefix = None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            GetAliases take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Get_AliasesLike

            aliasPrefix : is the prefix (at least 2 characters long) of the aliasName
            firstIndex :
            lastIndex :
            requireBlock :
            requireLastBlock :

        """

        # Required parameters
        self.aliasPrefix = aliasPrefix

        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["aliasPrefix"] = self.aliasPrefix

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex

        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAliasesLike, self).__init__(rt="getAliasesLike", data=self.data)

    def run(self):
        super(GetAliasesLike, self).run()                                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(GetAliasesLike, self).getData(key)                           # calls 'BasePost.getData()'
