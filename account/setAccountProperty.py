from base.BasePost import BasePost as Parent

class SetAccountProperty(Parent):
    def __init__(self, recipient = None, property=None, value=None, secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing = None, message=None ):
        """
            SetAccountProperty take a default 5 parameter as explained in NXT API Documentation ( is deadLine requested or not ? )

            Class is working with  post method, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request


            https://nxtwiki.org/wiki/The_Nxt_API#Set_Account_Property

            property : is the name of the property ( required )
            recipient : is the account where a property should be removed (optional)
            setter : is the account who did set the property (optional)
            * secretPhrase : secret Phrase of account where we want remove a property ( required or at lease ** )
            ** publicKey : publicKey of account where we want remove a property ( does not get in broadcast ) ( required or at least *)
            feeNQT : fee for sending transaction if 0 minimum is set ( 100000000 NQT )
            deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )

        """

        # Required parameters
        self.recipient = recipient
        self.property = property
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

        # Optional parameters
        self.referencedTransactionFullHash = referencedTransactionFullHash
        self.broadcast = broadcast
        self.value = value


        self.phasing = phasing
        self.message = message

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["recipient"] = self.recipient
        self.data["value"] = self.value
        self.data["property"] = self.property
        if publicKey:
            self.data["publicKey"] = self.publicKey
        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline
        if self.referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash
        if self.broadcast:
            self.data["broadcast"] = self.broadcast

        super(SetAccountProperty, self).__init__(rt="setAccountProperty", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(SetAccountProperty, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(SetAccountProperty, self).getData(key)  # calls 'BasePost.getData()'
