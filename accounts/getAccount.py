# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccount(Parent):


    def __init__(self, account=None, includeLessors=False, includeAssets=False, includeCurrencies=False, includeEffectiveBalance=False, rb=None):
        """
            GetAccount take a default 1 parameter as explained in NXT API Documentation ( is deadLine requested or not ? )

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account

            REQUEST
            :param accounts : is the id of accounts (S) (R)
            :param includeLessors : is true to include lessors, lessorsRS and lessorsInfo (B) (O)
            :param includeAssets : is true to include assetBalances and unconfirmedAssetBalances (B) (O)
            :param includeCurrencies : is true to include accountCurrencies (B) (O)
            :param includeEffectiveBalance : is true to include effectiveBalanceNXT and guaranteedBalanceNQT (B) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE

            :return unconfirmedBalanceNQT : is balanceNQT less unconfirmed outgoing transactions, the balance displayed in the client (S)
            :return effectiveBalanceNXT : is the balance (in NXT) of the accounts available for forging: the unleased guaranteedBalance of this
                                    accounts plus the leased guaranteedBalance of all lessors to this accounts (N)
            :return lessorsInfo : is an array of lessor objects including the fields  (A) :
            > currentHeightTo (S)
            > nextHeightFrom (S)
            > effectiveBalanceNXT (S)
            > nextLesseeRS (S)
            > currentLesseeRS (S)
            > currentHeightFrom (S)
            > nextHeightTo (S)
            :return lessors : is an array of lessor accounts IDs (A)
            :return currentLessee : is the accounts number of the lessee, if applicable (S)
            :return currentLeasingHeightTo : is the block height when the lease completes, if applicable (N)
            :return forgedBalanceNQT : is the balance (in NQT) that the accounts has forged (S)
            :return balanceNQT : is the minimally confirmed basic balance (in NQT) of the accounts (S)
            :return publicKey : is the public key of the accounts (S)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)
            :return assetBalances : is an array of asset objects (A) including the fields :
            > balanceQNT (S)
            > asset ID (S)
            :return guaranteedBalanceNQT : is the balance (in NQT) of the accounts with at least 1440 confirmations (S)
            :return unconfirmedAssetBalances : is an array of asset objects (A) including the fields :
            > unconfirmedBalanceQNT (S)
            > asset ID (S)
            :return currentLesseeRS : is the Reed-Solomon address of the lessee accounts (S)
            :return accountRS : is the Reed-Solomon address of the accounts (S)
            :return lessorsRS : is an array (A) of Reed-Solomon lessor accounts addresses
            :return accountCurrencies : is an array of currency objects  (A) (refer to Get Account Currencies for details)
            :return name : is the name associated with the accounts, if applicable (S)
            :return description : is the description of the accounts, if applicable (S)
            :return accounts : is the accounts number (S)
            :return currentLeasingHeightFrom : is the block height when the lease starts, if applicable (N)
            :return lastBlock : is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock) (S)


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

        # is the block ID of a block that must be present in the blockchain during execution (optional)

        self._account = account
        self._includeLessors = includeLessors
        self._includeAssets = includeAssets
        self._includeCurrencies = includeCurrencies
        self._includeEffectiveBalance = includeEffectiveBalance
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.includeLessors:
            self.data["includeLessors"] = self.includeLessors
        if self.includeAssets:
            self.data["includeAssets"] = self.includeAssets
        if self.includeCurrencies:
            self.data["includeCurrencies"] = self.includeCurrencies
        if self.includeEffectiveBalance:
            self.data["includeEffectiveBalace"] = self.includeEffectiveBalance

        super(GetAccount, self).__init__(rt = "getAccount", data=self.data, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def includeLessors(self):
        return self._includeLessors

    @includeLessors.setter
    def includeLessors(self, value):
        self._includeLessors = value

    @property
    def includeAssets(self):
        return self._includeAssets

    @includeAssets.setter
    def includeAssets(self, value):
        self._includeAssets = value

    @property
    def includeCurrencies(self):
        return self._includeCurrencies

    @includeCurrencies.setter
    def includeCurrencies(self, value):
        self._includeCurrencies = value

    @property
    def includeEffectiveBalance(self):
        return self._includeEffectiveBalance

    @includeEffectiveBalance.setter
    def includeEffectiveBalance(self, value):
        self._includeEffectiveBalance = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value


    def run(self):
        """
        Run rest request
        """
        super(GetAccount, self).run()                               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccount, self).getData(key)                 # calls 'BaseGet.getData()'

    def phelp(self):
        print(GetAccount.__doc__)

