from base.BaseGet import BaseGet as Parent

class GetAccountBlockIds(Parent):

    def __init__(self):

        super(GetAccountBlockIds, self).__init__(rt = "getAccountBlockIds")

    def run(self):
        super(GetAccountBlockIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountBlockIds, self).getData(key)    # calls 'BaseGet.getData()'