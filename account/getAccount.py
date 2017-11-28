# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccount(Parent):


    def __init__(self, account=None, includeLessors=False, includeAssets=False, includeCurrencies=False, includeEffectiveBalance=False, requireBlock=None, requireLastBlock=None):
        """
            GetAccount take a default 1 parameter as explained in NXT API Documentation ( is deadLine requested or not ? )

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account

            REQUEST
            account : is the id of account (S) (R)
            includeLessors : is true to include lessors, lessorsRS and lessorsInfo (B) (O)
            includeAssets : is true to include assetBalances and unconfirmedAssetBalances (B) (O)
            includeCurrencies : is true to include accountCurrencies (B) (O)
            includeEffectiveBalance : is true to include effectiveBalanceNXT and guaranteedBalanceNQT (B) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE

            unconfirmedBalanceNQT : is balanceNQT less unconfirmed outgoing transactions, the balance displayed in the client (S)
            effectiveBalanceNXT : is the balance (in NXT) of the account available for forging: the unleased guaranteedBalance of this
                                    account plus the leased guaranteedBalance of all lessors to this account (N)
            lessorsInfo : is an array of lessor objects including the fields  (A) :
            > currentHeightTo (S)
            > nextHeightFrom (S)
            > effectiveBalanceNXT (S)
            > nextLesseeRS (S)
            > currentLesseeRS (S)
            > currentHeightFrom (S)
            > nextHeightTo (S)
            lessors : is an array of lessor account IDs (A)
            currentLessee : is the account number of the lessee, if applicable (S)
            currentLeasingHeightTo : is the block height when the lease completes, if applicable (N)
            forgedBalanceNQT : is the balance (in NQT) that the account has forged (S)
            balanceNQT : is the minimally confirmed basic balance (in NQT) of the account (S)
            publicKey : is the public key of the account (S)
            requestProcessingTime : is the API request processing time (in millisec) (N)
            assetBalances : is an array of asset objects (A) including the fields :
            > balanceQNT (S)
            > asset ID (S)
            guaranteedBalanceNQT : is the balance (in NQT) of the account with at least 1440 confirmations (S)
            unconfirmedAssetBalances : is an array of asset objects (A) including the fields :
            > unconfirmedBalanceQNT (S)
            > asset ID (S)
            currentLesseeRS : is the Reed-Solomon address of the lessee account (S)
            accountRS : is the Reed-Solomon address of the account (S)
            lessorsRS : is an array (A) of Reed-Solomon lessor account addresses
            accountCurrencies : is an array of currency objects  (A) (refer to Get Account Currencies for details)
            name : is the name associated with the account, if applicable (S)
            description : is the description of the account, if applicable (S)
            account : is the account number (S)
            currentLeasingHeightFrom : is the block height when the lease starts, if applicable (N)
            lastBlock : is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock) (S)

            Legenda :
                ° the parameter are interchangable on
                * if you use the secretPhrase , the transaction is immediately broadcasted to network
                ** if you use the publicKey, you create an unsigned Transaction, and you need to sign and broardcast
                *** for buying
                (R) Required
                (O) Optional
                (N) Number
                (S) String
                (B) Boolean
                (A) Array
                >   Array Element
        """




        # is the block ID of a block that must be present in the blockchain during execution (optional)

        self.account = account
        self.includeLessors = includeLessors
        self.includeAssets = includeAssets
        self.includeCurrencies = includeCurrencies
        self.includeEffectiveBalance = includeEffectiveBalance
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.includeLessors:
            self.data["includeLessors"] = self.includeLessors
        if self.includeAssets:
            self.data["includeAssets"] = self.includeAssets
        if self.includeCurrencies:
            self.data["includeCurrencies"] = self.includeCurrencies
        if self.includeEffectiveBalance:
            self.data["includeEffectiveBalace"] = self.includeEffectiveBalance
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccount, self).__init__(rt = "getAccount", data=self.data)

    def run(self):
        super(GetAccount, self).run()                               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccount, self).getData(key)                 # calls 'BaseGet.getData()'


