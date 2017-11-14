from base.BasePost import BasePost as Parent

class SendMoney(Parent):
    def __init__(self,recipient = None, amountNQT=0, publicKey = None, secretPhrase=None, feeNQT = None, deadline = 0, message = None ):

        self.recipient = recipient
        self.amountNQT = amountNQT
        self.publicKey = publicKey
        self.secretPhrase = secretPhrase
        if feeNQT == 0:
            self.feeNQT = 100000000
        else:
            self.feeNQT = feeNQT
        self.deadline = deadline
        self.message = message

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        
        self.data["recipient"] = self.recipient
        self.data["amountNQT"] = self.amountNQT
        if publicKey:
            self.data["publicKey"] = self.publicKey
        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline
        self.data["message"] = self.message
        super(SendMoney, self).__init__(rt = "sendMoney", data=self.data)

    def run(self):
        super(SendMoney, self).run()               # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(SendMoney, self).getData(key)    # calls 'BasePost.getData()'

