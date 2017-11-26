from base.BaseGet import BaseGet as Parent

class GetAccountProperties(Parent):


    def __init__(self, recipient=None, setter=None, property=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):

        self.recipient = recipient
        self.setter = setter
        self.property = property
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["recipient"] = self.recipient
        if self.setter:
            self.data["setter"] = self.setter
        if self.property:
            self.data["property"] = self.property
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountProperties, self).__init__(rt = "getAccountProperties", data=self.data)

    def run(self):
        super(GetAccountProperties, self).run()                               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountProperties, self).getData(key)                 # calls 'BaseGet.getData()'


