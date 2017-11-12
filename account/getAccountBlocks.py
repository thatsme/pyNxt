from base.BaseGet import BaseGet as Parent

class GetAccountBlocks(Parent):

    def __init__(self):

        super(GetAccountBlocks, self).__init__(rt = "getAccountBlocks")

    def run(self):
        super(GetAccountBlocks, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountBlocks, self).getData(key)    # calls 'BaseGet.getData()'