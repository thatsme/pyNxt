from base.BaseGet import BaseGet as Parent

class GetAccountCurrentAskOrderIds(Parent):

    def __init__(self):

        super(GetAccountCurrentAskOrderIds, self).__init__(rt = "getAccountCurrentAskOrderIds")

    def run(self):
        super(GetAccountCurrentAskOrderIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrentAskOrderIds, self).getData(key)    # calls 'BaseGet.getData()'