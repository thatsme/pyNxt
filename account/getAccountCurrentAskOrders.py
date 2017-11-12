from base.BaseGet import BaseGet as Parent

class GetAccountCurrentAskOrders(Parent):

    def __init__(self):

        super(GetAccountCurrentAskOrders, self).__init__(rt = "getAccountCurrentAskOrders")

    def run(self):
        super(GetAccountCurrentAskOrders, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrentAskOrders, self).getData(key)    # calls 'BaseGet.getData()'