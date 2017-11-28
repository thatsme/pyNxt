# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountLedger(Parent):

    def __init__(self, account=None, event=None, eventType=None, holdingType=None, holding=None, includeTransactions=False, includeHoldingInfo=False, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):
        """
            Get multiple account ledger entries.

            GetAccountLedger take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Ledger

            REQUEST
            account : is the account ID (O)
            firstIndex : is a zero-based index to the first block to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block to retrieve (N) (O)
            event : is the event ID (S) (O)
            eventType : is a string representing the event type (S) (O)
            holdingType : is a string representing the holding type (S) (O)
            holding : is the holding ID (S) (O)
            includeTransactions : is true to retrieve transaction details, otherwise only transaction IDs are retrieved (B) (O)
            includeHoldingInfo : is true to retrieve asset or currency info (B) (O) with each ledger entry. The default is false.
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (S) (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (S) (O)

            RESPONSE
            entries : is an array (A) of ledger objects including the fields:
            > change (S) is the change in the balance for the holding identified by 'holdingType'
            > eventType (S) is the event type causing the account change
            > ledgerId (S) is the ledger entry ID
            > holding (S) is the item identifier for an asset or currency balance
            > isTransactionEvent (B) is true if the event is associated with a transaction and false if it is associated with a block.
            > balance (S) is the balance for the holding identified by 'holdingType'
            > holdingType (S) is the item being changed (account balance, asset balance or currency balance)
            > accountRS (S) is the Reed-Solomon address of the account
            > block (S) is the block ID that created the ledger entry
            > event (S) is the block or transaction associated with the event
            > account (S) is the account number
            > height (N) is the the block height associated with the event
            > timestamp (N) is the the block timestamp associated with the event

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

        self.account = account
        self.event = event
        self.eventType = eventType
        self.holding = holding
        self.holdingType = holdingType

        self.includeTransactions = includeTransactions
        self.includeHoldingInfo = includeHoldingInfo

        self.firstIndex = firstIndex

        self.lastIndex = lastIndex

        self.requireBlock = requireBlock

        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["account"] = self.account
        if self.event:
            self.data["event"] = self.event
        if self.eventType:
            self.data["eventType"] = self.eventType
        if self.holding:
            self.data["holding"] = self.holding
        if self.holdingType:
            self.data["holdingType"] = self.holdingType
        if self.includeTransactions:
            self.data["includeTransactions"] = self.includeTransactions
        if self.includeHoldingInfo:
            self.data["includeHoldingInfo"] = self.includeHoldingInfo
        if firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountLedger, self).__init__(rt = "getAccountLedger", data=self.data)

    def run(self):
        super(GetAccountLedger, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountLedger, self).getData(key)    # calls 'BaseGet.getData()'ß