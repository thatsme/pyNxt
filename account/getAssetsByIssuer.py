from base.BaseGet import BaseGet as Parent

class GetAssetsByIssuer(Parent):

    ## Multiaccount parameters (3)
    def __init__(self, ):

        super(GetAssetsByIssuer, self).__init__(rt = "getAssetsByIssuer")

    def run(self):
        super(GetAssetsByIssuer, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetsByIssuer, self).getData(key)    # calls 'BaseGet.getData()'