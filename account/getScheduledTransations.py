from base.BaseGet import BaseGet as Parent

class GetScheduledTransactions(Parent):

    def __init__(self, ):

        super(GetScheduledTransactions, self).__init__(rt = "getScheduledTransactions")

    def run(self):
        super(GetScheduledTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetScheduledTransactions, self).getData(key)    # calls 'BaseGet.getData()'