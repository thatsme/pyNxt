# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetScheduledTransactions(Parent):

    def __init__(self, account=None):
        """
            Get scheduled transactions

            GetScheduledTransactions take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Scheduled_Transactions

            REQUEST
            accounts : is the accounts ID (O)

            RESPONSE
            scheduledTransactions : is an array (A) of scheduled transaction
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
                (WP) Wrapper specific parameter

        """

        self.account = account

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = account

        super(GetScheduledTransactions, self).__init__(rt = "getScheduledTransactions", data=self.data)

    def run(self):
        super(GetScheduledTransactions, self).run()                 # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetScheduledTransactions, self).getData(key)    # calls 'BaseGet.getData()'