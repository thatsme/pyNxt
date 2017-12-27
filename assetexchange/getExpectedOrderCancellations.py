# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetExpectedOrderCancellations(Parent):
    def __init__(self, rb=None ):
        """
            Get all expected order cancellations in the order in which they are expected to be executed.

            GetExpectedOrderCancellations take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Expected_Orcer_Cancellations

            REQUEST
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return orderCancellations (A) is an array of order cancellation objects with the following fields for each transfer:
            > accounts (S) is the cancelling accounts number
            > accountRS (S) is the Reed-Solomon address of the accounts
            > order (S) is the ID of the order to be cancelled
            > height (N) is the block height of the order cancellation transaction
            > phased (B) is true if the order cancellation transaction is phased
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)

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
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        super(GetExpectedOrderCancellations, self).__init__(rt="getExpectedOrderCancellations", data=self.data, rb=self.rb)

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetExpectedOrderCancellations, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetExpectedOrderCancellations, self).getData(key)                           # calls 'BaseGet.getData()'
