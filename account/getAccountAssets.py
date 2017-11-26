from base.BaseGet import BaseGet as Parent

class GetAccountAssets(Parent):

    def __init__(self, account=None, assets=None, height=None, includeAssetsInfo=False, requireBlock=None, requireLastBlock=None):


        self.account = account
        self.assets = assets
        self.height = height
        self.includeAssetsInfo = includeAssetsInfo
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.assets:
            self.data["assets"] = self.assets
        if self.includeAssetsInfo:
            self.data["includeAssetsInfo"] = self.includeAssetsInfo
        if self.height:
            self.data["height"] = self.height
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountAssets, self).__init__(rt = "getAccountAssets", data=self.data)

    def run(self):
        super(GetAccountAssets, self).run()                                 # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountAssets, self).getData(key)                   # calls 'BaseGet.getData()'