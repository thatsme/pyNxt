from base.BaseGet import BaseGet as Parent

class RsConvert(Parent):

    def __init__(self, account=None ):

        self.account = account

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = account

        super(RsConvert, self).__init__(rt = "rsConvert", data=self.data)

    def run(self):
        super(RsConvert, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(RsConvert, self).getData(key)    # calls 'BaseGet.getData()'