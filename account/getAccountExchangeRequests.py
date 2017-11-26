from base.BaseGet import BaseGet as Parent

class GetAccountExchangeRequests(Parent):

    def __init__(self, account=None, currency=None, includeCurrencyInfo=False, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):

        self.account = account
        self.currency = currency
        self.includeCurrencyInfo = includeCurrencyInfo
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.currency:
            self.data["currency"] = self.currency
        if self.includeCurrencyInfo:
            self.data["includeCurrencyInfo"] = self.includeCurrencyInfo
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock


        super(GetAccountExchangeRequests, self).__init__(rt = "getAccountExchangeRequests", data=self.data)

    def run(self):
        super(GetAccountExchangeRequests, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountExchangeRequests, self).getData(key)    # calls 'BaseGet.getData()'