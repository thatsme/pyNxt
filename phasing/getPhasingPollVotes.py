# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPhasingPollVotes(Parent):
    def __init__(self, transaction=None, ri=None, rb=None ):
        """
            Get all cast phasing poll votes in a phasing poll given a phased transaction ID, if they are still available.

            GetPhasingPollVotes take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Phasing_Poll_Votes

            REQUEST
            :param transaction : is the transaction ID of the phasing poll
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return transaction : (S) is the transaction ID of the phasing poll
            :return account : (S) is the number of the account that created the phasing poll
            :return accountRS : (S) is the Reed-Solomon address of the account that created the phasing poll
            :return finishHeight : (N) is the block height at which the poll finished or will finish
            :return votingModel : (N) is the voting model (refer to Create Transaction Request)
            :return quorum : (S) is the minimum number of votes needed to approve the poll
            :return transactionFullHash : (S) is the full hash of the phasing poll transaction
            :return finished : (B) is true if the poll is finished, false otherwise (omitted if finished is false)
            :return result : (S) is the sum of the result of each account that approved (voted for) the transaction; an account's result is 1 if the voting model is 0, 4 or 5; it is the NQT, asset QNT or currency QNT balance of the account if the voting model is 1, 2 or 3 respectively; however, the result is 0 if minBalance is not met
            :return approved : (B) is true if the poll was approved, false otherwise
            :return minBalance : (S) is the required minimum balance of voting accounts to be eligible to vote
            :return minBalanceModel : (N) is the minimum balance model (refer to Create Transaction Request)
            :return hashedSecret : (S) is the hash of a secret that must be included in each approval (vote) transaction for the approval to be accepted (refer to Create Transaction Request)
            :return linkedFullHashes : (A) is an array of full hashes of linked transactions (omitted if votingModel != 4)
            :return whitelist : (A) is an array of whitelist objects containing the following two fields (omitted if votingModel != 5):
            :return > whitelisted : (S) is the number of the whitelisted account
            :return > whitelistedRS : (S) is the Reed-Solomon address of the whitelisted account
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

        # Required parameters
        self._transaction = transaction
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["transaction"] = self.transaction

        super(GetPhasingPollVotes, self).__init__(rt="getPhasingPollVotes", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, value):
        self._transaction = value

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
        super(GetPhasingPollVotes, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetPhasingPollVotes, self).getData(key)                           # calls 'BaseGet.getData()'
