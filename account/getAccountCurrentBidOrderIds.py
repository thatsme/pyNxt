from base.BaseGet import BaseGet as Parent

class GetAccountCurrentBidOrderIds(Parent):

    def __init__(self):

        super(GetAccountCurrentBidOrderIds, self).__init__(rt = "getAccountCurrentBidOrderIds")

    def run(self):
        super(GetAccountCurrentBidOrderIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrentBidOrderIds, self).getData(key)    # calls 'BaseGet.getData()'