from base.BaseGet import BaseGet as Parent

class GetAccountCurrencyCount(Parent):

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

        super(GetAccountCurrencyCount, self).__init__(rt = "getAccountCurrencyCount", data=self.data)

    def run(self):
        super(GetAccountCurrencyCount, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrencyCount, self).getData(key)    # calls 'BaseGet.getData()'