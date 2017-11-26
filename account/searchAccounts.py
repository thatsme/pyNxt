from base.BaseGet import BaseGet as Parent

class SearchAccounts(Parent):

    def __init__(self, query=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):

        self.query = query
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["query"] = query

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(SearchAccounts, self).__init__(rt = "searchAccounts", data=self.data)

    def run(self):
        super(SearchAccounts, self).run()                   # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(SearchAccounts, self).getData(key)     # calls 'BaseGet.getData()'