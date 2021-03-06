# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBidOrder(Parent):
    def __init__(self, order=None, rb=None ):
        """
            Get a bid/ask order given an order ID.

            GetBidOrder take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Bid_Order

            REQUEST
            :param order : is the Order ID
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return accounts : is the accounts number associated with the order (S)
            :return accountRS : is the Reed-Solomon address of the accounts (S)
            :return asset : is the ID of the asset being ordered (S)
            :return quantityQNT : is the order quantity (in QNT) (S)
            :return priceNQT : is the order price (in NQT) (S)
            :return height : is the block height of the order transaction (N)
            :return transactionHeight : is the transaction height (N)
            :return transactionIndex : is a zero-based index giving the order of the transaction in its block (N)
            :return order : is the ID of the order (S)
            :return type : is the type of order (bid or ask) (S)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
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
        self._order = order
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["order"] = self.order

        super(GetBidOrder, self).__init__(rt="getBidOrder", data=self.data, rb=self.rb)

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetBidOrder, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBidOrder, self).getData(key)                           # calls 'BaseGet.getData()'
