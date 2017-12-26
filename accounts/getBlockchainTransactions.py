# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBlockchainTransactions(Parent):

    def __init__(self,account=None, timestamp=0, type=None, subtype=None, numberOfConfirmations=0, withMessage=False, phasedOnly=False, nonPhasedOnly=False, includeExpiredPrunable=False, includePhasingResult=False, executeOnly=False, ri=None, rb=None ):
        """
            Get the transactions associated with an accounts in reverse block timestamp order.

            GetBlockchainTransactions take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Blockchain_Transactions

            REQUEST
            :param accounts : is accounts ID (S)
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

        self.account = account
        self.timestamp = timestamp
        self.type = type
        self.subtype = subtype
        self.numberOfConfirmations = numberOfConfirmations
        self.withMessage = withMessage
        self.phasedOnly = phasedOnly
        self.nonPhasedOnly = nonPhasedOnly
        self.includeExpiredPrunable = includeExpiredPrunable
        self.includePhasingResult = includePhasingResult
        self.executeOnly = executeOnly
        self.ri = ri
        self.rb = rb

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

    def run(self):
        super(GetBlockchainTransactions, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetBlockchainTransactions, self).getData(key)    # calls 'BaseGet.getData()'