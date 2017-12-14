# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAssetsByIssuer(Parent):

    def __init__(self,account=None, includeCounts=False, ri=None, rb=None ):
        """
            Get asset information given multiple creation accounts IDs in reverse block height of creation order.

            GetAssetsByIssuer take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Assets_By_Issuer

            REQUEST
            :param accounts : is array (A) of accounts ID's (S) / Multiaccount parameters (3)
            :param includeCounts : is true if the fields beginning with numberOf... are to be included (B) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return assets : is an array (A) of asset objects (refer to Get Asset)
            :return lastBlock : is the last block ID on the blockchain (S) (applies if requireBlock is provided but not requireLastBlock)
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

        self.accounts = [None]*3
        for a in account[:3]:
            self.accounts.append(a)

        self.includeCounts = includeCounts
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        for a in self.accounts:
            self.data["accounts"] = a

        if self.includeCounts:
            self.data["includeCounts"] = self.includeCounts

        super(GetAssetsByIssuer, self).__init__(rt = "getAssetsByIssuer", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetAssetsByIssuer, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAssetsByIssuer, self).getData(key)    # calls 'BaseGet.getData()'