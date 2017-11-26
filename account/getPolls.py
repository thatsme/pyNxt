from base.BaseGet import BaseGet as Parent

class GetPolls(Parent):

    def __init__(self, account=None, timestamp=0, firstIndex=None, lastIndex=None, includeFinished=False, finishedOnly=False, requireBlock=None, requireLastBlock=None ):

        self.account = account
        self.timestamp = timestamp
        self.includeFinished = includeFinished
        self.finishedOnly = finishedOnly
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = account
        self.data["timestamp"] = timestamp

        self.data["includeFinished"] = self.includeFinished
        self.data["finishedOnly"] = self.finishedOnly

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetPolls, self).__init__(rt = "getPolls", data=self.data)

    def run(self):
        super(GetPolls, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetPolls, self).getData(key)    # calls 'BaseGet.getData()'