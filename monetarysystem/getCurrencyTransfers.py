# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetCurrencyTransfers(Parent):
    def __init__(self, currency=None, account = None, timestamp=None, includeCurrencyInfo=False, ri=None, rb=None ):
        """
            Get currency transfers given a currency ID and/or an account ID in reverse block height order
            (or in expected order of execution for expected transfers).

            GetCurrencyTransfers take a default 1/5 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currency_Transfers

            REQUEST
            :param currency : is the currency ID (S)
            :param account : is an account ID (S)(O)
            :param timestamp : is the earliest transfer (in seconds since the genesis block) to retrieve (optional, does not apply to expected transfers)
            :param includeCurrencyInfo : is true (B) to include some currency fields (optional, does not apply to expected transfers)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return :transfers : (A) is an array of transfer objects with the following fields for each transfer:
            :return > code (S) is the currency code
            :return > units (S) is the amount (in QNT) of the transfer
            :return > issuanceHeight (N) is the blockchain height of the currency issuance for a reservable currency
            :return > type (N) is the currency type bitmask (refer to Get Currency for details)
            :return > issuerAccountRS (S) is the Reed-Solomon address of the issuer account
            :return > transfer (S) is the transfer ID
            :return > senderRS (S) is the Reed-Solomon address of the sender account
            :return > sender (S) is the account number of the sender account
            :return > recipientRS (S) is the Reed-Solomon address of the recipient account
            :return > decimals (N) is the number of decimal places used by the currency
            :return > recipient (S) is the account number of the recipient account
            :return > name (S) is the currency name
            :return > currency (S) is the currency ID
            :return > issuerAccount (S) is the issuer account ID
            :return > height (N) is the blockchain height of the transfer
            :return > timestamp (N) is the timestamp (in seconds since the genesis block) of the transfer block, does not apply to an expected transfer
            :return > phased (B) is true if the transaction is phased, false otherwise, applies only to an expected transfer
            :return > issuerAccountRS (S) is the Reed-Solomon address of the issuer account
            :return > issuerAccount (S) is the issuer account ID
            :return requestProcessingTime : (N) is the API request processing time (in millisec)
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
        self._currency  = currency
        self._account = account
        self._timestamp = timestamp
        self._includeCurrencyInfo = includeCurrencyInfo
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["currency"] = self.currency
        self.data["account"] = self.account
        self.data["timestamp"] = self.timestamp
        self.data["includeCurrencyInfo"] = self.includeCurrencyInfo

        super(GetCurrencyTransfers, self).__init__(rt="getCurrencyTransfers", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def includeCurrencyInfo(self):
        return self._includeCurrencyInfo

    @includeCurrencyInfo.setter
    def includeCurrencyInfo(self, value):
        self._includeCurrencyInfo = value

    @property
    def ri(self):
        return self._ri

    @ri.setter
    def ri(self, value):
        self._ri = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetCurrencyTransfers, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetCurrencyTransfers, self).getData(key)                           # calls 'BaseGet.getData()'
