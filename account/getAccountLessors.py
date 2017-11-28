# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountLessors(Parent):

    def __init__(self, account=None, height=None, requireBlock=None, requireLastBlock=None):
        """
            Get the lessors to an account.

            GetAccountLedgerLessor take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Lessor

            REQUEST
            account : is the ledger ID
            height : is the height of the blockchain to determine the lessors (N) (O) ( default is last block)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            accountRS (S) is the Reed-Solomon address of the account
            account (S) is the account number
            height : is the the block height associated with the event (N)
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            lessors : is an array (A) of lessor objects including the fields:
            > lessorRS (S)
            > lessor (S)
            > guaranteedBalanceNQT (S)
            requestProcessingTime : is the API request processing time (N) (in millisec)

            Legenda :
                ° the parameter are interchangable on
                * if you use the secretPhrase , the transaction is immediately broadcasted to network
                ** if you use the publicKey, you create an unsigned Transaction, and you need to sign and broardcast
                *** for buying
                (R) Required
                (O) Optional
                (N) Number
                (S) String
                (B) Boolean
                (A) Array
                >   Array Element

        """

        self.account = account
        self.height = height
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.height:
            self.data["height"] = self.height
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountLessors, self).__init__(rt = "getAccountLessors", data=self.data)

    def run(self):
        super(GetAccountLessors, self).run()                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountLessors, self).getData(key)           # calls 'BaseGet.getData()'