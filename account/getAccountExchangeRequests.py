from base.BaseGet import BaseGet as Parent

class GetAccountExchangeRequests(Parent):

    def __init__(self):

        super(GetAccountExchangeRequests, self).__init__(rt = "getAccountExchangeRequests")

    def run(self):
        super(GetAccountExchangeRequests, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountExchangeRequests, self).getData(key)    # calls 'BaseGet.getData()'