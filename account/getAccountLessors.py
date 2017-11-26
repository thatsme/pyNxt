from base.BaseGet import BaseGet as Parent

class GetAccountLessors(Parent):

    def __init__(self, account=None, height=None, requireBlock=None, requireLastBlock=None):

        self.account = account
        self.height = height
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.height:
            self.data["height"] = self.height
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountLessors, self).__init__(rt = "getAccountLessors", data=self.data)

    def run(self):
        super(GetAccountLessors, self).run()                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountLessors, self).getData(key)           # calls 'BaseGet.getData()'