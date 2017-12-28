# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPollVotes(Parent):

    def __init__(self, poll=None, includeWeights=False, ri=None, rb=None):
        """
            Get all votes on a poll in reverse chronological order.

            GetPollVotes take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Poll_Votes

            REQUEST
            :param poll : is the poll ID
            :param includeWeights : is true to calculate and return the weight assigned to each vote (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return votes : (A) is an array of vote objects (refer to Get Poll Vote for details)
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

            Note: Votes are deleted from the database 1441 blocks after the poll is finished.
            Only aggregate results are kept (refer to Get Poll Result).

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

        self._poll = poll
        self._includeWeights = includeWeights
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["poll"] = self.poll
        self.data["account"] = self.account
        self.data["includeWeights"] = self.includeWeights

        super(GetPollVotes, self).__init__(rt = "getPollVotes", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def poll(self):
        return self._poll

    @poll.setter
    def poll(self, value):
        self._poll = value

    @property
    def includeWeights(self):
        return self._includeWeights

    @includeWeights.setter
    def includeWeights(self, value):
        self._includeWeights = value

    @property
    def ri(self):
        return self._ri

    @ri.setter
    def ri(self, value):
        self._ri = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetPollVotes, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPollVotes, self).getData(key)               # calls 'BaseGet.getData()

