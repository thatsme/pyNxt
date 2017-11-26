from base.BaseGet import BaseGet as Parent

class GetAccountCurrentBidOrderIds(Parent):

    def __init__(self, account=None, assets=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):

        self.account = account
        self.assets = assets
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        self.data["assets"] = self.assets
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountCurrentBidOrderIds, self).__init__(rt = "getAccountCurrentBidOrderIds", data=self.data)

    def run(self):
        super(GetAccountCurrentBidOrderIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrentBidOrderIds, self).getData(key)    # calls 'BaseGet.getData()'