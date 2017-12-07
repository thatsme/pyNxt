# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class BlacklistAPIProxyPeer(Parent):
    def __init__(self, peer=None):
        """
            Blacklist a remote node from the UI, so it won't be used when in roaming and light client modes.
            POST only.

            BlacklistAPIProxyPeer take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Blacklist_API_Proxy_Peer

            REQUEST
            :param peer : (S) is the IP address or domain name of the peer (plus optional port)
            :param adminPassword : is a string (S) with the admin password (O)

            RESPONSE
            :return done : (B) is true if the peer was not already known, omitted otherwise
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
                (O) Object
                >   Array Element
                (WP) Wrapper Meta-parameter


        """

        # Required parameters
        self.peer = peer

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        if peer:
            self.data["peer"] = self.peer

        super(BlacklistAPIProxyPeer, self).__init__(rt="blacklistAPIProxyPeer", data=self.data)

    def run(self):
        super(BlacklistAPIProxyPeer, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(BlacklistAPIProxyPeer, self).getData(key)  # calls 'BasePost.getData()'

