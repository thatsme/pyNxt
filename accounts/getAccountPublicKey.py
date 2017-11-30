# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountPublicKey(Parent):

    def __init__(self, account=None, requireBlock=None, requireLastBlock=None):
        """
            Get the public key associated with an accounts ID.

            GetAccountPublicKey take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Public_Key

            REQUEST
            accounts : is the accounts ID (S)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            publicKey (S) is the 32-byte public key associated with the accounts, returned as a hex string
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
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountPublicKey, self).__init__(rt = "getAccountPublicKey", data=self.data)

    def run(self):
        super(GetAccountPublicKey, self).run()                  # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountPublicKey, self).getData(key)    # calls 'BaseGet.getData()'