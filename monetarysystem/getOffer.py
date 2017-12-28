# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetOffer(Parent):
    def __init__(self, offer=None, rb=None ):
        """
            Get offer details given an offer ID.

            GetOffer take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Offer

            REQUEST
            :param offer : is the offer ID (S)
            :param rb : rb object ( check base/Rb.py) (WP)

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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        # Required parameters
        self._offer = offer
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["offer"] = self.offer

        super(GetOffer, self).__init__(rt="getOffer", data=self.data, rb=self.rb)

    @property
    def offer(self):
        return self._offer

    @offer.setter
    def offer(self, value):
        self._offer = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetOffer, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetOffer, self).getData(key)                           # calls 'BaseGet.getData()'
