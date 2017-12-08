# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class IssueCurrency(Parent):
    def __init__(self, name=None, code=None, description=None, type=0, initialSupply=0, reserveSupply=0, maxSupply=0, issuanceHeight=None, minReservePerUnitNQT=0, minDifficulty=0, maxDifficulty=0, ruleset=0, algorithm=2, decimals=0, publicKey = None, secretPhrase=None, feeNQT = None, deadline = 0, referencedTransactionFullHash = None, broadcast=True, phasing = None, message=None ):
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
                (O) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        # Required parameters
        self.name = name
        self.code = code
        self.description = description
        self.type = type
        self.initialSupply = initialSupply
        self.reserveSupply = reserveSupply
        self.maxSupply = maxSupply
        self.issuanceHeight = issuanceHeight
        self.minReservePerUnitNQT = minReservePerUnitNQT
        self.minDifficulty = minDifficulty
        self.maxDifficulty = maxDifficulty
        self.ruleset = ruleset
        self.algorithm = algorithm
        self.decimals = decimals

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

        super(IssueCurrency, self).__init__(rt="issueCurrency", data=self.data)

    def run(self):
        super(IssueCurrency, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(IssueCurrency, self).getData(key)  # calls 'BasePost.getData()'
