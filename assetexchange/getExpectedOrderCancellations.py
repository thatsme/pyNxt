# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetExpectedOrderCancellations(Parent):
    def __init__(self, asset=None, account=None, firstIndex=None, lastIndex=None, timestamp=0, includeAssetInfo=False, requireBlock=None, requireLastBlock=None ):
        """
            Get all expected order cancellations in the order in which they are expected to be executed.

            GetExpectedOrderCancellations take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Expected_Orcer_Cancellations

            REQUEST
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            orderCancellations (A) is an array of order cancellation objects with the following fields for each transfer:
            > account (S) is the cancelling account number
            > accountRS (S) is the Reed-Solomon address of the account
            > order (S) is the ID of the order to be cancelled
            > height (N) is the block height of the order cancellation transaction
            > phased (B) is true if the order cancellation transaction is phased
            lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            requestProcessingTime : is the API request processing time (in millisec) (N)

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
                (WP) Wrapper specific parameter


        """

        # Required parameters
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock

        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetExpectedOrderCancellations, self).__init__(rt="getExpectedOrderCancellations", data=self.data)

    def run(self):
        super(GetExpectedOrderCancellations, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetExpectedOrderCancellations, self).getData(key)                           # calls 'BaseGet.getData()'
