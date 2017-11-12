from base.BaseGet import BaseGet as Parent

class GetAccountCurrentBidOrders(Parent):

    def __init__(self):

        super(GetAccountCurrentBidOrders, self).__init__(rt = "getAccountCurrentBidOrders")

    def run(self):
        super(GetAccountCurrentBidOrders, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrentBidOrders, self).getData(key)    # calls 'BaseGet.getData()'