# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPeers(Parent):

    def __init__(self, active = False, state=None, includePeerInfo=False, service=None):
        """
            GetPeers Get a list of peer IP addresses.
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Peers

            REQUEST
            :param active : (B) is true for active (not NON_CONNECTED) peers only (optional, if true overrides state)
            :param state : (S) is the state of the peers, one of NON_CONNECTED, CONNECTED, or DISCONNECTED (optional)
            :param includePeerInfo : (B) is true to include peer detail as in Get Peer
            :param service : (S) to filter on a specific service

            RESPONSE
            :return peers (A) is an array of peer addresses
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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
                (WP) Wrapper Meta-parameter

        """

        self.active = active
        self.state = state
        self.includePeerInfo = includePeerInfo
        self.service = service

        # Initialize dictionary
        self.data = {}
        self.data["active"] = self.active
        self.data["includePeerInfo"] = self.includePeerInfo

        if self.state:
            self.data["state"] = self.state
        if self.service:
            self.data["service"] = self.service

        super(GetPeers, self).__init__(rt = "getPeers", data=self.data)

    def run(self):
        super(GetPeers, self).run()                                 # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPeers, self).getData(key)                   # calls 'BaseGet.getData()'