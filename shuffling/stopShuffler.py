# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class StopShuffler(Parent):
    def __init__(self, account=None, shufflingFullHash=None, adminPassword=None, secretPhrase=None):
        """
            Starts a automated Shuffler. Once started, the Shuffler monitors the blockchain state for transactions relevant to the specified shuffle, and automatically submits the required transactions on behalf of the user,
            performing shuffle processing, verification, or cancellation as needed.

            StopShuffler take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Stop_Shuffler

            REQUEST
            :param account : is the account ID (optional if shufflingFullHash or secretPhrase or adminPassword is provided)
            :param shufflingFullHash : is the full hash of the shuffling (optional if account or adminPassword is provided)
            :param secretPhrase : is the secret phrase of the account entering the shuffling (optional if adminPassword is provided)
            :param adminPassword : is the admin password (optional if secretPhrase is provided)

            RESPONSE
            :return stoppedShuffler : (B) means the specified shuffler was stopped
            :return stoppedAllShufflers : (B) means all shufflers on the node was stopped (only if adminPassword is provided in request)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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
        self.account = account
        self.shufflingFullHash = shufflingFullHash
        self.adminPassword = adminPassword
        self.secretPhrase = secretPhrase

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["shufflingFullHash"] = self.shufflingFullHash
        self.data["account"] = self.account
        self.data["adminPassword"] = self.adminPassword
        self.data["secretPhrase"] = self.secretPhrase

        super(StopShuffler, self).__init__(rt="stopShuffler", data=self.data)

    def run(self):
        super(StopShuffler, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(StopShuffler, self).getData(key)  # calls 'BasePost.getData()'

