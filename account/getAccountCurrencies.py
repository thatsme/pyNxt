from base.BaseGet import BaseGet as Parent

class GetAccountCurrencies(Parent):

    def __init__(self):

        super(GetAccountCurrencies, self).__init__(rt = "getAccountCurrencies")

    def run(self):
        super(GetAccountCurrencies, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrencies, self).getData(key)    # calls 'BaseGet.getData()'