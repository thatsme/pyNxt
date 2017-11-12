from base.BaseGet import BaseGet as Parent

class GetAccountPhasedTransactionCount(Parent):

    def __init__(self):

        super(GetAccountPhasedTransactionCount, self).__init__(rt = "getAccountPhasedTransactionCount")

    def run(self):
        super(GetAccountPhasedTransactionCount, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountPhasedTransactionCount, self).getData(key)    # calls 'BaseGet.getData()'