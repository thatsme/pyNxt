# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class DeleteScheduledTransaction(Parent):
    def __init__(self, transaction = None):
        """
            DeleteScheduledTransaction take a default 1 parameter as explained in NXT API Documentation

            API is working with POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Delete_Scheduled_Transaction

            REQUEST
            :param transaction : is the name of the transaction (S) (R)

            RESPONSE

            Legenda
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

        # Required parameters
        self.transaction = transaction
        self.phasing = None
        self.message = None

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["transaction"] = self.transaction

        super(DeleteScheduledTransaction, self).__init__(rt="deleteScheduledTransaction", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(DeleteScheduledTransaction, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(DeleteScheduledTransaction, self).getData(key)  # calls 'BasePost.getData()'


