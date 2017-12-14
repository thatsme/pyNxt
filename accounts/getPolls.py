# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPolls(Parent):

    def __init__(self, account=None, timestamp=0, includeFinished=False, finishedOnly=False, ri=None, rb=None ):
        """
            Get poll details in reverse creation order.

            GetPolls take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Polls

            REQUEST
            :param accounts : is the accounts ID (O)
            :param timestamp : is the earliest poll (in seconds since the genesis block) to retrieve (N) (O)
            :param includeFinished : is true to include completed polls (B) (O)
            :param finishedOnly : is true to exclude not yet executed, phased transactions (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return polls : is an array (A) of polls (refer to Get Poll for details)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
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

        self.account = account
        self.timestamp = timestamp
        self.includeFinished = includeFinished
        self.finishedOnly = finishedOnly
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = account
        self.data["timestamp"] = timestamp

        self.data["includeFinished"] = self.includeFinished
        self.data["finishedOnly"] = self.finishedOnly

        super(GetPolls, self).__init__(rt = "getPolls", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetPolls, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPolls, self).getData(key)    # calls 'BaseGet.getData()'