# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class StartForging(Parent):
    def __init__(self, secretPhrase=None):
        """
            Start or stop forging with an account, or check to see if an account is forging. POST only.

            StartForging take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Start_Forging

            REQUEST
            :param secretPhrase : (S) is the secret passphrase of the account
                    (optional for stopForging and getForging if password protected like the Debug Operations)

            RESPONSE
            :return deadline : (N) is the estimated time (in seconds since the last block) until the account will forge
                                a block (startForging and getForging only)
            :return hitTime : (N) is the estimated time (in seconds since the genesis block) when the account will forge
                                a block (startForging and getForging only)
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
        self.secretPhrase = secretPhrase

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase

        super(StartForging, self).__init__(rt="startForging", data=self.data)

    def run(self):
        super(StartForging, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(StartForging, self).getData(key)  # calls 'BasePost.getData()'
