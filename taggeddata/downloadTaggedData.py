# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class DownloadTaggedData(Parent):

    def __init__(self,transaction=None, retrieve=None,  rb=None ):
        """
            Download tagged data as a file if it is still available.

            DownloadTaggedData take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Download_Tagged_Data

            REQUEST
            :param transaction : is the transaction ID of the tagged data (S)
            :param retrieve : is true to (B) retrieve pruned data from other nodes if not available (optional)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            The downloaded data file named nxt, unless there is an error in the request.

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

        self._transaction = transaction
        self._retrieve = retrieve
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["transaction"] = self.transaction
        self.data["retrieve"] = self.retrieve

        super(DownloadTaggedData, self).__init__(rt = "downloadTaggedData", data=self.data, rb=self.rb)

    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, value):
        self._transaction = value

    @property
    def retrieve(self):
        return self._retrieve

    @retrieve.setter
    def retrieve(self, value):
        self._retrieve = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        super(DownloadTaggedData, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(DownloadTaggedData, self).getData(key)    # calls 'BaseGet.getData()'