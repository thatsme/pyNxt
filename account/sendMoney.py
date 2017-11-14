from base.BasePost import BasePost as Parent

class SendMoney(Parent):
    def __init__(self, recipient = None, amountNQT=0, publicKey = None, secretPhrase=None, feeNQT = None, deadline = 0, phasing = None, message=None ):
        """
            SendMoney take a default 5 parameter as explained in NXT API Documentation ( is deadLine requested or not ? )

            Class is working with  post method, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request


            https://nxtwiki.org/wiki/The_Nxt_API#Send_Money


            recipient : account id of recipient
            amountNQT : is the amount in NQT to put in transaction
            publicKey : publicKey of sender account ( does not get in broadcast )
            secretPhrase : secret Phrase of sender account
            feeNQT : fee for sending transaction if 0 minimum is set ( 100000000 NQT )
            deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )


        """

        # Required parameters
        self.recipient = recipient
        self.amountNQT = amountNQT
        self.publicKey = publicKey
        self.secretPhrase = secretPhrase
        if feeNQT == 0:
            self.feeNQT = 100000000
        else:
            self.feeNQT = feeNQT

        if deadline == 0:
            self.deadline = 60
        else:
            self.deadline = deadline

        self.phasing = phasing
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
        super(SendMoney, self).__init__(rt = "sendMoney", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(SendMoney, self).run()               # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(SendMoney, self).getData(key)    # calls 'BasePost.getData()'

