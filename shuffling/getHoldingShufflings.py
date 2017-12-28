# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetHoldingShufflings(Parent):

    def __init__(self, holding=False, stage=None, includeFinished=False, adminPassword=None, ri=None, rb=None):
        """
            Retrieves info about shufflings for a specific holding and/or stage.

            GetHoldingShufflings take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Holding_Shufflings

            REQUEST
            :param holding : is the holding ID (S) (O)
            :param stage : is the stage of the shuffling (See Get Constants for type definitions) (O)
            :param includeFinished : is true to include completed shufflings (B) (O)
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

        self._holding = holding
        self._stage = stage
        self._includeFinished = includeFinished
        self._adminPassword = adminPassword
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["holding"] = self.holding
        self.data["stage"] = self.stage
        self.data["includeFinished"] = self.includeFinished

        if self.adminPassword:
            self.data["adminPassword"] = self.adminPassword

        super(GetHoldingShufflings, self).__init__(rt = "getHoldingShufflings", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def holding(self):
        return self._holding

    @holding.setter
    def holding(self, value):
        self._holding = value

    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value

    @property
    def includeFinished(self):
        return self._includeFinished

    @includeFinished.setter
    def includeFinished(self, value):
        self._includeFinished = value

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
        super(GetHoldingShufflings, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetHoldingShufflings, self).getData(key)               # calls 'BaseGet.getData()