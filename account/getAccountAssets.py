from base.BaseGet import BaseGet as Parent

class GetAccountAssets(Parent):

    def __init__(self):
        super(GetAccountAssets, self).__init__(rt = "getAccountAssets")

    def run(self):
        super(GetAccountAssets, self).run()  # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountAssets, self).getData(key)  # calls 'BaseGet.getData()'