# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetExchangesByOffer(Parent):
    def __init__(self, offer=None, includeCurrencyInfo=False, ri=None, rb=None ):
        """
            Get currency exchanges given an exchange request transaction ID in reverse chronological order.

            GetExchangesByOffer take a default 1/5 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Exchanges_By_Offer

            REQUEST
            :param offer : (S) is a currency offer ID
            :param includeCurrencyInfo : is true (B) to include some currency fields (optional, does not apply to expected transfers)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return exchanges : (A) is an array of exchange objects with the following fields for each exchange:
            :return > seller : (S) is the seller account number
            :return > code : (S) is the currency code
            :return > sellerRS : (S) is the Reed-Solomon address of the seller account
            :return > units : (S) is the amount of currency exchanged (in QNT)
            :return > issuanceHeight : (N) is the blockchain height of currency issuance for a reservable currency
            :return > type : (N) is the currency type bitmask (refer to Get Currency for details)
            :return > rateNQT : (S) is the currency exchange rate (in NQT per QNT)
            :return > buyer : (S) is the account number of the buyer
            :return > offer : (S) is the offer ID
            :return > buyerRS : (S) is the Reed-Solomon address of the buyer account
            :return > decimals : (N) is the number of decimal places used by the currency
            :return > name : (S) is the currency name
            :return > currency : (S) is the currency ID
            :return > block : (S) is the block ID of the block containing the exchange transaction
            :return > transaction : (S) is the transaction ID of the exchange
            :return > timestamp : (N) is the timestamp (in seconds since the genesis block) of the exchange
            :return > height : is the blockchain height of the block containing the exchange transaction
            :return > issuerAccountRS : (S) is the Reed-Solomon address of the issuer account
            :return > issuerAccount : (S) is the issuer account ID
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
        self._offer  = offer
        self._includeCurrencyInfo = includeCurrencyInfo
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["offer"] = self.offer
        self.data["includeCurrencyInfo"] = self.includeCurrencyInfo

        super(GetExchangesByOffer, self).__init__(rt="getExchangesByOffer", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def offer(self):
        return self._offer

    @offer.setter
    def offer(self, value):
        self._offer = value

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
        super(GetExchangesByOffer, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetExchangesByOffer, self).getData(key)                           # calls 'BaseGet.getData()'
