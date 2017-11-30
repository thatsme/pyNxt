# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrenciesByIssuer(Parent):

    def __init__(self, account=None, firstIndex=None, lastIndex=None, includeCounts=False, requireBlock=None, requireLastBlock=None):
        """
            Get currencies issued by multiple accounts in reverse creation order.

            GetCurrenciesByIssuer take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currencies_By_Issuer

            REQUEST
            accounts : is array (A) of accounts ID's (S) / Multiaccount parameters (3)
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            currencies : is an array of arrays (A) of currency objects, where the outer array is indexed by the given accounts IDs
                        (refer to Get Currency for details about the currency objects)
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

        self.accounts = [None]*3
        for a in account[:3]:
            self.accounts.append(a)

        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.includeCounts = includeCounts
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        for a in self.accounts:
            self.data["accounts"] = a

        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.includeCounts:
            self.data["includeCounts"] = self.includeCounts
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock


        super(GetCurrenciesByIssuer, self).__init__(rt = "getCurrenciesByIssuer", data=self.data)

    def run(self):
        super(GetCurrenciesByIssuer, self).run()                        # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetCurrenciesByIssuer, self).getData(key)          # calls 'BaseGet.getData()'