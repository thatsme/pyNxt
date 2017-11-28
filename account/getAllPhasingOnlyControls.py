# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAllPhasingOnlyControl(Parent):

    def __init__(self, account=None ):
        """
            Retrieve all accounts subject to phasing control with their respective restrictions.

            GetAllPhasingOnlyControl take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_All_Phasing_Only_Control

            REQUEST
            firstIndex : is a zero-based index to the first block ID to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block ID to retrieve (N) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            phasingOnlyControls :is an array (A) with phasing only controls objects (Refer to Get Phasing Only Control for details)
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

        super(GetAllPhasingOnlyControl, self).__init__(rt = "getAllPhasingOnlyControl", data=self.data)

    def run(self):
        super(GetAllPhasingOnlyControl, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAllPhasingOnlyControl, self).getData(key)       # calls 'BaseGet.getData()'
