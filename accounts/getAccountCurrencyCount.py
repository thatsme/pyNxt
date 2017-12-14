# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountCurrencyCount(Parent):

    def __init__(self, account=None, height=None, rb=None):
        """
            GetAccountCurrencyCount take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Currency_Count

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param height : is the height of the blockchain to determine the asset count (N) (O) (default is last block)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return numberOfCurrencies : is the number of currencies issued (N)
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
        self.height = height
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.height:
            self.data["height"] = self.height

        super(GetAccountCurrencyCount, self).__init__(rt = "getAccountCurrencyCount", data=self.data, rb=self.rb)

    def run(self):
        super(GetAccountCurrencyCount, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountCurrencyCount, self).getData(key)    # calls 'BaseGet.getData()'