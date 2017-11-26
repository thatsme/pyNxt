from base.BaseGet import BaseGet as Parent

class GetAccountBlockIds(Parent):

    def __init__(self, account=None, timestamp=0, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):

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

        super(GetAccountBlockIds, self).__init__(rt = "getAccountBlockIds", data=self.data)

    def run(self):
        super(GetAccountBlockIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountBlockIds, self).getData(key)    # calls 'BaseGet.getData()'