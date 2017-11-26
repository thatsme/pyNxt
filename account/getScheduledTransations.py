from base.BaseGet import BaseGet as Parent

class GetScheduledTransactions(Parent):

    def __init__(self, account=None):

        self.account = account

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = account

        super(GetScheduledTransactions, self).__init__(rt = "getScheduledTransactions", data=self.data)

    def run(self):
        super(GetScheduledTransactions, self).run()                 # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetScheduledTransactions, self).getData(key)    # calls 'BaseGet.getData()'