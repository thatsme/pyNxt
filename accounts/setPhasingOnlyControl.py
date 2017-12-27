# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent


class SetPhasingOnlyControl(Parent):
    def __init__(self, controlVotingModel=0, controlQuorum=0, controlWhiteListed=None, controlMinBalance=None, controlMinBalanceModel=None, controlHolding=None, controlMaxFee=None, controlMinDuration=None, controlMaxDuration=None, publicKey=None, secretPhrase=None, feeNQT=None, deadline=0, referencedTransactionFullHash=None, broadcast=True, phasing=None, message=None, rec=None):
        """
            Sets (or removes) phasing control for a specific accounts.
            SetPhasingOnlyControl take a default 5 parameter as explained in NXT API Documentation

            API is working with POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request

            https://nxtwiki.org/wiki/The_Nxt_API#Set_Phasing_Only_Control

            REQUEST
            :param controlVotingModel : is the voting model or -1 to remove phasing control (R)
            :param controlQuorum : is the expected quorum (N) (O)
            :param controlWhitelisted : is the whitelisted accounts (R) (O) (multiple values)
            :param controlMinBalance : is the expected minimum balance (N) (O)
            :param controlMinBalanceModel : is the expected minimum balance model (O)
            :param controlHolding : is the holding ID (S) (O)
            :param controlMaxFee : is the maximum allowed accumulated total fees for not yet finished phased transactions (N) (O)
            :param controlMinDuration : is the minimum duration in block height (N) (O)
            :param controlMaxDuration : is the maximum phasing duration in block height (N) (O)
            :param recipientPublicKey is the public key of the lessee (recipient) accounts (optional, enhances security of a new accounts)
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

            RESPONSE
            signatureHash : is a SHA-256 hash of the transaction signature (S)
            unsignedTransactionBytes : are the unsigned transaction bytes (S)
            transactionJSON : is a transaction object (O)  (refer to Get Transaction for details)
            broadcasted : is true if the transaction was broadcast, false otherwise (B)
            requestProcessingTime : is the API request processing time (in millisec)  (N)
            transactionBytes :  are the signed transaction bytes (S)
            fullHash : is the full hash of the signed transaction (S)
            transaction : is the ID of the newly created transaction (S)
            requestProcessingTime : is the API request processing time (N) (in millisec)

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
        self._controlVotingModel = controlVotingModel
        self._controlQuorum = controlQuorum
        self._controlMinBalance = controlMinBalance
        self._controlMinBalanceModel = controlMinBalanceModel
        self._controlHolding = controlHolding
        self._controlMaxFee = controlMaxFee
        self._controlMinDuration = controlMinDuration
        self._controlMaxDuration = controlMaxDuration
        self._controlWhiteListed = controlWhiteListed
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

        self.data["controlVotingModel"] = self.controlVotingModel

        if self.controlQuorum:
            self.data["controlQuorum"] = self.controlQuorum

        if self.controlMinBalance:
            self.data["controlMinBalance"] = self.controlMinBalance

        if controlMinBalanceModel:
            self.data["controlMinBalanceModel"] = self.controlMinBalanceModel

        if controlHolding:
            self.data["controlHolding"] = self.controlHolding

        if controlMaxFee:
            self.data["controlMaxFee"] = self.controlMaxFee

        if controlMinDuration:
            self.data["controlMinDuration"] = self.controlMinDuration

        if controlMaxDuration:
            self.data["controlMaxDuration"] = self.controlMaxDuration

        if publicKey:
            self.data["publicKey"] = self.publicKey
        if secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        if referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline
        self.data["broadcast"] = self.broadcast

        super(SetPhasingOnlyControl, self).__init__(rt="setPhasingOnlyControl", data=self.data, phasing=self.phasing, message=self.message, rec=self.rec)

    @property
    def controlVotingModel(self):
        return self._controlVotingModel

    @controlVotingModel.setter
    def controlVotingModel(self, value):
        self._controlVotingModel = value

    @property
    def controlQuorum(self):
        return self._controlQuorum

    @controlQuorum.setter
    def controlQuorum(self, value):
        self._controlQuorum = value

    @property
    def controlWhiteListed(self):
        return self._controlWhiteListed

    @controlWhiteListed.setter
    def controlWhiteListed(self, value):
        self._taccounts = [None]*3
        for a in value[:3]:
            self.taccounts.append(a)
        self._controlWhiteListed = self._taccounts

    @property
    def controlMinBalance(self):
        return self._controlMinBalance

    @controlMinBalance.setter
    def controlMinBalance(self, value):
        self._controlMinBalance = value

    @property
    def controlMinBalanceModel(self):
        return self._controlMinBalanceModel

    @controlMinBalanceModel.setter
    def controlMinBalanceModel(self, value):
        self._controlMinBalanceModel = value

    @property
    def controlHolding(self):
        return self._controlHolding

    @controlHolding.setter
    def controlHolding(self, value):
        self._controlHolding = value

    @property
    def controlMaxFee(self):
        return self._controlMaxFee

    @controlMaxFee.setter
    def controlMaxFee(self, value):
        self._controlMaxFee = value

    @property
    def controlMinDuration(self):
        return self._controlMinDuration

    @controlMinDuration.setter
    def controlMinDuration(self, value):
        self._controlMinDuration = value

    @property
    def controlMaxDuration(self):
        return self._controlMaxDuration

    @controlMaxDuration.setter
    def controlMaxDuration(self, value):
        self._controlMaxDuration = value

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
        super(SetPhasingOnlyControl, self).run()                         # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(SetPhasingOnlyControl, self).getData(key)           # calls 'BasePost.getData()'

