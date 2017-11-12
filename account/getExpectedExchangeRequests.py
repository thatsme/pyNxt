from base.BaseGet import BaseGet as Parent

class GetExpectedExchangeRequests(Parent):

    def __init__(self, ):

        super(GetExpectedExchangeRequests, self).__init__(rt = "getExpectedExchangeRequests")

    def run(self):
        super(GetExpectedExchangeRequests, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetExpectedExchangeRequests, self).getData(key)    # calls 'BaseGet.getData()'