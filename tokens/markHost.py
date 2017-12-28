# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class MarkHost(Parent):
    def __init__(self, host=None, weight=None, date=None,  secretPhrase=None):
        """
            Generates a node hallmark. POST only.

            MarkHost take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Mark_Host

            REQUEST
            :param secretPhrase : is the secret passphrase for the account that will be hallmarked on the node (S)
            :param host : is the IP address or domain name of the node (S)
            :param weight : is the weight to assign to the node
            :param date : is the current date in YYYY-MM-DD format

            Note: Refer to Create Hallmark for details.

            RESPONSE
            :return hallmark (S) is the hallmark hex string
            :return requestProcessingTime (N) is the API request processing time (in millisec)

            Note: Refer to Create Hallmark for instructions for applying the hallmark to a public node.

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
        self._host = host
        self._weight = weight
        self._date = date

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["host"] = self.host
        self.data["weight"] = self.weight
        self.data["date"] = self.date
        self.data["secretPhrase"] = self.secretPhrase

        super(MarkHost, self).__init__(rt="markHost", data=self.data)

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    def run(self):
        super(MarkHost, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(MarkHost, self).getData(key)  # calls 'BasePost.getData()'

