from base.BaseGet import BaseGet as Parent

class GetAccountCurrencies(Parent):

    def __init__(self, account=None, currency=None, height=None, includeCurrencyInfo=False, requireBlock=None, requireLastBlock=None):

        self.account = account
        self.currency = currency
        self.height = height
        self.includeCurrencyInfo = includeCurrencyInfo
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
        if self.height:
            self.data["height"] = self.height
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock


        super(GetAccountCurrencies, self).__init__(rt = "getAccountCurrencies", data=self.data)

    def run(self):
        super(GetAccountCurrencies, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrencies, self).getData(key)               # calls 'BaseGet.getData()'