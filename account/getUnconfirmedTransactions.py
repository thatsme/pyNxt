from base.BaseGet import BaseGet as Parent

class GetUnconfirmedTransactions(Parent):

    ## Multiaccount parameters (3)
    def __init__(self):

        super(GetUnconfirmedTransactions, self).__init__(rt = "getUnconfirmedTransactions")

    def run(self):
        super(GetUnconfirmedTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetUnconfirmedTransactions, self).getData(key)    # calls 'BaseGet.getData()'