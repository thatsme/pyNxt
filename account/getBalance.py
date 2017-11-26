from base.BaseGet import BaseGet as Parent

class GetBalance(Parent):

    def __init__(self, account=None, includeEffectiveBalance=False, height= None, requireBlock=None, requireLastBlock=None ):

        self.account = account
        self.includeEffectiveBalance = includeEffectiveBalance
        self.height = height
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.includeEffectiveBalance:
            self.data["includeEffectiveBalance"] = self.includeEffectiveBalance
        if self.height:
            self.data["height"] = self.height
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetBalance, self).__init__(rt = "getBalance", data=self.data)

    def run(self):
        super(GetBalance, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBalance, self).getData(key)    # calls 'BaseGet.getData()'