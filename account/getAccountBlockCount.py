from base.BaseGet import BaseGet as Parent

class GetAccountBlockCount(Parent):

    def __init__(self):
        super(GetAccountBlockCount, self).__init__(rt = "getAccountBlockCount")

    def run(self):
        super(GetAccountBlockCount, self).run()  # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountBlockCount, self).getData(key)  # calls 'BaseGet.getData()'