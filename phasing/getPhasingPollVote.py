# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPhasingPollVote(Parent):
    def __init__(self, transaction=None, account=None, rb=None ):
        """
            Get a cast phasing poll vote given a phased transaction ID and an account ID of a voter, if it is still available.

            GetPhasingPollVote take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Phasing_Poll_Vote

            REQUEST
            :param transaction : is the phased transaction ID
            :param account is the account ID of a voter in the poll
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return voter : (S) is the account ID of the voter in the poll
            :return voterRS : (S) is the Reed-Solomon address of the voter
            :return transaction : (S) is the phased transaction ID
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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

        # Required parameters
        self._transaction = transaction
        self._account = account
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["transaction"] = self.transaction
        self.data["account"] = self.account

        super(GetPhasingPollVote, self).__init__(rt="getPhasingPollVote", data=self.data, rb=self.rb)

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, value):
        self._transaction = value

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
        super(GetPhasingPollVote, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetPhasingPollVote, self).getData(key)                           # calls 'BaseGet.getData()'
