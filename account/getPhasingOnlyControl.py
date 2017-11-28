# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetPhasingOnlyControl(Parent):

    def __init__(self, account=None ):
        """
            Retrieve phasing control with their respective restrictions for a specific account.

            GetPhasingOnlyControl take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Phasing_Only_Control

            REQUEST
            account : is an account ID
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            account : is the account number (S)
            accountRS : is the Reed-Solomon address of the account (S)
            quorum : is the minimum number of votes needed to approve the transaction (S)
            whitelist : is an array (A) with the whitelisted accounts including the fields:
            > whitelisted (S) is the account number
            > whitelistedRS (S) is the Reed-Solomon address of the account
            maxFees : is the maximum fees the account can spend per block (S)
            minDuration : is the minimum duration of the phasing period (N)
            maxDuration : is the maximum duration of the phasing period (N)
            votingModel : is an integer code for the method of approval (N)
            minBalance : is the minimum balance (in NQT or QNT) required for voting (S)
            minBalanceModel : is the minimum balance model (N)
            holding : is the asset or currency ID (only included if holding != 0) (S)
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

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = account

        super(GetPhasingOnlyControl, self).__init__(rt = "getPhasingOnlyControl", data=self.data)

    def run(self):
        super(GetPhasingOnlyControl, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetPhasingOnlyControl, self).getData(key)    # calls 'BaseGet.getData()'