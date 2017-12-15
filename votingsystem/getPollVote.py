# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPollVote(Parent):

    def __init__(self, poll=None, account=None, includeWeights=False, rb=None):
        """
            Get a poll vote given a poll ID and an account ID.

            GetPollVote take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Poll_Vote

            REQUEST
            :param poll : is the poll ID
            :param account : is the account ID
            :param includeWeights : is true to calculate and return the weight assigned to each vote (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return votes : (A) is an array of votes, the range values (S) corresponding to each option (answer) with empty strings for non-votes
            :return voter : (S) is the account number of the voter
            :return voterRS : (S) is the Reed-Solomon address of the voter
            :return transaction : (S) is the transaction ID of the vote
            :return weight : (S) is the weight assigned to each vote (applies if includeWeights is true)
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
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

        self.poll = poll
        self.account = account
        self.includeWeights = includeWeights
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["poll"] = self.poll
        self.data["account"] = self.account
        self.data["includeWeights"] = self.includeWeights

        super(GetPollVote, self).__init__(rt = "getPollVote", data=self.data)

    def run(self):
        super(GetPollVote, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPollVote, self).getData(key)               # calls 'BaseGet.getData()

