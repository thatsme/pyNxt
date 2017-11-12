from base.BaseGet import BaseGet as Parent

class GetGuaranteedBalance(Parent):

    def __init__(self, ):

        super(GetGuaranteedBalance, self).__init__(rt = "getGuaranteedBalance")

    def run(self):
        super(GetGuaranteedBalance, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetGuaranteedBalance, self).getData(key)    # calls 'BaseGet.getData()'