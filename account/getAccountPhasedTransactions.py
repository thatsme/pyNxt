from base.BaseGet import BaseGet as Parent

class GetAccountPhasedTransactions(Parent):

    def __init__(self):

        super(GetAccountPhasedTransactions, self).__init__(rt = "getAccountPhasedTransactions")

    def run(self):
        super(GetAccountPhasedTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountPhasedTransactions, self).getData(key)    # calls 'BaseGet.getData()'