from base.BaseGet import BaseGet as Parent

class GetAccountPhasedTransactionCount(Parent):

    def __init__(self, account=None, requireBlock=None, requireLastBlock=None):

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

        super(GetAccountPhasedTransactionCount, self).__init__(rt = "getAccountPhasedTransactionCount", data=self.data)

    def run(self):
        super(GetAccountPhasedTransactionCount, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountPhasedTransactionCount, self).getData(key)       # calls 'BaseGet.getData()'