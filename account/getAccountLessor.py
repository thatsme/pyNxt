from base.BaseGet import BaseGet as Parent

class GetAccountLessor(Parent):

    def __init__(self):

        super(GetAccountLessor, self).__init__(rt = "getAccountLessor")

    def run(self):
        super(GetAccountLessor, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountLessor, self).getData(key)    # calls 'BaseGet.getData()'