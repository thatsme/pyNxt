# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetGuaranteedBalance(Parent):

    def __init__(self, account=None, numberOfConfirmations=0, rb=None ):
        """
            Get the balance of an accounts that is confirmed at least a specified number of times.

            GetGuaranteedBalance take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Guaranteed_Balance

            REQUEST
            :param accounts : is accounts ID (S)
            :param numberOfConfirmations : is the minimum number of confirmations for a transaction to be included in the guaranteed balance (N) (O),
                                    if omitted or zero then minimally confirmed transactions are included)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return guaranteedBalanceNQT : is the balance (in NQT) of the accounts with at least numberOfConfirmations confirmations (S)
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


        self._account = account
        self._numberOfConfirmations = numberOfConfirmations
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = account

        if self.numberOfConfirmations:
            self.data["numberOfConfirmations"] = self.numberOfConfirmations

        super(GetGuaranteedBalance, self).__init__(rt = "getGuaranteedBalance", data=self.data, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def numberOfConfirmations(self):
        return self._numberOfConfirmations

    @numberOfConfirmations.setter
    def numberOfConfirmations(self, value):
        self._numberOfConfirmations = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetGuaranteedBalance, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetGuaranteedBalance, self).getData(key)               # calls 'BaseGet.getData()'