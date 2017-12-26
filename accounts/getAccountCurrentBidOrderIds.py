# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountCurrentBidOrderIds(Parent):

    def __init__(self, account=None, assets=None, ri=None, rb=None):
        """
            GetAccountCurrentBidOrderIds take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Current_Bid_Order_Ids

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param asset : is an asset ID filter (S) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return bidOrderIds or askOrderIds : is an array (A) of order IDs
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

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

        self._account = account
        self._assets = assets
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["assets"] = self.assets

        super(GetAccountCurrentBidOrderIds, self).__init__(rt = "getAccountCurrentBidOrderIds", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def assets(self):
        return self._assets

    @assets.setter
    def assets(self, value):
        self._assets = value

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
        super(GetAccountCurrentBidOrderIds, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountCurrentBidOrderIds, self).getData(key)    # calls 'BaseGet.getData()'