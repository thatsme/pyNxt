# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPollResult(Parent):

    def __init__(self, poll=None, votingModel=None, holding=None, minBalance=None, minBalanceModel=None, requireBlock=None, requireLastBlock=None):
        """
            Get the result of a poll.

            GetPollResult take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Poll_Result

            REQUEST
            :param poll is the poll ID
            :param votingModel (optional, default null)
            :param holding (optional, default null)
            :param minBalance (optional, default 0)
            :param minBalanceModel (required if minBalance > 0, must match votingModel when votingModel > 0)
            :param requireBlock is the block ID of a block that must be present in the blockchain during execution (optional)
            :param requireLastBlock is the block ID of a block that must be last in the blockchain during execution (optional)

            Note: The votingModel, holding, minBalance and minBalanceModel parameters are optional and default to the original
            values specified when the poll was created (refer to Create Poll). The original values can only be overridden while
            the votes are still stored in the database, until 1441 blocks after the poll is completed. If votingModel is specified,
            holding, minBalance and minBalanceModel or the defaults specified above apply, otherwise they are ignored.

            RESPONSE
            :return poll : (S) is the poll ID
            :return votingModel : (N) is the votingModel used to calculate results (refer to Note above)
            :return minBalanceModel : (N) is the minBalanceModel used to calculate results (refer to Note above)
            :return minBalance : (S) is the minBalance used to calculate results (refer to Note above)
            :return holding : (S) is the asset or currency ID if the voting model uses an asset or currency balance to determine weight, if applicable (refer to Note above)
            :return decimals : (N) is the number decimal places used by the asset or currency, if applicable
            :return finished : (B) is true if the poll is complete, false otherwise
            :return options : (A) is the array of options (answers) of the poll
            :return results : (A) is an array of result objects with the following fields for each result:
            > weight : (S) is the sum of the weight of each account that voted for the corresponding option (answer); an account's weight is 1 if the voting model is 0, otherwise it is the NQT, asset QNT or currency QNT balance of the account if the voting model is 1, 2 or 3 respectively; however, the weight is 0 if minBalance is not met
            > result : (S) is the sum over each account that voted for the corresponding option (answer) of: the product of the account's weight and the rangeValue selected when the vote was cast.
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
        self.votingModel = votingModel
        self.holding = holding
        self.minBalance = minBalance
        self.minBalanceModel = minBalanceModel

        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["poll"] = self.poll
        self.data["votingModel"] = self.votingModel
        self.data["holding"] = self.holding
        self.data["minBalance"] = self.minBalance
        self.data["minBalanceModel"] = self.minBalanceModel

        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetPollResult, self).__init__(rt = "getPollResult", data=self.data)

    def run(self):
        super(GetPollResult, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPollResult, self).getData(key)               # calls 'BaseGet.getData()

