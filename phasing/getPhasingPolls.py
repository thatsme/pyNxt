# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPhasingPolls(Parent):
    def __init__(self, transactions=None, countVotes=False, requireBlock=None, requireLastBlock=None ):
        """
            Get phasing poll details given multiple phased transaction IDs.

            GetPhasingPolls take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Phasing_Polls

            REQUEST
            :param transactions : is one of multiple currency IDs (WP) (S)
            :param countVotes is true to (B) compute the poll result while the votes are still available (O)
            :param requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            :param requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

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
                (O) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        # Required parameters
        self.transactions = [None]*3
        for a in transactions[:3]:
            self.transactions.append(a)

        self.countVotes = countVotes
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["transactions"] = self.transactions
        self.data["countVotes"] = self.countVotes

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetPhasingPolls, self).__init__(rt="getPhasingPolls", data=self.data)

    def run(self):
        super(GetPhasingPolls, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPhasingPolls, self).getData(key)                           # calls 'BaseGet.getData()'
