from base.BasePost import BasePost as Parent

class GetAccountId(Parent):

    def __init__(self, publicKey=None, secretPhrase=None):

        self.publicKey = publicKey
        self.secretPhrase = secretPhrase

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["publicKey"] = self.publicKey
        self.data["secretPhrase"] = self.secretPhrase

        super(GetAccountId, self).__init__(rt = "getAccountId", data=self.data)

    def run(self):
        super(GetAccountId, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountId, self).getData(key)       # calls 'BaseGet.getData()'