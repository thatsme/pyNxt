# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBalance(Parent):

    def __init__(self, account=None, includeEffectiveBalance=False, height= None, rb=None ):
        """
            Get asset information given multiple creation accounts IDs in reverse block height of creation order.

            GetBalance take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Balance

            REQUEST
            :param accounts : is array (A) of accounts ID's (S) / Multiaccount parameters (3)
            :param includeEffectiveBalance : is true to include effectiveBalanceNXT and guaranteedBalanceNQT (B) (O)
            :param height : is the height to retrieve accounts balance for, if still available (N) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return unconfirmedBalanceNQT : is balanceNQT less unconfirmed outgoing transactions, the balance displayed in the client (S)
            :return guaranteedBalanceNQT : is the balance (in NQT) of the accounts with at least 1440 confirmations (S)
            :return effectiveBalanceNXT : is the balance (in NXT) of the accounts available for forging: the unleased guaranteedBalance
                                of this accounts plus the leased guaranteedBalance of all lessors to this accounts (N)
            :return forgedBalanceNQT : is the balance (in NQT) that the accounts has forged (S)
            :return balanceNQT : is the minimally confirmed basic balance (in NQT) of the accounts (S)
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
        self.includeEffectiveBalance = includeEffectiveBalance
        self.height = height
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = self.account
        if self.includeEffectiveBalance:
            self.data["includeEffectiveBalance"] = self.includeEffectiveBalance
        if self.height:
            self.data["height"] = self.height

        super(GetBalance, self).__init__(rt = "getBalance", data=self.data, rb=self.rb)

    def run(self):
        super(GetBalance, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetBalance, self).getData(key)    # calls 'BaseGet.getData()'