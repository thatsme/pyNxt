# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetInboundPeers(Parent):

    def __init__(self, includePeerInfo=False):
        """
            Get all peers that have sent a request to this peer in the last 30 minutes.

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Inbound_Peers

            REQUEST
            :param includePeerInfo is true (B) to include peer information, otherwise include only the address (O)

            RESPONSE
            :return peers : is an array of peers objects (A) (unless the asset parameter is specified) with the following fields for each asset:
            > ....
            >
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

        self._includePeerInfo = includePeerInfo

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        if self.includePeerInfo:
            self.data["includePeerInfo"] = self.includePeerInfo

        super(GetInboundPeers, self).__init__(rt = "getInboundPeers", data=self.data)

    @property
    def includePeerInfo(self):
        return self._includePeerInfo

    @includePeerInfo.setter
    def includePeerInfo(self, value):
        self._includePeerInfo = value

    def run(self):
        super(GetInboundPeers, self).run()                                 # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetInboundPeers, self).getData(key)                   # calls 'BaseGet.getData()'