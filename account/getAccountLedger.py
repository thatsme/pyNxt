from base.BaseGet import BaseGet as Parent

class GetAccountLedger(Parent):

    def __init__(self, account=None, event=None, eventType=None, holdingType=None, holding=None, includeTransactions=False, includeHoldingInfo=False, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):

        self.account = account
        self.event = event
        self.eventType = eventType
        self.holding = holding
        self.holdingType = holdingType

        self.includeTransactions = includeTransactions
        self.includeHoldingInfo = includeHoldingInfo

        self.firstIndex = firstIndex

        self.lastIndex = lastIndex

        self.requireBlock = requireBlock

        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["account"] = self.account
        if self.event:
            self.data["event"] = self.event
        if self.eventType:
            self.data["eventType"] = self.eventType
        if self.holding:
            self.data["holding"] = self.holding
        if self.holdingType:
            self.data["holdingType"] = self.holdingType
        if self.includeTransactions:
            self.data["includeTransactions"] = self.includeTransactions
        if self.includeHoldingInfo:
            self.data["includeHoldingInfo"] = self.includeHoldingInfo
        if firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountLedger, self).__init__(rt = "getAccountLedger", data=self.data)

    def run(self):
        super(GetAccountLedger, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountLedger, self).getData(key)    # calls 'BaseGet.getData()'ß