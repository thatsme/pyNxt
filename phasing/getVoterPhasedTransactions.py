# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetVoterPhasedTransaction(Parent):
    def __init__(self, account=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None ):
        """
            Get pending phased transactions which include a whitelist in reverse chronological creation order.
            These transactions can be considered transaction approval requests.

            GetVoterPhasedTransaction take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Voter_Phased_Transaction

            REQUEST
            :param account is a whitelisted account ID included in the phased transactions
            :param firstIndex : is a zero-based index to the first vote to retrieve (O)
            :param lastIndex : is a zero-based index to the last vote to retrieve (O)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

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
                (WP) Wrapper Meta-parameter

        """

        # Required parameters
        self.account = account
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetVoterPhasedTransaction, self).__init__(rt="getVoterPhasedTransaction", data=self.data)

    def run(self):
        super(GetVoterPhasedTransaction, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetVoterPhasedTransaction, self).getData(key)                           # calls 'BaseGet.getData()'
