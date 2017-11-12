from base.BaseGet import BaseGet as Parent

class GetAccountLedger(Parent):

    def __init__(self):

        super(GetAccountLedger, self).__init__(rt = "getAccountLedger")

    def run(self):
        super(GetAccountLedger, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountLedger, self).getData(key)    # calls 'BaseGet.getData()'ß