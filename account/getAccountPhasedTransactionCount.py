# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountPhasedTransactionCount(Parent):

    def __init__(self, account=None, requireBlock=None, requireLastBlock=None):
        """
            Get the number of pending phased transactions associated with an account given the account ID.

            GetAccountPhasedTransactionCount take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Phased_Transaction_Count

            REQUEST
            account : is the id of account (S) (R)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            numberOfPhasedTransactions (N) is the number of pending phased transactions
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
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
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountPhasedTransactionCount, self).__init__(rt = "getAccountPhasedTransactionCount", data=self.data)

    def run(self):
        super(GetAccountPhasedTransactionCount, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountPhasedTransactionCount, self).getData(key)       # calls 'BaseGet.getData()'