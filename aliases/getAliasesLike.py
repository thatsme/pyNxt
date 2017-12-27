# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAliasesLike(Parent):
    def __init__(self, aliasPrefix = None, ri=None, rb=None ):
        """
            Get all aliases starting with a given prefix in alias name order.

            API is working with GET method

            GetAliases take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Aliases_Like

            REQUEST
            :param aliasPrefix : is the prefix (at least 2 characters long) of the aliasName (S) (R)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return aliases : is an array (A) of alias objects (refer to Get Alias for details)
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
        self._aliasPrefix = aliasPrefix
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["aliasPrefix"] = self.aliasPrefix

        super(GetAliasesLike, self).__init__(rt="getAliasesLike", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def aliasPrefix(self):
        return self._aliasPrefix

    @aliasPrefix.setter
    def aliasPrefix(self, value):
        self._aliasPrefix = value

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
        super(GetAliasesLike, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAliasesLike, self).getData(key)                           # calls 'BaseGet.getData()'
