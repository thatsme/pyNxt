# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrency(Parent):
    def __init__(self, currency=None, code = None,  includeCounts=False, rb=None ):
        """
            Get the details of a currency.

            GetCurrency take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currency

            REQUEST
            :param currency : is the currency ID (S) (O)
            :param code : is the currency code (optional if currency provided)
            :param includeCounts : (B) is true to include numberOf... fields (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return initialSupply : (S) is the initial currency supply (in QNT)
            :return currentReservePerUnitNQT : (S) is the minimum currency reserve (in NQT per QNT)
            :return types : (A) is an array of currency types, one or more of:
            :return > EXCHANGEABLE
            :return > CONTROLLABLE
            :return > RESERVABLE
            :return > CLAIMABLE
            :return > MINTABLE
            :return > NON_SHUFFLEABLE
            :return code : (S) is the currency code
            :return creationHeight : (N) is the blockchain height of the currency creation
            :return minDifficulty : (N) is the minimum difficulty for a mintable currency
            :return numberOfTransfers : (N) is the number of currency transfers
            :return description : (S) is the currency description
            :return minReservePerUnitNQT : (S) is the minimum currency reserve (in NQT per QNT) for a reservable currency
            :return currentSupply : (S) is the current currency supply (in QNT)
            :return issuanceHeight : (N) is the blockchain height of the currency issuance for a reservable currency
            :return requestProcessingTime : (N) is the API request processing time (in millisec)
            :return type : (N) is the currency type bitmask, from least to most significant bit: exchangeable, controllable, reservable, claimable, mintable, non-shuffleable
            :return reserveSupply : (S) is the reserve currency supply (in NQT) for a reservable currency
            :return maxDifficulty : (N) is the maximum difficulty for a mintable currency
            :return accountRS : (S) is the Reed-Solomon address of the issuing account
            :return decimals : (N) is the number of decimal places used by the currency
            :return name : (S) is the name of the currency
            :return numberOfExchanges : (N) is the number of currency exchanges
            :return currency : (S) is the currency ID
            :return maxSupply : (S) is the maximum currency supply (in QNT)
            :return account : (S) is the account ID of the currency issuer
            :return algorithm : (N) is the algorithm number for a mintable currency: 2 for SHA256, 3 for SHA3, 5 for Scrypt, 25 for Keccak25
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)

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

        # Required parameters
        self.currency  = currency
        self.code = code
        self.includeCounts = includeCounts
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["code"] = self.code
        self.data["includeCounts"] = self.includeCounts

        super(GetCurrency, self).__init__(rt="getCurrency", data=self.data, rb=self.rb)

    def run(self):
        super(GetCurrency, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetCurrency, self).getData(key)                           # calls 'BaseGet.getData()'
