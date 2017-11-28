# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountLedgerEntry(Parent):

    def __init__(self, ledgerId=None, includeTransaction=False, includeHoldingInfo=False):
        """
            Get multiple account ledger entries.

            GetAccountLedgerEntry take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Ledger

            REQUEST
            ledgerId : is the ledger ID
            includeTransactions : is true to retrieve transaction details, otherwise only transaction IDs are retrieved (B) (O)
            includeHoldingInfo : is true to retrieve asset or currency info (B) (O) with the ledger entry. The default is false.
            RESPONSE
            change : is the change in the balance for the holding identified by 'holdingType' (S)
            eventType : is the event type causing the account change (S)
            ledgerId : is the ledger entry ID (S)
            holding : is the item identifier for an asset or currency balance (S)
            isTransactionEvent : is true if the event is associated with a transaction and false if it is associated with a block. (B)
            balance : is the balance for the holding identified by 'holdingType' (S)
            holdingType : is the item being changed (account balance, asset balance or currency balance) (S)
            accountRS : is the Reed-Solomon address of the account (S)
            block : is the block ID that created the ledger entry (S)
            event : is the block or transaction associated with the event (S)
            account : is the account number (S)
            height : is the the block height associated with the event (N)
            timestamp : is the the block timestamp associated with the event (N)

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

        self.ledgerId = ledgerId
        self.includeTransaction = includeTransaction
        self.includeHoldingInfo = includeHoldingInfo

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["ledgerId"] = self.ledgerId
        if self.includeTransaction:
            self.data["includeTransaction"] = self.includeTransaction
        if self.includeHoldingInfo:
            self.data["includeHoldingInfo"] = self.includeHoldingInfo

        super(GetAccountLedgerEntry, self).__init__(rt="getAccountLedgerEntry", data=self.data)

    def run(self):
        super(GetAccountLedgerEntry, self).run()                        # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountLedgerEntry, self).getData(key)               # calls 'BaseGet.getData()'ß