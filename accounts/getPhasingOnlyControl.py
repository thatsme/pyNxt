# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPhasingOnlyControl(Parent):

    def __init__(self, account=None, rb=None ):
        """
            Retrieve phasing control with their respective restrictions for a specific accounts.

            GetPhasingOnlyControl take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Phasing_Only_Control

            REQUEST
            :param accounts : is an accounts ID
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return accounts : is the accounts number (S)
            :return accountRS : is the Reed-Solomon address of the accounts (S)
            :return quorum : is the minimum number of votes needed to approve the transaction (S)
            :return whitelist : is an array (A) with the whitelisted accounts including the fields:
            > whitelisted (S) is the accounts number
            > whitelistedRS (S) is the Reed-Solomon address of the accounts
            :return maxFees : is the maximum fees the accounts can spend per block (S)
            :return minDuration : is the minimum duration of the phasing period (N)
            :return maxDuration : is the maximum duration of the phasing period (N)
            :return votingModel : is an integer code for the method of approval (N)
            :return minBalance : is the minimum balance (in NQT or QNT) required for voting (S)
            :return minBalanceModel : is the minimum balance model (N)
            :return holding : is the asset or currency ID (only included if holding != 0) (S)
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
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = account

        super(GetPhasingOnlyControl, self).__init__(rt = "getPhasingOnlyControl", data=self.data, rb=self.rb)


    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetPhasingOnlyControl, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetPhasingOnlyControl, self).getData(key)    # calls 'BaseGet.getData()'