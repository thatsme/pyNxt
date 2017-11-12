from base.BaseGet import BaseGet as Parent

class GetAccount(Parent):


    def __init__(self):

        super(GetAccount, self).__init__(rt = "getAccount")

    def run(self):
        super(GetAccount, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccount, self).getData(key)    # calls 'BaseGet.getData()'


