# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class BuyAlias(Parent):
    def __init__(self, alias = None, aliasName=None, amountNQT=0, secretPhrase=None,  publicKey = None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=False, phasing = None, message=None, recipientPublicKey=None, ecBlockId=None, ecBlockHeight=None ):
        """
            BuyAlias take a default 5 parameter as explained in NXT API Documentation ( is deadLine requested or not ? )

            Class is working with  post method, and create a transaction, for more info about transactions please refer to

            https://nxtwiki.org/wiki/The_Nxt_API#Buy_Alias

            property : is the name of the property ( required )
            recipient : is the account where a property should be removed (optional)
            setter : is the account who did set the property (optional)
            * secretPhrase : secret Phrase of account where we want remove a property ( required or at lease ** )
            ** publicKey : publicKey of account where we want remove a property ( does not get in broadcast ) ( required or at least *)
            feeNQT : fee for sending transaction if 0 minimum is set ( 100000000 NQT )
            deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )

        """

        # Required parameters
        self.alias = alias
        self.aliasName = aliasName
        self.amountNQT = amountNQT
        self.publicKey = publicKey
        self.secretPhrase = secretPhrase
        if feeNQT == 0:
            self.feeNQT = 100000000
        else:
            self.feeNQT = feeNQT

        # Optional parameters
        self.referencedTransactionFullHash = referencedTransactionFullHash
        self.broadcast = broadcast

        if deadline == 0:
            self.deadline = 60
        else:
            self.deadline = deadline

        self.phasing = phasing
        self.message = message

        self.recipientPublicKey = recipientPublicKey
        self.ecBlockId = ecBlockId
        self.ecBlockHeight = ecBlockHeight

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["alias"] = self.alias
        self.data["aliasName"] = self.aliasName
        self.data["amoungNQT"] = self.amountNQT
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

        if self.recipientPublicKey:
            self.data["recipientPublicKey"] = self.recipientPublicKey

        if self.ecBlockId:
            self.data["ecBlockId"] = self.ecBlockId

        if self.ecBlockHeight:
            self.data["ecBlockHeight"] = self.ecBlockHeight

        super(BuyAlias, self).__init__(rt="buyAlias", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(BuyAlias, self).run()                                   # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(BuyAlias, self).getData(key)                       # calls 'BasePost.getData()'
