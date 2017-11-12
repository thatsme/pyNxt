from base.BaseGet import BaseGet as Parent

class GetBalance(Parent):

    def __init__(self, ):

        super(GetBalance, self).__init__(rt = "getBalance")

    def run(self):
        super(GetBalance, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBalance, self).getData(key)    # calls 'BaseGet.getData()'