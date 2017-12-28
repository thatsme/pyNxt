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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self._active = active
        self._state = state
        self._includePeerInfo = includePeerInfo
        self._service = service

        # Initialize dictionary
        self.data = {}
        self.data["active"] = self.active
        self.data["includePeerInfo"] = self.includePeerInfo

        if self.state:
            self.data["state"] = self.state
        if self.service:
            self.data["service"] = self.service

        super(GetPeers, self).__init__(rt = "getPeers", data=self.data)

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def includePeerInfo(self):
        return self._includePeerInfo

    @includePeerInfo.setter
    def includePeerInfo(self, value):
        self._includePeerInfo = value

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value

    def run(self):
        super(GetPeers, self).run()                                 # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPeers, self).getData(key)                   # calls 'BaseGet.getData()'