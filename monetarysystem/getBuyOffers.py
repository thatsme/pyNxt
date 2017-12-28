# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBuyOffers(Parent):
    def __init__(self, currency=None, account=None, availableOny=False, sortByRate=False, ri=None, rb=None ):
        """
            Get currency buy or sell offers given a currency ID and/or an account ID in order of rate
            (if sortByRate is true for expected offers, otherwise in the expected order of execution).

            GetBuyOffers take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Buy_Offers

            REQUEST
            :param currency : is the currency ID (S)
            :param account : is the account ID (optional if currency provided) (S)
            :param availableOnly : is true (B)to include only offers with non-zero supply and limit, but is ignored when both
                            currency and account are given (optional, does not apply to expected offers)
            :param sortByRate : is true (B) to sort by rate (optional, applies only to expected offers,
                            which are returned in expected order of execution by default)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        # Required parameters
        self._currency = currency
        self._account = account
        self._availableOny = availableOny
        self._sortByRate = sortByRate
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["currency"] = self.currency
        self.data["account"] = self.account
        self.data["availableOny"] = self.availableOny
        self.data["sortByRate"] = self.sortByRate

        super(GetBuyOffers, self).__init__(rt="getBuyOffers", data=self.data, ri=self.ri, rb=self.rb)

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
    def availableOny(self):
        return self._availableOny

    @availableOny.setter
    def availableOny(self, value):
        self._availableOny = value

    @property
    def sortByRate(self):
        return self._sortByRate

    @sortByRate.setter
    def sortByRate(self, value):
        self._sortByRate = value

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
        super(GetBuyOffers, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetBuyOffers, self).getData(key)                           # calls 'BaseGet.getData()'
