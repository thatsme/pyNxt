# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class StartFundingMonitor(Parent):
    def __init__(self, property=None, amount=None, threshold=None, interval=0, secretPhrase=None, holdingType=None, holding=None ):
        """
            Starts a funding monitor that will transfer NXT, ASSET or CURRENCY from the funding accounts to a recipient accounts
            when the amount held by the recipient accounts drops below the threshold.
            The transfer will not be done until the current block height is greater than equal to the block height
            of the last transfer plus the interval. The funding accounts is identified by the secret phrase.

            The recipient accounts are identified by the specified accounts property (see Set Account Property).
            Each accounts that has this property set by the funding accounts will be monitored for changes.
            The property value can be omitted or it can consist of a JSON string containing one
            or more values in the format: {"amount":long,"threshold":long,"interval":integer}

            StartFoundingMonitor take a default 5 parameter as explained in NXT API Documentation

            API is working with POST method only

            https://nxtwiki.org/wiki/The_Nxt_API#Start_Founding_Monitor

            REQUEST
            :param property : is the name of the accounts property (R)
            :param amount : is the amount to fund the recipient accounts with (in NQT or QNT) (N)
            :param threshold : is the threshold (N)
            :param interval : is the the number of blocks to wait after before funding the recipient (N)
            :param secretPhrase *: is the secret phrase of the funding accounts
            :param holdingType : is a string representing the holding type (S) (O)
            :param holding : is the holding ID (S) (O)


            RESPONSE
            :return started : is true if the monitor has been started (B)
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

        self.property = property
        self.amount = amount
        self.threshold = threshold
        self.interval = interval
        self.secretPhrase = secretPhrase
        self.holdingType = holdingType
        self.holding = holding

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["property"] = self.property
        self.data["amount"] = self.amount
        self.data["threshold"] = self.threshold
        self.data["interval"] = self.interval
        self.data["secretPhrase"] = self.secretPhrase
        if self.holdingType:
            self.data["holdingType"] = self.holdingType

        if self.holding:
            self.data["holding"] = self.holding

        super(StartFundingMonitor, self).__init__(rt = "startFundingMonitor", data=self.data)

    def run(self):
        super(StartFundingMonitor, self).run()                    # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(StartFundingMonitor, self).getData(key)      # calls 'BasePost.getData()'


