# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class IssueCurrency(Parent):
    def __init__(self, name=None, code=None, description=None, type=0, initialSupply=0, reserveSupply=0, maxSupply=0, issuanceHeight=None, minReservePerUnitNQT=0, minDifficulty=0, maxDifficulty=0, ruleset=0, algorithm=2, decimals=0, publicKey = None, secretPhrase=None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=True, phasing = None, message=None,rec=None ):
        """
            Issue a new currency or re-issue an existing currency with different properties. POST only.

            IssueCurrency take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Issue_Currency

            REQUEST
            :param name : is the currency name, 3 to 10 characters and longer than the currency code
            :param code : is the uppercase currency code with the following fee structure: three letters 25000 NXT, four letters 1000 NXT, five letters 40 NXT, re-issue 40 NXT
            :param description : is the currency description
            :param type : is the currency type bitmask, from least to most significant bit: exchangeable, controllable, reservable, claimable, mintable, non-shuffleable
            :param initialSupply : is the initial currency supply (in QNT) (must match maxSupply unless mintable or claimable, must be zero for claimable)
            :param reserveSupply : is the reserve currency supply (in QNT) (must match maxSupply)
            :param maxSupply : is the maximum currency supply (in QNT)
            :param issuanceHeight : is the blockchain height at which a reservable currency is issued if the reserve minimum is met
            :param minReservePerUnitNQT : is the minimum currency reserve (in NQT per QNT of reserveSupply) for issuance of a reservable currency
            :param minDifficulty : is the minimum difficulty (minimum 1) for a mintable currency
            :param maxDifficulty : is the maximum difficulty (maximum 255 and greater than minDifficulty) for a mintable currency
            :param ruleset : is for future use, always set to zero
            :param algorithm : is an algorithm code for a mintable currency: 2 for SHA256, 3 for SHA3, 5 for Scrypt, 25 for Keccak25
            :param decimals : is the number of decimal places used by the currency (optional, default zero)

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

            Notes: Reservable requires exchangeable and/or claimable, as does controllable; but mintable requires exchangeable.
            Claimable requires reservable, non-mintable and zero initialSupply.

            Response: Refer to Create Transaction Response. The transaction ID is also the currency ID.

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
        self._code = code
        self._description = description
        self._type = type
        self._initialSupply = initialSupply
        self._reserveSupply = reserveSupply
        self._maxSupply = maxSupply
        self._issuanceHeight = issuanceHeight
        self._minReservePerUnitNQT = minReservePerUnitNQT
        self._minDifficulty = minDifficulty
        self._maxDifficulty = maxDifficulty
        self._ruleset = ruleset
        self._algorithm = algorithm
        self._decimals = decimals

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
        self.data["code"] = self.code
        self.data["description"] = self.description
        self.data["type"] = self.type

        self.data["initialSupply"] = self.initialSupply
        self.data["reserveSupply"] = self.reserveSupply
        self.data["maxSupply"] = self.maxSupply

        self.data["issuanceHeight"] = self.issuanceHeight
        self.data["minReservePerUnitNQT"] = self.minReservePerUnitNQT

        self.data["minDifficult"] = self.minDifficulty
        self.data["maxDifficult"] = self.maxDifficulty

        self.data["ruleset"] = self.ruleset
        self.data["algorithm"] = self.algorithm
        self.data["decimals"] = self.decimals

        if self.publicKey:
            self.data["publicKey"] = self.publicKey

        if self.secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase

        if self.referencedTransactionFullHash:
            self.data["referencedTransactionFullHash"] = self.referencedTransactionFullHash

        self.data["broadcast"] = self.broadcast
        self.data["feeNQT"] = self.feeNQT
        self.data["deadline"] = self.deadline

        super(IssueCurrency, self).__init__(rt="issueCurrency", data=self.data, rec=self.rec)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def initialSupply(self):
        return self._initialSupply

    @initialSupply.setter
    def initialSupply(self, value):
        self._initialSupply = value

    @property
    def reserveSupply(self):
        return self._reserveSupply

    @reserveSupply.setter
    def reserveSupply(self, value):
        self._reserveSupply = value

    @property
    def maxSupply(self):
        return self._maxSupply

    @maxSupply.setter
    def maxSupply(self, value):
        self._maxSupply = value

    @property
    def issuanceHeight(self):
        return self._issuanceHeight

    @issuanceHeight.setter
    def issuanceHeight(self, value):
        self._issuanceHeight = value

    @property
    def minReservePerUnitNQT(self):
        return self._minReservePerUnitNQT

    @minReservePerUnitNQT.setter
    def minReservePerUnitNQT(self, value):
        self._minReservePerUnitNQT = value

    @property
    def minDifficulty(self):
        return self._minDifficulty

    @minDifficulty.setter
    def minDifficulty(self, value):
        self._minDifficulty = value

    @property
    def maxDifficulty(self):
        return self._maxDifficulty

    @maxDifficulty.setter
    def maxDifficulty(self, value):
        self._maxDifficulty = value

    @property
    def ruleset(self):
        return self._ruleset

    @ruleset.setter
    def ruleset(self, value):
        self._ruleset = value

    @property
    def algorithm(self):
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value):
        self._algorithm = value

    @property
    def decimals(self):
        return self._decimals

    @decimals.setter
    def decimals(self, value):
        self._decimals = value

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
        super(IssueCurrency, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(IssueCurrency, self).getData(key)  # calls 'BasePost.getData()'
