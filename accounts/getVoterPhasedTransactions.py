# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetVoterPhasedTransactions(Parent):

    def __init__(self, account=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get pending phased transactions which include a whitelist in reverse chronological creation order.
            These transactions can be considered transaction approval requests.

            GetVoterPhasedTransactions take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Voter_Phased_Transactions

            REQUEST
            accounts :  is a whitelisted accounts ID included in the phased transactions (R)
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            Refer to Get Transaction for details.


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
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = account

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetVoterPhasedTransactions, self).__init__(rt = "getVoterPhasedTransactions", data=self.data)

    def run(self):
        super(GetVoterPhasedTransactions, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetVoterPhasedTransactions, self).getData(key)       # calls 'BaseGet.getData()'