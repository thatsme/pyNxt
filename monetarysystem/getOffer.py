# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetOffer(Parent):
    def __init__(self, offer=None, requireBlock=None, requireLastBlock=None ):
        """
            Get offer details given an offer ID.

            GetOffer take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Offer

            REQUEST
            :param currency : is the mintable currency ID (S)
            :param account is the minting account ID
            :param units is the amount (in QNT) of currency to mint
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return sellOffer and buyOffer : (O) are objects with the following fields:
            :return > offer : (S) is the offer ID
            :return > expirationHeight : (N) is the blockchain height of offer expiration
            :return > accountRS : (S) is the Reed-Solomon address of the offering account
            :return > limit : (S) is the cumulative limit of currency buys or sells
            :return > currency : (S) is the currency ID
            :return > supply : (S) is the current currency supply
            :return > account : (S) is the offering account number
            :return > height : (N) is the blockchain height of offer creation
            :return > rateNQT : (S) is the currency exchange rate (in NQT per QNT)
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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
        self.offer = offer

        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["offer"] = self.offer

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetOffer, self).__init__(rt="getOffer", data=self.data)

    def run(self):
        super(GetOffer, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetOffer, self).getData(key)                           # calls 'BaseGet.getData()'
