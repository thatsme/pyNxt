# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class StartFundingMonitor(Parent):
    def __init__(self, property=None, amount=None, threshold=None, interval=0, secretPhrase=None, holdingType=None, holding=None ):
        """
            Starts a funding monitor that will transfer NXT, ASSET or CURRENCY from the funding account to a recipient account
            when the amount held by the recipient account drops below the threshold.
            The transfer will not be done until the current block height is greater than equal to the block height
            of the last transfer plus the interval. The funding account is identified by the secret phrase.

            The recipient accounts are identified by the specified account property (see Set Account Property).
            Each account that has this property set by the funding account will be monitored for changes.
            The property value can be omitted or it can consist of a JSON string containing one
            or more values in the format: {"amount":long,"threshold":long,"interval":integer}

            StartFoundingMonitor take a default 5 parameter as explained in NXT API Documentation

            Class is working with POST method only

            https://nxtwiki.org/wiki/The_Nxt_API#Start_Founding_Monitor

            REQUEST
            property : is the name of the account property (R)
            amount : is the amount to fund the recipient account with (in NQT or QNT) (N)
            threshold : is the threshold (N)
            interval : is the the number of blocks to wait after before funding the recipient (N)
            * secretPhrase : is the secret phrase of the funding account
            holdingType : is a string representing the holding type (S) (O)
            holding : is the holding ID (S) (O)


            RESPONSE
            started : is true if the monitor has been started (B)
            requestProcessingTime : is the API request processing time (N) (in millisec)

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
                (O) Object
                >   Array Element

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
        return super(StartFundingMonitor, self).getData(key)      # calls 'BasePost.getData()'


