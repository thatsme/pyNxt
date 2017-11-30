# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetGuaranteedBalance(Parent):

    def __init__(self, account=None, numberOfConfirmations=0, requireBlock=None, requireLastBlock=None ):
        """
            Get the balance of an accounts that is confirmed at least a specified number of times.

            GetGuaranteedBalance take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Guaranteed_Balance

            REQUEST
            accounts : is accounts ID (S)
            numberOfConfirmations : is the minimum number of confirmations for a transaction to be included in the guaranteed balance (N) (O),
                                    if omitted or zero then minimally confirmed transactions are included)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            guaranteedBalanceNQT : is the balance (in NQT) of the accounts with at least numberOfConfirmations confirmations (S)
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            requestProcessingTime : is the API request processing time (N) (in millisec)

            Legenda :
                ° the parameter are interchangeable on
                * if you use the secretPhrase , the transaction is immediately broadcasted to network
                ** if you use the publicKey, you create an unsigned Transaction, and you need to sign and broardcast
                *** for buying
                (R) Required
                (O) Optional
                (N) Number
                (S) String
                (B) Boolean
                (A) Array
                (O) Object
                >   Array Element
                (WP) Wrapper specific parameter

        """


        self.account = account
        self.numberOfConfirmations = numberOfConfirmations
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = account

        if self.numberOfConfirmations:
            self.data["numberOfConfirmations"] = self.numberOfConfirmations
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetGuaranteedBalance, self).__init__(rt = "getGuaranteedBalance", data=self.data)

    def run(self):
        super(GetGuaranteedBalance, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetGuaranteedBalance, self).getData(key)               # calls 'BaseGet.getData()'