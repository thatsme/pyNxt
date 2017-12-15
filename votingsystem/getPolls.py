# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPolls(Parent):

    def __init__(self, account=None, timestamp=None, includeFinished=False, finishedOnly=False, ri=None, rb=None):
        """
            Get poll details in reverse creation order.

            GetPolls take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Polls

            REQUEST
            :param account : is a creation account ID filter (O)
            :param timestamp : is the earliest poll (in seconds since the genesis block) to retrieve (O)
            :param firstIndex : is a zero-based index to the first poll to retrieve (O)
            :param lastIndex : is a zero-based index to the last poll to retrieve (O)
            :param includeFinished : is true to include completed polls (B) (O)
            :param finishedOnly is true to exclude not yet executed, phased transactions (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return polls (A) is an array of polls (refer to Get Poll for details)
            :return lastBlock (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime (N) is the API request processing time (in millisec)

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

        self.account = account
        self.timestamp = timestamp
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.includeFinished = includeFinished
        self.finishedOnly = finishedOnly
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        self.data["timestamp"] = self.timestamp
        self.data["includeFinished"] = self.includeFinished
        self.data["finishedOnly"] = self.finishedOnly

        super(GetPolls, self).__init__(rt = "getPolls", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetPolls, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPolls, self).getData(key)               # calls 'BaseGet.getData()

