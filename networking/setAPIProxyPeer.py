# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class SetAPIProxyPeer(Parent):
    def __init__(self, peer=None, adminPassword=None):
        """
            SetAPIProxyPeer Blacklist a remote node from the UI, so it won't be used when in roaming and light client modes.
            POST only.

            SetAPIProxyPeer take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Set_API_Proxy_Peer

            REQUEST
            :param peer : (S) is the IP address or domain name of the peer (plus optional port)
            :param adminPassword : is a string (S) with the admin password (O)

            RESPONSE
            :return downloadedVolume : (N) is the number of bytes downloaded by the peer
            :return address : (S) the IP address or DNS name of the peer
            :return weight : (N) is the peer's weight value
            :return uploadedVolume : (N) is the number of bytes uploaded by the peer
            :return version : (S) is the version of the software running on the peer
            :return platform : (S) is a string representing the peer's platform
            :return blockchainState : (S) is a string describing the state of the blockchain in the peer
            :return lastUpdated : (N) is the timestamp (in seconds since the genesis block) of the last peer status update
            :return blacklisted : (B) is true if the peer is blacklisted
            :return services : (A) is an array of strings with the services the node provides
            :return apiPort : (N) is the API access port of the peer
            :return apiSSLPort : (N) is the SSL API access port of the peer
            :return blacklistingCause : (S) is the cause of blacklisting (if blacklisted is true)
            :return announcedAddress : (S) is the name that the peer announced to the network (could be a DNS name, IP address, or any other string)
            :return application : (S) is the name of the software application, typically NRS
            :return state : (N) defines the state of the peer: 0 for NON_CONNECTED, 1 for CONNECTED, or 2 for DISCONNECTED
            :return shareAddress : (B) is true if the address is allowed to be shared with other peers
            :return inbound : (B) is true if the peer has made a request to this node
            :return inboundWebSocket : (B) is true if an inbound websocket has been established from this node
            :return outboundWebSocket : (B) is true if an outbound websocket has been established to this node
            :return lastConnectAttempt : (B) is the timestamp (in seconds since the genesis block) of the last connection attempt to the peer
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
        self._peer = peer
        self._adminPassword = adminPassword

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        if self.peer:
            self.data["peer"] = self.peer
        if self.adminPassword:
            self.data["adminPassword"] = self.adminPassword

        super(SetAPIProxyPeer, self).__init__(rt="setAPIProxyPeer", data=self.data)

    @property
    def peer(self):
        return self._peer

    @peer.setter
    def peer(self, value):
        self._peer = value

    @property
    def adminPassword(self):
        return self._adminPassword

    @adminPassword.setter
    def adminPassword(self, value):
        self._adminPassword = value

    def run(self):
        super(SetAPIProxyPeer, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(SetAPIProxyPeer, self).getData(key)  # calls 'BasePost.getData()'

