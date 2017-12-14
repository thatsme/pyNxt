# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountExchangeRequests(Parent):

    def __init__(self, account=None, currency=None, includeCurrencyInfo=False, ri=None, rb=None):
        """
            Get the exchange requests associated with a given accounts and/or currency in reverse chronological
            order (or in expected order of execution for expected requests).

            GetAccountExchangeRequests take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Exchange_Requests

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param currency : is the currency ID (optional for expected requests if accounts provided)
            :param includeCurrencyInfo : is true to include the response fields
                                    code, decimals, name, issuanceHeight, type, timestamp,
                                    issuerAccountRS and issuerAccount (optional, applies only to expected requests)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self.account = account
        self.currency = currency
        self.includeCurrencyInfo = includeCurrencyInfo
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.currency:
            self.data["currency"] = self.currency
        if self.includeCurrencyInfo:
            self.data["includeCurrencyInfo"] = self.includeCurrencyInfo

        super(GetAccountExchangeRequests, self).__init__(rt = "getAccountExchangeRequests", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetAccountExchangeRequests, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountExchangeRequests, self).getData(key)    # calls 'BaseGet.getData()'