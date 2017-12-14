# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetFundingMonitor(Parent):

    def __init__(self, secretPhrase=None, adminPassword=None, includeMonitoredAccounts=False, property=None, holdingType=None, holding=None, account=None):
        """
            Get a funding monitor.

            GetFundingMonitor take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Funding_Monitor

            REQUEST
            :param secretPhrase is the secret phrase of the funding account, used to get a single monitor. (optional)
            :param adminPassword is the admin password, used to get a single monitor or all monitors (optional if secretPhrase is provided)
            :param includeMonitoredAccounts is true to include account info of the monitored accounts (optional)
            :param property is the name of the account property (optional)
            :param holdingType is a string representing the holding type (optional)
            :param holding is the holding ID (optional)
            :param account is the account ID (optional)

            RESPONSE
            :return monitors : (A) is an array of monitor objects including the following fields:
            >  holding : (S) is the holding ID
            >  amount : (S) is the amount to fund the monitored accounts with (NQT or QNT)
            >  monitoredAccounts : (A) is an array of monitored account objects including the following fields
                (only if includeMonitoredAccounts is true):
                > amount : (S) is the amount to fund the monitored accounts with. Overrides amount in parent object.
                > account : (S) is the monitored account ID
                > accountRS : (S) is the monitored account Reed Solomon address
                > threshold : (S) is the threshold. Overrides threshold in parent object.
                > interval : (N) is the interval. Overrides interval in parent object.
            > holdingType : (N) is the holding type
            > account : (S) is the monitoring account ID
            > accountRS : (S) is the Reed Solomon address of the monitoring account
            > property : (S) is the account property
            > threshold : (S) is the threshold
            > interval : (N) is the interval
            :return requestProcessingTime (N) is the API request processing time (in millisec)

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

        self.secretPhrase = secretPhrase
        self.adminPassword = adminPassword
        self.includeMonitoredAccounts = includeMonitoredAccounts
        self.property = property
        self.holdingType = holdingType
        self.holding = holding
        self.account = account

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        if self.secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        if self.adminPassword:
            self.data["adminPassword"] = self.adminPassword

        self.data["includeMonitoredAccounts"] = self.includeMonitoredAccounts
        self.data["property"] = self.property
        self.data["holdingType"] = self.holdingType
        self.data["holding"] = self.holding
        self.data["account"] = self.account

        super(GetFundingMonitor, self).__init__(rt = "getFundingMonitor", data=self.data)

    def run(self):
        super(GetFundingMonitor, self).run()                        # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetFundingMonitor, self).getData(key)          # calls 'BaseGet.getData()'