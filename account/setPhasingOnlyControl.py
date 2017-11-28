# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent


class SetPhasingOnlyControl(Parent):
    def __init__(self, controlVotingModel=0, controlQuorum=0, controlWhiteListed=None, controlMinBalance=None, controlMinBalanceModel=None, controlHolding=None, controlMaxFee=None, controlMinDuration=None, controlMaxDuration=None, publicKey=None, secretPhrase=None, feeNQT=None, deadline=0, referencedTransactionFullHash=None, broadcast=True, phasing=None, message=None):
        """
            Sets (or removes) phasing control for a specific account.
            SetPhasingOnlyControl take a default 5 parameter as explained in NXT API Documentation

            Class is working with POST method only, and create a transaction, for more info about transactions please refer to
            https://nxtwiki.org/wiki/The_Nxt_API#Create_Transaction_Request

            https://nxtwiki.org/wiki/The_Nxt_API#Set_Phasing_Only_Control

            REQUEST
            controlVotingModel : is the voting model or -1 to remove phasing control (R)
            controlQuorum : is the expected quorum (N) (O)
            controlWhitelisted : is the whitelisted accounts (R) (O) (multiple values)
            controlMinBalance : is the expected minimum balance (N) (O)
            controlMinBalanceModel : is the expected minimum balance model (O)
            controlHolding : is the holding ID (S) (O)
            controlMaxFee : is the maximum allowed accumulated total fees for not yet finished phased transactions (N) (O)
            controlMinDuration : is the minimum duration in block height (N) (O)
            controlMaxDuration : is the maximum phasing duration in block height (N) (O)
            recipientPublicKey is the public key of the lessee (recipient) account (optional, enhances security of a new account)
            * publicKey : publicKey of sender account ( does not get in broadcast )
            ** secretPhrase : secret Phrase of sender account
            feeNQT : fee for sending transaction (R) if 0 minimum is set ( 100000000 NQT )
            deadLine : is the deadline (in minutes) for the transaction to be confirmed, 32767 minutes maximum ( if 0, 60 )
            referencedTransactionFullHash : creates a chained transaction, meaning that the current transaction cannot be confirmed
                                            unless the referenced transaction is also confirmed (O)
            broadcast : is set to false to prevent broadcasting the transaction to the network (B) (O)
            phasing : phasing object ( check base/Phasing.py )
            message : message object ( check base/message.py )

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
                (O) Object
                >   Array Element

        """

        # Required parameters
        self.controlVotingModel = controlVotingModel
        self.controlQuorum = controlQuorum
        self.controlMinBalance = controlMinBalance
        self.controlMinBalanceModel = controlMinBalanceModel
        self.controlHolding = controlHolding
        self.controlMaxFee = controlMaxFee
        self.controlMinDuration = controlMinDuration
        self.controlMaxDuration = controlMaxDuration

        self.cvl = [None] * 3
        for a in controlWhiteListed[:3]:
            self.cvl.append(a)

        self.publicKey = publicKey
        self.secretPhrase = secretPhrase
        self.referencedTransactionFullHash = referencedTransactionFullHash
        self.broadcast = broadcast

        if feeNQT == 0:
            self.feeNQT = 100000000
        else:
            self.feeNQT = feeNQT

        if deadline == 0:
            self.deadline = 60
        else:
            self.deadline = deadline

        self.phasing = phasing
        self.message = message

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

        super(SetPhasingOnlyControl, self).__init__(rt="setPhasingOnlyControl", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(SetPhasingOnlyControl, self).run()                         # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(SetPhasingOnlyControl, self).getData(key)           # calls 'BasePost.getData()'

