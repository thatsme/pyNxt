# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAlias(Parent):
    def __init__(self, alias = None, aliasName=None, rb=None ):
        """
            Get information about a given alias

            GetAlias take a default 1/2 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Alias

            REQUEST
            :param alias : is the ID of the accounts that owns the aliases (S)
            :param aliasName : is the earliest creation time (in seconds since the genesis block) of the aliases (S) (O)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return timestamp : is the time (in seconds since the genesis block) when the alias was created or last transferred (N)
            :return aliasName : is the name of the alias (S)
            :return accounts : is the number of the accounts that owns the alias (S)
            :return accountRS : is the Reed-Solomon address of the accounts that owns the alias (S)
            :return aliasURI : is what the alias points to, in URI format (S)
            :return alias : is the alias ID (S)
            :return priceNQT : is the asking price (in NQT) of the alias if it is for sale (S)
            :return buyer : is the accounts number of the buyer if the alias is for sale and a buyer is specified (S)
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
        self._alias = alias
        self._aliasName = aliasName
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        self.data["alias"] = self.alias
        self.data["aliasName"] = self.aliasName

        super(GetAlias, self).__init__(rt="getAlias", data=self.data, rb=self.rb)

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value

    @property
    def aliasName(self):
        return self._aliasName

    @aliasName.setter
    def aliasName(self, value):
        self._aliasName = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(GetAlias, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAlias, self).getData(key)                           # calls 'BaseGet.getData()'
