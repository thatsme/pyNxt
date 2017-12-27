# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class StopForging(Parent):
    def __init__(self, secretPhrase=None):
        """
            Start or stop forging with an account, or check to see if an account is forging. POST only.

            StopForging take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Stop_Forging

            REQUEST
            :param secretPhrase : (S) is the secret passphrase of the account
                    (optional for stopForging and getForging if password protected like the Debug Operations)

            RESPONSE
            :return foundAndStopped : (B) is true if forging was stopped, false if forging was already stopped (stopForging only)
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
        self._secretPhrase = secretPhrase

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase

        super(StopForging, self).__init__(rt="stopForging", data=self.data)

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    def run(self):
        super(StopForging, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(StopForging, self).getData(key)  # calls 'BasePost.getData()'
