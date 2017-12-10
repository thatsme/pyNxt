# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class StartShuffler(Parent):
    def __init__(self, shufflingFullHash=None, recipientSecretPhrase=None, recipientPublicKey=None, secretPhrase=None):
        """
            Starts a automated Shuffler. Once started, the Shuffler monitors the blockchain state for transactions relevant to the specified shuffle, and automatically submits the required transactions on behalf of the user,
            performing shuffle processing, verification, or cancellation as needed.

            StartShuffler take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Start_Shuffler

            REQUEST
            :param secretPhrase : is the secret phrase of the account entering the shuffling
            :param shufflingFullHash : is the full hash of the shuffling
            :param recipientSecretPhrase : is the secret phrase of the recipient account (optional if recipientPublicKey is present)
            :param recipientPublicKey : is the public key of the recipient account (optional if recipientSecretPhrase is present)

            RESPONSE
            :return shuffling (S) is the shuffling ID
            :return shufflingFullHash (S) is the full hash of the shuffling
            :return account (S) is the account ID
            :return accountRS (S) is the account Reed Solomong address
            :return recipient (S) is the account ID of the recipient account
            :return recipientRS (S) is the account Reed Solomon address of the recipient account
            :return requestProcessingTime (N) is the API request processing time (in millisec)

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
        self.shufflingFullHash = shufflingFullHash
        self.recipientSecretPhrase = recipientSecretPhrase
        self.recipientPublicKey = recipientPublicKey

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["shufflingFullHash"] = self.shufflingFullHash
        self.data["recipientSecretPhrase"] = self.recipientSecretPhrase
        self.data["recipientPublicKey"] = self.recipientPublicKey
        self.data["secretPhrase"] = self.secretPhrase

        super(StartShuffler, self).__init__(rt="startShuffler", data=self.data)

    def run(self):
        super(StartShuffler, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(StartShuffler, self).getData(key)  # calls 'BasePost.getData()'

