
from base.BaseGet import BaseGet as Parent

class GetAccountLedgerEntry(Parent):

    def __init__(self, ledgerId=None, includeTransaction=False, includeHoldingInfo=False):

        self.ledgerId = ledgerId
        self.includeTransaction = includeTransaction
        self.includeHoldingInfo = includeHoldingInfo

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["ledgerId"] = self.ledgerId
        if self.includeTransaction:
            self.data["includeTransaction"] = self.includeTransaction
        if self.includeHoldingInfo:
            self.data["includeHoldingInfo"] = self.includeHoldingInfo

        super(GetAccountLedgerEntry, self).__init__(rt="getAccountLedgerEntry", data=self.data)

    def run(self):
        super(GetAccountLedgerEntry, self).run()                        # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountLedgerEntry, self).getData(key)               # calls 'BaseGet.getData()'ß