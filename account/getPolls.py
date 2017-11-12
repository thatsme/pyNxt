from base.BaseGet import BaseGet as Parent

class GetPolls(Parent):

    def __init__(self, ):

        super(GetPolls, self).__init__(rt = "getPolls")

    def run(self):
        super(GetPolls, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetPolls, self).getData(key)    # calls 'BaseGet.getData()'