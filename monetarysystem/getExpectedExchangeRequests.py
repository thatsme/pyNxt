# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetExpectedExchangeRequests(Parent):

    def __init__(self, account=None, currency=None, includeCurrencyInfo=False, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):
        """
            Get the exchange requests associated with a given accounts and/or currency in reverse chronological
            order (or in expected order of execution for expected requests).

            GetExpectedExchangeRequests take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Expected_Exchange_Requests

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param currency : is the currency ID (optional for expected requests if accounts provided)
            :param includeCurrencyInfo : is true to include the response fields
                                    code, decimals, name, issuanceHeight, type, timestamp,
                                    issuerAccountRS and issuerAccount (optional, applies only to expected requests)
            :param firstIndex : is a zero-based index to the first order ID to retrieve (N) (O)
            :param lastIndex : is a zero-based index to the last order ID to retrieve (N) (O)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            :return exchangeRequests : is an array (A) of requests with the following fields for each request:
            > code (S) is a currency code
            > subtype (N) is 5 for buy and 6 for sell
            > decimals (N) is the number of decimal places
            > name (S) is the currency name
            > units (S) is the number of currency units to buy or sell (in QNT)
            > issuanceHeight (N) is the blockchain height of issuance for a reservable currency, zero otherwise
            > type (N) is the currency type bitmask (refer to Get Currency)
            > transaction (S) is the transaction ID
            > timestamp (N) is the timestamp (in seconds since the genesis block) of the block when the request was executed
            > rateNQT (S) is the exchange rate (in NQT per QNT)
            > issuerAccountRS (S) is the Reed-Solomon address of the issuer accounts
            > issuerAccount (S) is the issuer accounts ID
            > phased (B) is true if the transaction is phased (applies only to expected requests)
            :param lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :param requestProcessingTime : is the API request processing time (N) (in millisec)

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
        self.includeCurrencyInfo = includeCurrencyInfo
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.currency:
            self.data["currency"] = self.currency
        if self.includeCurrencyInfo:
            self.data["includeCurrencyInfo"] = self.includeCurrencyInfo
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock


        super(GetExpectedExchangeRequests, self).__init__(rt = "getExpectedExchangeRequests", data=self.data)

    def run(self):
        super(GetExpectedExchangeRequests, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetExpectedExchangeRequests, self).getData(key)    # calls 'BaseGet.getData()'