# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class CanDeleteCurrency(Parent):

    def __init__(self, account=None, currency=None, requireBlock = None, requireLastBlock=None ):
        """
            Decrypt an AES-encrypted message.

            CanDeleteCurrency take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Can_Delete_Currency

            REQUEST
            :param account : is the account ID (S)
            :param currency : is the currency ID (S)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return canDelete (B) is true if the currency can be deleted, false otherwise
            :return lastBlock (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

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

        self.account = account
        self.currency = currency
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["currency"] = self.currency

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(CanDeleteCurrency, self).__init__(rt = "canDeleteCurrency", data=self.data)

    def run(self):
        super(CanDeleteCurrency, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(CanDeleteCurrency, self).getData(key)             # calls 'BaseGet.getData()'