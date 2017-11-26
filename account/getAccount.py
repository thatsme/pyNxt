from base.BaseGet import BaseGet as Parent

class GetAccount(Parent):


    def __init__(self, account=None, includeLessors=False, includeAssets=False, includeCurrencies=False, includeEffectiveBalance=False, requireBlock=None, requireLastBlock=None):

        self.account = account
        self.includeLessors = includeLessors
        self.includeAssets = includeAssets
        self.includeCurrencies = includeCurrencies
        self.includeEffectiveBalance = includeEffectiveBalance
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.includeLessors:
            self.data["includeLessors"] = self.includeLessors
        if self.includeAssets:
            self.data["includeAssets"] = self.includeAssets
        if self.includeCurrencies:
            self.data["includeCurrencies"] = self.includeCurrencies
        if self.includeEffectiveBalance:
            self.data["includeEffectiveBalace"] = self.includeEffectiveBalance
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccount, self).__init__(rt = "getAccount", data=self.data)

    def run(self):
        super(GetAccount, self).run()                               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccount, self).getData(key)                 # calls 'BaseGet.getData()'


