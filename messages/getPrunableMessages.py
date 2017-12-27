# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPrunableMessages(Parent):

    def __init__(self, account=None,otherAccount=None,  secretPhrase=None, timestamp=0, ri=None, rb=None ):
        """
            Get all still-available prunable messages given an accounts id,
            optionally limiting to only those with another accounts as recipient or sender, in reverse chronological order.

            GetPrunableMessages take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Prunable_Messages

            REQUEST
            :param accounts : is the accounts ID (S)
            :param otherAccount : is another accounts ID, either sender or recipient, to limit the response (S)
            :param secretPhrase : is the secret passphrase used to decrypt the encrypted part of the message (O)
            :param timestamp : is the earliest prunable message (in seconds since the genesis block) to retrieve (optional)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return prunableMessages : is an array (A) of prunable message objects (refer to Get Prunable Message for details)
            :return lastBlock : is the last block ID on the blockchain (S)(applies if requireBlock is provided but not requireLastBlock)
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
        self._otherAccount = otherAccount
        self._secretPhrase = secretPhrase
        self._timestamp = timestamp
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        if self.otherAccount:
            self.data["otherAccount"] = self.otherAccount

        self.data["secretPhrase"] = self.secretPhrase
        self.data["timestamp"] = self.timestamp

        super(GetPrunableMessages, self).__init__(rt = "getPrunableMessages", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def otherAccount(self):
        return self._otherAccount

    @otherAccount.setter
    def otherAccount(self, value):
        self._otherAccount = value

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

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
        super(GetPrunableMessages, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetPrunableMessages, self).getData(key)             # calls 'BaseGet.getData()'