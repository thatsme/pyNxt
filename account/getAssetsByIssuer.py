from base.BaseGet import BaseGet as Parent

class GetAssetsByIssuer(Parent):

    ## Multiaccount parameters (3)
    def __init__(self,account=None, firstIndex=None, lastIndex=None, includeCounts=False, requireBlock=None, requireLastBlock=None ):

        self.accounts = [None]*3
        for a in account[:3]:
            self.accounts.append(a)

        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.includeCounts = includeCounts
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        for a in self.accounts:
            self.data["account"] = a

        if firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.includeCounts:
            self.data["includeCounts"] = self.includeCounts
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAssetsByIssuer, self).__init__(rt = "getAssetsByIssuer", data=self.data)

    def run(self):
        super(GetAssetsByIssuer, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetsByIssuer, self).getData(key)    # calls 'BaseGet.getData()'