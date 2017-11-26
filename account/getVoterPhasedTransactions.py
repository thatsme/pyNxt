from base.BaseGet import BaseGet as Parent

class GetVoterPhasedTransactions(Parent):

    def __init__(self, account=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):

        self.account = account
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = account

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetVoterPhasedTransactions, self).__init__(rt = "getVoterPhasedTransactions", data=self.data)

    def run(self):
        super(GetVoterPhasedTransactions, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetVoterPhasedTransactions, self).getData(key)       # calls 'BaseGet.getData()'