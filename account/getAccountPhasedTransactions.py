from base.BaseGet import BaseGet as Parent

class GetAccountPhasedTransactions(Parent):

    def __init__(self, account=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):

        self.account = account
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountPhasedTransactions, self).__init__(rt = "getAccountPhasedTransactions", data=self.data)

    def run(self):
        super(GetAccountPhasedTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountPhasedTransactions, self).getData(key)    # calls 'BaseGet.getData()'