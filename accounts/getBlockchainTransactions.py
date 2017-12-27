# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent
from base.Validators import accepts
from base.Validators import returns
from base.Ri import Ri
from base.Rb import Rb
import json

class GetBlockchainTransactions(Parent):

    ## @accepts(self, str, int, str, str, int, bool, bool, bool, bool, bool, bool, Ri, Rb)
    def __init__(self, account=None, timestamp=0, type=None, subtype=None, numberOfConfirmations=0, withMessage=False, phasedOnly=False, nonPhasedOnly=False, includeExpiredPrunable=False, includePhasingResult=False, executeOnly=False, ri=None, rb=None ):
        """
            Get the transactions associated with an accounts in reverse block timestamp order.

            GetBlockchainTransactions take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Blockchain_Transactions

            REQUEST
            :param account : is accounts ID (S)
            :param timestamp : is the earliest block (in seconds since the genesis block) to retrieve (N) (O)
            :param type : is the type of transactions to retrieve (S) (O)
            :param subtype : is the subtype of transactions to retrieve (S) (O)
            :param numberOfConfirmations : is the required number of confirmations per transaction (B) (O)
            :param withMessage : is true to retrieve only only transactions having a message attachment, either non-encrypted or decryptable by the accounts (B) (O)
            :param phasedOnly : is true to retrieve only phased transactions (B) (O) (optional unless nonPhasedOnly provided)
            :param nonPhasedOnly : is true to retrieve only nonphased transactions (B) (O) (optional unless phasedOnly provided)
            :param includeExpiredPrunable : is true' to retrieve pruned data if available (B) (O)
            :param includePhasingResult : is true to retrieve execution status of each phased transaction (B) (O)
            :param executedOnly : is true to exclude phased transactions that are not yet executed (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return transactions : is an array (A) of transactions (refer to Get Transaction for details)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (N) (in millisec)

            TRANSACTIONS
            the istance can be accessed as iterator

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
        ###
        self._account = account
        self._timestamp = timestamp
        self._type = type
        self._subtype = subtype
        self._numberOfConfirmations = numberOfConfirmations
        self._withMessage = withMessage
        self._phasedOnly = phasedOnly
        self._nonPhasedOnly = nonPhasedOnly
        self._includeExpiredPrunable = includeExpiredPrunable
        self._includePhasingResult = includePhasingResult
        self._executeOnly = executeOnly
        self._ri = ri
        self._rb = rb

        ## For iterator
        self.index = 0
        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        self.data["timestamp"] = self.timestamp
        self.data["numberOfConfirmations"] = self.numberOfConfirmations
        if self.type:
            self.data["type"] = self.type
        if self.subtype:
            self.data["subtype"] = self.subtype

        if self.withMessage:
            self.data["withMessage"] = self.withMessage
        if self.phasedOnly:
            self.data["phasedOnly"] = self.phasedOnly
        if self.nonPhasedOnly:
            self.data["nonPhasedOnly"] = self.nonPhasedOnly
        if self.includeExpiredPrunable:
            self.data["includeExpiredPrunable"] = self.includeExpiredPrunable
        if self.includePhasingResult:
            self.data["includePhasingResult"] = self.includePhasingResult
        if self.executeOnly:
            self.data["executeOnly"] = self.executeOnly

        super(GetBlockchainTransactions, self).__init__(rt = "getBlockchainTransactions", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def subtype(self):
        return self._subtype

    @subtype.setter
    def subtype(self, value):
        self._subtype = value

    @property
    def numberOfConfirmations(self):
        return self._numberOfConfirmations

    @numberOfConfirmations.setter
    def numberOfConfirmations(self, value):
        self._numberOfConfirmations = value

    @property
    def withMessage(self):
        return self._withMessage

    @withMessage.setter
    def withMessage(self, value):
        self._withMessage = value

    @property
    def phasedOnly(self):
        return self._phasedOnly

    @phasedOnly.setter
    def phasedOnly(self, value):
        self._phasedOnly = value

    @property
    def nonPhasedOnly(self):
        return self._nonPhasedOnly

    @nonPhasedOnly.setter
    def nonPhasedOnly(self, value):
        self._nonPhasedOnly = value

    @property
    def includeExpiredPrunable(self):
        return self._includeExpiredPrunable

    @includeExpiredPrunable.setter
    def includeExpiredPrunable(self, value):
        self._includeExpiredPrunable = value

    @property
    def includePhasingResult(self):
        return self._includePhasingResult

    @includePhasingResult.setter
    def includePhasingResult(self, value):
        self._includePhasingResult = value

    @property
    def executeOnly(self):
        return self._executeOnly

    @executeOnly.setter
    def executeOnly(self, value):
        self._executeOnly = value

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

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.dataDict["transactions"][self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def __reversed__(self):
        return reversed(self.dataDict["transactions"])

    def run(self):
        super(GetBlockchainTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetBlockchainTransactions, self).getData(key)    # calls 'BaseGet.getData()'

