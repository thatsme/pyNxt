from base.BaseGet import BaseGet as Parent

class GetAccountCurrencyCount(Parent):

    def __init__(self):

        super(GetAccountCurrencyCount, self).__init__(rt = "getAccountCurrencyCount")

    def run(self):
        super(GetAccountCurrencyCount, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrencyCount, self).getData(key)    # calls 'BaseGet.getData()'