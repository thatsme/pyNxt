from base.BaseGet import BaseGet as Parent

class GetBlockchainTransactions(Parent):

    def __init__(self, ):

        super(GetBlockchainTransactions, self).__init__(rt = "getBlockchainTransactions")

    def run(self):
        super(GetBlockchainTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBlockchainTransactions, self).getData(key)    # calls 'BaseGet.getData()'