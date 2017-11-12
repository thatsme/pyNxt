from base.BaseGet import BaseGet as Parent

class GetAccountAssetCount(Parent):

    def __init__(self):
        super(GetAccountAssetCount, self).__init__(rt = "getAccountAssetCount")

    def run(self):
        super(GetAccountAssetCount, self).run()  # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountAssetCount, self).getData(key)  # calls 'BaseGet.getData()'