from base.BaseGet import BaseGet as Parent

class GetUnconfirmedTransactionIds(Parent):

    ## Multiaccount parameters (3)
    def __init__(self):

        super(GetUnconfirmedTransactionIds, self).__init__(rt = "getUnconfirmedTransationIds")

    def run(self):
        super(GetUnconfirmedTransactionIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetUnconfirmedTransactionIds, self).getData(key)    # calls 'BaseGet.getData()'