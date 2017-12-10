# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPoll(Parent):

    def __init__(self, poll=None, requireBlock=None, requireLastBlock=None):
        """
            Get the details of a poll.

            GetPoll take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Poll

            REQUEST

            :param poll is the poll ID
            :param requireBlock is the block ID of a block that must be present in the blockchain during execution (optional)
            :param requireLastBlock is the block ID of a block that must be last in the blockchain during execution (optional)

            RESPONSE
            :return poll : (S) is the poll ID
            :return account : (S) is the account number of the poll creator
            :return accountRS : (S) is the Reed-Solomon address of the account
            :return name : (S) is the name of the poll
            :return description : (S) is the description of the poll, or the question to be answered
            :return finishHeight : (N) is the block height when the poll is completed
            :return finished : (B) is true if the poll is completed, false otherwise
            :return votingModel : (N) is 0 for One Vote Per Account, 1 for Vote By NXT Balance, 2 for Vote By Asset Balance and 3 for Vote By Currency Balance
            :return minNumberOfOptions : (N) is the minimum number of options (answers) that must be voted for
            :return maxNumberOfOptions : (N) is the maximum number of options (answers) that can be voted for
            :return minBalance : (S) is the minimum balance (in NQT or QNT) required for voting
            :return minBalanceModel : (N) is 1 for NXT balance, 2 for an asset balance, 3 for a currency balance when minBalance > 0
            :return holding : is the asset or currency ID when minBalanceModel > 1
            :return options : (A) is the array of options (answers)
            :return minRangeValue : (N) is the minimum integer value for an option (answer)
            :return maxRangeValue : (N) is the maximum integer value for an option (answer)
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
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["poll"] = self.poll

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetPoll, self).__init__(rt = "getPoll", data=self.data)

    def run(self):
        super(GetPoll, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPoll, self).getData(key)               # calls 'BaseGet.getData()

