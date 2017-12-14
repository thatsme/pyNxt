# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountCurrentAskOrders(Parent):

    def __init__(self, account=None, assets=None, ri=None, rb=None):
        """
            GetAccountCurrentAskOrderIds take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Current_Ask_Orders

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param asset : is an asset ID filter (S) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return bidOrders or askOrders (A) is an array of order objects (refer to Get Order for details)
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

        self.account = account
        self.assets = assets
        self.ri = ri
        self.rb=rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["assets"] = self.assets

        super(GetAccountCurrentAskOrders, self).__init__(rt = "getAccountCurrentAskOrders", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetAccountCurrentAskOrders, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountCurrentAskOrders, self).getData(key)    # calls 'BaseGet.getData()'