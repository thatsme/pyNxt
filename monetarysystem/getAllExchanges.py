# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAllExchanges(Parent):
    def __init__(self, timestamp=None, firstIndex=None, lastIndex=None, includeCurrencyInfo=False, requireBlock=None, requireLastBlock=None ):
        """
            Get all currency exchanges in reverse chronological order.

            GetAllExchanges take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_All_Exchanges

            REQUEST
            :param timestamp : is the earliest timestamp to retrieve (O)
            :param firstIndex : is a zero-based index to the first alias to retrieve (O)
            :param lastIndex : is a zero-based index to the last alias to retrieve (O)
            :param includeCurrencyInfo : is true to include some currency details (B) (O)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return assets : is an array (A) of asset objects (refer to Get Asset)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)

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
        self.timestamp = timestamp
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.includeCurrencyInfo = includeCurrencyInfo
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["timestamp"] = self.timestamp
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex

        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex

        if self.includeCurrencyInfo:
            self.data["includeCurrencyInfo"] = self.includeCurrencyInfo

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAllExchanges, self).__init__(rt="getAllExchanges", data=self.data)

    def run(self):
        super(GetAllExchanges, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAllExchanges, self).getData(key)                           # calls 'BaseGet.getData()'
