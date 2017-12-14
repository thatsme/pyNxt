# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class ParseTransaction(Parent):


    def __init__(self, transactionBytes=None, transactionJSON=None, requireBlock=None, requireLastBlock=None):
        """
            Get a transaction object given a (signed or unsigned) transaction bytecode, or re-parse a transaction object. Verify the signature.

            ParseTransaction take a default 1 parameter as explained in NXT API Documentation ( is deadLine requested or not ? )

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Parse_Transaction

            REQUEST
            :param transactionBytes : is the signed or unsigned bytecode of the transaction (O)
            :param transactionJSON : is the transaction object (optional if transactionBytes is included)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return verify (B) is true if the signature is verified, false otherwise

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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter
        """




        # is the block ID of a block that must be present in the blockchain during execution (optional)

        self.transactionBytes = transactionBytes
        self.transactionJSON = transactionJSON
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["transactionBytes"] = self.transactionBytes
        self.data["transactionJSON"] = self.transactionJSON

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(ParseTransaction, self).__init__(rt = "parseTransaction", data=self.data)

    def run(self):
        """
        Run rest request
        """
        super(ParseTransaction, self).run()                               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(ParseTransaction, self).getData(key)                 # calls 'BaseGet.getData()'

    def phelp(self):
        print(ParseTransaction.__doc__)

