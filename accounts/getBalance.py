# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBalance(Parent):

    def __init__(self, account=None, includeEffectiveBalance=False, height= None, requireBlock=None, requireLastBlock=None ):
        """
            Get asset information given multiple creation accounts IDs in reverse block height of creation order.

            GetBalance take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Balance

            REQUEST
            accounts : is array (A) of accounts ID's (S) / Multiaccount parameters (3)
            includeEffectiveBalance : is true to include effectiveBalanceNXT and guaranteedBalanceNQT (B) (O)
            height : is the height to retrieve accounts balance for, if still available (N) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            unconfirmedBalanceNQT : is balanceNQT less unconfirmed outgoing transactions, the balance displayed in the client (S)
            guaranteedBalanceNQT : is the balance (in NQT) of the accounts with at least 1440 confirmations (S)
            effectiveBalanceNXT : is the balance (in NXT) of the accounts available for forging: the unleased guaranteedBalance
                                of this accounts plus the leased guaranteedBalance of all lessors to this accounts (N)
            forgedBalanceNQT : is the balance (in NQT) that the accounts has forged (S)
            balanceNQT : is the minimally confirmed basic balance (in NQT) of the accounts (S)
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
        self.includeEffectiveBalance = includeEffectiveBalance
        self.height = height
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.includeEffectiveBalance:
            self.data["includeEffectiveBalance"] = self.includeEffectiveBalance
        if self.height:
            self.data["height"] = self.height
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetBalance, self).__init__(rt = "getBalance", data=self.data)

    def run(self):
        super(GetBalance, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBalance, self).getData(key)    # calls 'BaseGet.getData()'