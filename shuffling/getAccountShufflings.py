# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountShufflings(Parent):

    def __init__(self, account=None, includeFinished=False, includeHoldingInfo=False, adminPassword=None, ri=None, rb=None):
        """
            Retrieves info about shufflings for a specific account.

            GetAccountShufflings take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Shufflings

            REQUEST
            :param account : is the account ID (S)
            :param includeFinished : is true to include completed shufflings (B) (O)
            :param includeHoldingInfo is true to include holding info (B) (O)
            :param adminPassword is a string with the admin password (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return shufflings : (A) is an array containing the shuffling object (refer to Get Shuffling)
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

        self._account = account
        self._includeFinished = includeFinished
        self._includeHoldingInfo = includeHoldingInfo
        self._adminPassword = adminPassword
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        self.data["includeFinished"] = self.includeFinished
        self.data["includeHoldingInfo"] = self.includeHoldingInfo

        if self.adminPassword:
            self.data["adminPassword"] = self.adminPassword

        super(GetAccountShufflings, self).__init__(rt = "getAccountShufflings", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def includeFinished(self):
        return self._includeFinished

    @includeFinished.setter
    def includeFinished(self, value):
        self._includeFinished = value

    @property
    def includeHoldingInfo(self):
        return self._includeHoldingInfo

    @includeHoldingInfo.setter
    def includeHoldingInfo(self, value):
        self._includeHoldingInfo = value

    @property
    def adminPassword(self):
        return self._adminPassword

    @adminPassword.setter
    def adminPassword(self, value):
        self._adminPassword = value

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
        super(GetAccountShufflings, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountShufflings, self).getData(key)               # calls 'BaseGet.getData()'