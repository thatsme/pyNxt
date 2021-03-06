# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class StopFundingMonitor(Parent):
    def __init__(self, pproperty=None, account=None, adminPassword=None, secretPhrase=None, holdingType=None, holding=None ):
        """
            Stop a funding monitor. When the secret phrase is specified, a single monitor will be stopped.
            The monitor is identified by the secret phrase, holding and accounts property.
            The administrator password is not required and will be ignored.

            When the administrator password is specified, a single monitor can be stopped by specifying the funding accounts,
            holding and accounts property. If no accounts is specified, all monitors will be stopped.

            The holding type and accounts property name must be specified when the secret phrase or accounts is specified.
            Holding type codes are listed in getConstants. In addition, the holding identifier must be specified
            when the holding type is ASSET or CURRENCY.

            StopFoundingMonitor take a default 5 parameter as explained in NXT API Documentation

            API is working with POST method only

            https://nxtwiki.org/wiki/The_Nxt_API#Stop_Founding_Monitor

            REQUEST
            :param pproperty : is the name of the accounts property (S) (O)
            :param adminPassword : is the admin password, used to stop a single monitor or all monitors (optional if secretPhrase is provided)
            :param secretPhrase : is the secret phrase of the funding accounts (S)
            :param account : is the account ID (S) (O)
            :param holdingType : is a string representing the holding type (S) (O)
            :param holding : is the holding ID (S) (O)


            RESPONSE
            :return stopped : is the number of the monitors that have been stopped (N)
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

        self.pproperty = pproperty
        self.account = account
        self.adminPassword = adminPassword
        self.secretPhrase = secretPhrase
        self.holdingType = holdingType
        self.holding = holding

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["property"] = self.pproperty
        self.data["account"] = self.account
        self.data["secretPhrase"] = self.secretPhrase

        if self.adminPassword:
            self.data["adminPassword"] = self.adminPassword

        if self.holdingType:
            self.data["holdingType"] = self.holdingType

        if self.holding:
            self.data["holding"] = self.holding

        super(StopFundingMonitor, self).__init__(rt = "stopFundingMonitor", data=self.data)

    @property
    def pproperty(self):
        return self._pproperty

    @pproperty.setter
    def pproperty(self, value):
        self._pproperty = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def adminPassword(self):
        return self._adminPassword

    @adminPassword.setter
    def adminPassword(self, value):
        self._adminPassword = value

    @property
    def holding(self):
        return self._holding

    @holding.setter
    def holding(self, value):
        self._holding = value

    @property
    def holdingType(self):
        return self._holdingType

    @holdingType.setter
    def holdingType(self, value):
        self._holdingType = value


    def run(self):
        super(StopFundingMonitor, self).run()                    # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(StopFundingMonitor, self).getData(key)      # calls 'BasePost.getData()'


