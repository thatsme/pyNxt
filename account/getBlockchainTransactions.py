from base.BaseGet import BaseGet as Parent

class GetBlockchainTransactions(Parent):

    def __init__(self,account=None, timestamp=0, type=None, subtype=None, firstIndex=None, lastIndex=None, numberOfConfirmations=0, withMessage=False, phasedOnly=False, nonPhasedOnly=False, includeExpiredPrunable=False, includePhasingResult=False, executeOnly=False, requireBlock=None, requireLastBlock=None ):

        self.account = account
        self.timestamp = timestamp
        self.type = type
        self.subtype = subtype
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.numberOfConfirmations = numberOfConfirmations
        self.withMessage = withMessage
        self.phasedOnly = phasedOnly
        self.nonPhasedOnly = nonPhasedOnly
        self.includeExpiredPrunable = includeExpiredPrunable
        self.includePhasingResult = includePhasingResult
        self.executeOnly = executeOnly
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        self.data["timestamp"] = self.timestamp
        self.data["numberOfConfirmations"] = self.numberOfConfirmations
        if self.type:
            self.data["type"] = self.type
        if self.subtype:
            self.data["subtype"] = self.subtype

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.withMessage:
            self.data["withMessage"] = self.withMessage
        if self.phasedOnly:
            self.data["phasedOnly"] = self.phasedOnly
        if self.nonPhasedOnly:
            self.data["nonPhasedOnly"] = self.nonPhasedOnly
        if self.includeExpiredPrunable:
            self.data["includeExpiredPrunable"] = self.includeExpiredPrunable
        if self.includePhasingResult:
            self.data["includePhasingResult"] = self.includePhasingResult
        if self.executeOnly:
            self.data["executeOnly"] = self.executeOnly
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetBlockchainTransactions, self).__init__(rt = "getBlockchainTransactions", data=self.data)

    def run(self):
        super(GetBlockchainTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBlockchainTransactions, self).getData(key)    # calls 'BaseGet.getData()'