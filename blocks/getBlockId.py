# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBlockId(Parent):
    def __init__(self, height=None, rb=None ):
        """
            Get a block ID given a block height.

            GetBlockId take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Block_Id

            REQUEST
            :param height : is the block height (N) (optional if block provided)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return block : is the block ID (S)
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
        self._height = height
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["height"] = self.height

        super(GetBlockId, self).__init__(rt="getBlockId", data=self.data, rb=self.rb)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetBlockId, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBlockId, self).getData(key)                           # calls 'BaseGet.getData()'
