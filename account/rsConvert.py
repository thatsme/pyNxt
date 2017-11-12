from base.BaseGet import BaseGet as Parent

class RsConvert(Parent):

    def __init__(self, ):

        super(RsConvert, self).__init__(rt = "rsConvert")

    def run(self):
        super(RsConvert, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(RsConvert, self).getData(key)    # calls 'BaseGet.getData()'