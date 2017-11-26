from base.BaseGet import BaseGet as Parent

class GetUnconfirmedTransactionIds(Parent):

    ## Multiaccount parameters (3)
    def __init__(self, account=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):

        self.accounts = [None]*3
        for a in account[:3]:
            self.accounts.append(a)

        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        for a in self.accounts:
            self.data["account"] = a

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetUnconfirmedTransactionIds, self).__init__(rt = "getUnconfirmedTransactionIds", data=self.data)

    def run(self):
        super(GetUnconfirmedTransactionIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetUnconfirmedTransactionIds, self).getData(key)    # calls 'BaseGet.getData()'