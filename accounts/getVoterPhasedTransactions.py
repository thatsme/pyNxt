# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetVoterPhasedTransactions(Parent):

    def __init__(self, account=None, ri=None, rb=None ):
        """
            Get pending phased transactions which include a whitelist in reverse chronological creation order.
            These transactions can be considered transaction approval requests.

            GetVoterPhasedTransactions take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Voter_Phased_Transactions

            REQUEST
            :param accounts :  is a whitelisted accounts ID included in the phased transactions (R)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            Refer to Get Transaction for details.


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
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["accounts"] = account

        super(GetVoterPhasedTransactions, self).__init__(rt = "getVoterPhasedTransactions", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

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

    def run(self):
        super(GetVoterPhasedTransactions, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetVoterPhasedTransactions, self).getData(key)       # calls 'BaseGet.getData()'