from base.BaseGet import BaseGet as Parent

class GetAccountPublicKey(Parent):

    def __init__(self):

        super(GetAccountPublicKey, self).__init__(rt = "getAccountPublicKey")

    def run(self):
        super(GetAccountPublicKey, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountPublicKey, self).getData(key)    # calls 'BaseGet.getData()'