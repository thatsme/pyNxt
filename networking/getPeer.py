# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPeer(Parent):

    def __init__(self, peer = None):
        """
            GetPeer Get information about a given peer.
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Peer

            REQUEST
            :param peer : (S) is the IP address or domain name of the peer (plus optional port)

            RESPONSE
            :return isNewlyAdded : (B) is true if the peer was not already known, omitted otherwise
            :return hallmark : (S) is the hex string of the peer's hallmark, if it is defined
            :return downloadedVolume : (N) is the number of bytes downloaded by the peer
            :return address : (S) the IP address or DNS name of the peer
            :return weight : (N) is the peer's weight value
            :return uploadedVolume : (N) is the number of bytes uploaded by the peer
            :return version : (S) is the version of the software running on the peer
            :return platform : (S) is a string representing the peer's platform
            :return lastUpdated : (N) is the timestamp (in seconds since the genesis block) of the last peer status update
            :return blacklisted : (B) is true if the peer is blacklisted
            :return services : (A) is an array of strings with the services the node provides
            :return blacklistingCause : (S) is the cause of blacklisting (if blacklisted is true)
            :return announcedAddress : (S) is the name that the peer announced to the network
                                        (could be a DNS name, IP address, or any other string)
            :return application : (S) is the name of the software application, typically NRS
            :return state : (N) defines the state of the peer: 0 for NON_CONNECTED, 1 for CONNECTED, or 2 for DISCONNECTED
            :return shareAddress : (B) is true if the address is allowed to be shared with other peers
            :return inbound : (B) is true if the peer has made a request to this node
            :return inboundWebSocket : (B) is true if an inbound websocket has been established from this node
            :return outboundWebSocket : (B) is true if an outbound websocket has been established to this node
            :return lastConnectAttempt : (B) is the timestamp (in seconds since the genesis block) of the last connection attempt to the peer
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

        self.peer = peer

        # Initialize dictionary
        self.data = {}

        if self.peer:
            self.data["peer"] = self.peer

        super(GetPeer, self).__init__(rt = "getPeer", data=self.data)

    def run(self):
        super(GetPeer, self).run()                                 # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPeer, self).getData(key)                   # calls 'BaseGet.getData()'