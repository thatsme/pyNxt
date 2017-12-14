# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetScheduledTransactions(Parent):

    def __init__(self, account=None):
        """
            Get scheduled transactions

            GetScheduledTransactions take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Scheduled_Transactions

            REQUEST
            :param accounts : is the accounts ID (O)

            RESPONSE
            :return scheduledTransactions : is an array (A) of scheduled transaction
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

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = account

        super(GetScheduledTransactions, self).__init__(rt = "getScheduledTransactions", data=self.data)

    def run(self):
        super(GetScheduledTransactions, self).run()                 # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetScheduledTransactions, self).getData(key)    # calls 'BaseGet.getData()'