# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountCurrencyCount(Parent):

    def __init__(self, account=None, height=None, requireBlock=None, requireLastBlock=None):
        """
            GetAccountCurrencyCount take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Currency_Count

            REQUEST
            accounts : is the id of accounts (S) (R)
            height : is the height of the blockchain to determine the asset count (N) (O) (default is last block)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            numberOfCurrencies : is the number of currencies issued (N)
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
        self.height = height
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.height:
            self.data["height"] = self.height
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountCurrencyCount, self).__init__(rt = "getAccountCurrencyCount", data=self.data)

    def run(self):
        super(GetAccountCurrencyCount, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrencyCount, self).getData(key)    # calls 'BaseGet.getData()'