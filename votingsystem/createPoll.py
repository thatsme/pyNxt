# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class CreatePoll(Parent):
    def __init__(self, name=None, description = None, finishHeight=None, votingModel=None, minNumberOfOptions=None, maxNumberOfOptions=None, minRangeValue=None, maxRangeValue=None, minBalance=None, minBalanceModel=None, holding=None, option00=None, option01=None, option02=None, publicKey = None, secretPhrase=None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=True, phasing = None, message=None, rec=None ):
        """
            Create a new poll. POST only.

            CreatePoll take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Create_Poll

            REQUEST
            :return name : is the name of the poll
            :return description : is the description of the poll, or the question to be answered
            :return finishHeight : is the block height when the poll is completed
            :return votingModel : is 0 for One Vote Per Account, 1 for Vote By NXT Balance, 2 for Vote By Asset Balance and 3 for Vote By Currency Balance
            :return minNumberOfOptions : is the minimum number of options (answers) that must be voted for
            :return maxNumberOfOptions : is the maximum number of options (answers) that can be voted for
            :return minRangeValue : is the minimum integer value for an option (answer) (>= 0)
            :return maxRangeValue : is the maximum integer value for an option (answer) (>= minRangeValue)
            :return minBalance : is the minimum balance (in NQT or QNT) required for voting (optional, default 0)
            :return minBalanceModel : is (required if minBalance > 0, must match votingModel when votingModel > 0)
            > 1 for NXT balance
            > 2 for an asset balance
            > 3 for a currency balance
            :return holding : is the asset or currency ID (required if minBalanceModel > 1)
            :return option00 : is the name of option (answer) 0
            :return option01 : is the name of option (answer) 1 (optional)
            :return option02 : is the name of option (answer) 2 (optional)
            :param publicKey *: publicKey of sender accounts ( does not get in broadcast )
            :param secretPhrase **: secret Phrase of sender accounts
            :param feeNQT : fee for sending transaction (R) if 0 minimum is set ( 100000000 NQT )
            :param deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            :param referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            :param broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            :param phasing : phasing object ( check base/Phasing.py ) (O) (WP)
            :param message : message object ( check base/message.py ) (O) (WP)
            :param rec : rec object ( check base/Rec.py) (WP)

            Notes: Up to 100 options (answers) can be specified, but there is an extra fee for each option beyond 20.
            Unlike the API, the NRS client treats a vote of 0 as a nonvote not contributing to the number answers (options) chosen.
            The NRS client uses checkboxes for selecting answers when minRangeValue = 0 and maxRangeValue = 1;
            otherwise sliding controls are used to select answers from the allowed range.

            Note: When a balance affects the poll result, the result depends only on the balance
            (including pending outgoing phased transfers) computed just prior to the finish height.

            RESPONSE
            :return signatureHash : is a SHA-256 hash of the transaction signature (S)
            :return unsignedTransactionBytes : are the unsigned transaction bytes (S)
            :return transactionJSON : is a transaction object (O)  (refer to Get Transaction for details)
            :return broadcasted : is true if the transaction was broadcast, false otherwise (B)
            :return requestProcessingTime : is the API request processing time (in millisec)  (N)
            :return transactionBytes :  are the signed transaction bytes (S)
            :return fullHash : is the full hash of the signed transaction (S)
            :return transaction : is the ID of the newly created transaction (S)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

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
        self._name = name
        self._description = description
        self._finishHeight = finishHeight
        self._votingModel = votingModel
        self._minNumberOfOptions = minNumberOfOptions
        self._maxNumberOfOptions = maxNumberOfOptions
        self._minRangeValue = minRangeValue
        self._maxRangeValue = maxRangeValue
        self._minBalance = minBalance
        self._minBalanceModel = minBalanceModel
        self._holding = holding
        self._options00 = option00
        self._options01 = option01
        self._options02 = option02

        self._publicKey = publicKey
        self._secretPhrase = secretPhrase
        self._referencedTransactionFullHash = referencedTransactionFullHash
        self._broadcast = broadcast
        self._feeNQT = feeNQT
        self._deadline = deadline

        self._phasing = phasing
        self._message = message
        self._rec = rec

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["name"] = self.name
        self.data["description"] = self.description
        self.data["finishHeight"] = self.finishHeight
        self.data["votingModel"] = self.votingModel
        self.data["minNumberOfOptions"] = self.minNumberOfOptions
        self.data["maxNumberOfOptions"] = self.maxNumberOfOptions
        self.data["minRangeValue"] = self.minRangeValue
        self.data["maxRangeValue"] = self.maxRangeValue
        self.data["minBalance"] = self.minBalance
        self.data["minBalanceModel"] = self.minBalanceModel
        self.data["holding"] = self.holding
        self.data["options00"] = self.options00
        self.data["options01"] = self.options01
        self.data["options02"] = self.options02

        self.data["publicKey"] = self.publicKey
        self.data["secretPhrase"] = self.secretPhrase
        self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash
        self.data["broadcast"] = self.broadcast
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline


        super(CreatePoll, self).__init__(rt="createPoll", data=self.data, phasing=self.phasing, message=self.message, rec=self.rec)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def finishHeight(self):
        return self._finishHeight

    @finishHeight.setter
    def finishHeight(self, value):
        self._finishHeight = value

    @property
    def votingModel(self):
        return self._votingModel

    @votingModel.setter
    def votingModel(self, value):
        self._votingModel = value

    @property
    def minNumberOfOptions(self):
        return self._minNumberOfOptions

    @minNumberOfOptions.setter
    def minNumberOfOptions(self, value):
        self._minNumberOfOptions = value

    @property
    def maxNumberOfOptions(self):
        return self._maxNumberOfOptions

    @maxNumberOfOptions.setter
    def maxNumberOfOptions(self, value):
        self._maxNumberOfOptions = value

    @property
    def minRangeValue(self):
        return self._minRangeValue

    @minRangeValue.setter
    def minRangeValue(self, value):
        self._minRangeValue = value

    @property
    def maxRangeValue(self):
        return self._maxRangeValue

    @maxRangeValue.setter
    def maxRangeValue(self, value):
        self._maxRangeValue = value

    @property
    def minBalance(self):
        return self._minBalance

    @minBalance.setter
    def minBalance(self, value):
        self._minBalance = value

    @property
    def minBalanceModel(self):
        return self._minBalanceModel

    @minBalanceModel.setter
    def minBalanceModel(self, value):
        self._minBalanceModel = value

    @property
    def holding(self):
        return self._holding

    @holding.setter
    def holding(self, value):
        self._holding = value

    @property
    def options00(self):
        return self._options00

    @options00.setter
    def options00(self, value):
        self._options00 = value

    @property
    def options01(self):
        return self._options01

    @options01.setter
    def options01(self, value):
        self._options01 = value

    @property
    def options02(self):
        return self._options02

    @options02.setter
    def options02(self, value):
        self._options02 = value

    @property
    def publicKey(self):
        return self._publicKey

    @publicKey.setter
    def publicKey(self, value):
        self._publicKey = value

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def referencedTransactionFullHash(self):
        return self._referencedTransactionFullHash

    @referencedTransactionFullHash.setter
    def referencedTransactionFullHash(self, value):
        self._referencedTransactionFullHash = value

    @property
    def broadcast(self):
        return self._broadcast

    @broadcast.setter
    def broadcast(self, value):
        self._broadcast = value

    @property
    def feeNQT(self):
        return self._feeNQT

    @feeNQT.setter
    def feeNQT(self, value):
        if value == 0:
            self._feeNQT = 100000000
        else:
            self._feeNQT = value

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        if value == 0:
            self._deadline = 60
        else:
            self._deadline = value

    @property
    def phasing(self):
        return self._phasing

    @phasing.setter
    def phasing(self, value):
        self._phasing = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def rec(self):
        return self._rec

    @rec.setter
    def rec(self, value):
        self._rec = value

    def run(self):
        super(CreatePoll, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(CreatePoll, self).getData(key)  # calls 'BasePost.getData()'

