# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetNextBlockGenerators(Parent):

    def __init__(self, limit=1 ):
        """
            The GetNextBlockGenerators API will return the next block generators ordered by the hit time.
            The list of active forgers is initialized using the block generators with at least 2 blocks generated
            within the previous 10,000 blocks. Accounts without a public key will not be included.
            The list is updated as new blocks are processed. This means the results will not be 100% correct since
            previously active generators may no longer be running and new generators won't be known until they generate a block.
            This API will be replaced when transparent forging is activated.

            GetNextBlockGenerators take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Next_Block_Generators

            REQUEST
            :param limit : (N) The number of forgers to return and defaults to 1.

            RESPONSE
            :return activeCount - The number of active generators
            :return height - The last block height
            :return lastBlock - The last block identifier
            :return timestamp - The last block timestamp
            :return generator : (A) The next block generators
            :return > account - The account identifier
            :return > accountRS - The account RS identifier
            :return > deadline - The difference between the generation time and the last block timestamp
            :return > effectiveBalanceNXT - The account effective balance
            :return > hitTime - The generation time for the account
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

        self._limit = limit

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["limit"] = limit

        super(GetNextBlockGenerators, self).__init__(rt = "getNextBlockGenerators", data=self.data)

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value

    def run(self):
        super(GetNextBlockGenerators, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetNextBlockGenerators, self).getData(key)               # calls 'BaseGet.getData()'