# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetDataTagsLike(Parent):

    def __init__(self, tagPrefix=None, ri=None, rb=None ):
        """
            Get the distinct tags of all available tagged data, with the number of uses of each tag,
            in order of number of uses, then alphabetical order.

            GetDataTagsLike take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Data_Tags_Like

            REQUEST
            :param tagPrefix :  is the prefix to search for (2 character minimum) among all data tags (S)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return tags : (A) is an array of tag objects including the fields:
            > tag (S) is a tag word
            > count (N) is the number of uses of tag among all tagged data
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

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
        self._tagPrefix = tagPrefix
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        super(GetDataTagsLike, self).__init__(rt = "getDataTagsLike", data=self.data, rb=self.rb)

    @property
    def tagPrefix(self):
        return self._tagPrefix

    @tagPrefix.setter
    def tagPrefix(self, value):
        self._tagPrefix = value

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
        super(GetDataTagsLike, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetDataTagsLike, self).getData(key)    # calls 'BaseGet.getData()'