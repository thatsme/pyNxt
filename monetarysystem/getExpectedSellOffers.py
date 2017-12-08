# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetExpectedSellOffers(Parent):
    def __init__(self, currency=None, account=None, availableOny=False, sortByRate=False,  requireBlock=None, requireLastBlock=None ):
        """
            Get currency buy or sell offers given a currency ID and/or an account ID in order of rate
            (if sortByRate is true for expected offers, otherwise in the expected order of execution).

            GetExpectedSellOffers take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Expected_Sell_Offers

            REQUEST
            :param currency : is the currency ID (S)
            :param account : is the account ID (optional if currency provided) (S)
            :param availableOnly : is true (B)to include only offers with non-zero supply and limit, but is ignored when both
                            currency and account are given (optional, does not apply to expected offers)
            :param sortByRate : is true (B) to sort by rate (optional, applies only to expected offers,
                            which are returned in expected order of execution by default)
            :param firstIndex : is a zero-based index to the first offer to retrieve (optional, does not apply to expected offers)
            :param lastIndex : is a zero-based index to the last offer to retrieve (optional, does not apply to expected offers)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return offers : (A) is an array of buy or sell offer objects (refer to Get Offer for details)
                                with the following additional field only for an expected offer:
            :return > phased : (B) is true if the offer is phased, false otherwise
            :return lastBlock (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
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
        self.currency = currency
        self.account = account
        self.availableOny = availableOny
        self.sortByRate = sortByRate
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["currency"] = self.currency
        self.data["account"] = self.account
        self.data["availableOny"] = self.availableOny
        self.data["sortByRate"] = self.sortByRate

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetExpectedSellOffers, self).__init__(rt="getExpectedSellOffers", data=self.data)

    def run(self):
        super(GetExpectedSellOffers, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetExpectedSellOffers, self).getData(key)                           # calls 'BaseGet.getData()'
