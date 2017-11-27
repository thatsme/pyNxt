# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAlias(Parent):
    def __init__(self, alias = None, aliasName=None, requireBlock=None, requireLastBlock=None ):
        """
            GetAlias take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with  post method, and create a transaction, for more info about transactions please refer to

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Alias

            alias : is the id of alias
            aliasName : is the name of alias
            requireBlock :
            requireLastBlock :

        """

        # Required parameters
        self.alias = alias
        self.aliasName = aliasName
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["alias"] = self.alias
        self.data["aliasName"] = self.aliasName

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAlias, self).__init__(rt="getAlias", data=self.data)

    def run(self):
        super(GetAlias, self).run()                                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(GetAlias, self).getData(key)                           # calls 'BasePost.getData()'
