from base.BaseGet import BaseGet as Parent

class GetAccount(Parent):


    def __init__(self):

        super(GetAccount, self).__init__()
        self.requestType = "getAccount"

    def run(self):
        super(GetAccount, self).run()               # calls 'BaseGet.run()'

    def getData(self):
        return super(GetAccount, self).getData()    # calls 'BaseGet.getData()'


