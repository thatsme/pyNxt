# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountCurrencies(Parent):

    def __init__(self, account=None, currency=None, height=None, includeCurrencyInfo=False, requireBlock=None, requireLastBlock=None):
        """
            GetAccountCurrencies take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Currencies

            REQUEST
            accounts : is the id of accounts (S) (R)
            currency : is a currency ID filter (S) (O)
            height : is the blockchain height at which the response applies (N) (O) (default is the current height)
            includeCurrencyInfo : is true if several currency information properties is to be included (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            accountCurrencies : is an array (A)  of currency objects with the following fields:
            > code (S) is the currency code
            > unconfirmedUnits (S) is the amount of unconfirmed currency units (in QNT)
            > decimals (N) is the number of currency decimal places
            > name (S) is the currency name
            > currency (S) is the currency ID
            > units (S) is the amount of currency (in QNT)
            > issuanceHeight (N) is the blockchain height of issuance for a reservable currency
            > type (N) is the currency type bitmask (refer to Get Currency)
            > issuerAccountRS (S) is the Reed-Solomon address of the issuer accounts
            > issuerAccount (S) is the issuer accounts ID
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
        self.currency = currency
        self.height = height
        self.includeCurrencyInfo = includeCurrencyInfo
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
        if self.height:
            self.data["height"] = self.height
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock


        super(GetAccountCurrencies, self).__init__(rt = "getAccountCurrencies", data=self.data)

    def run(self):
        super(GetAccountCurrencies, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrencies, self).getData(key)               # calls 'BaseGet.getData()'