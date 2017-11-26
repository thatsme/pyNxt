from base.BaseGet import BaseGet as Parent

class GetGuaranteedBalance(Parent):

    def __init__(self, account=None, numberOfConfirmations=0, requireBlock=None, requireLastBlock=None ):


        self.account = account
        self.numberOfConfirmations = numberOfConfirmations
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = account

        if self.numberOfConfirmations:
            self.data["numberOfConfirmations"] = self.numberOfConfirmations
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetGuaranteedBalance, self).__init__(rt = "getGuaranteedBalance", data=self.data)

    def run(self):
        super(GetGuaranteedBalance, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetGuaranteedBalance, self).getData(key)    # calls 'BaseGet.getData()'