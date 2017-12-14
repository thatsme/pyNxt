# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetIds(Parent):
    def __init__(self, ri=None, rb=None ):
        """
            Get the IDs of all assets in the exchange in reverse block height of creation order.

            GetAssetIds take a default 1/2 parameter as explained in NXT API Documentation

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Asset_Ids

            REQUEST
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return assets : is an array (A) of asset IDs
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
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        super(GetAssetIds, self).__init__(rt="getAssetIds", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetAssetIds, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAssetIds, self).getData(key)                           # calls 'BaseGet.getData()'
