# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetChannelTaggedData(Parent):

    def __init__(self, channel=None, account=None, includeData=False, ri=None, rb=None ):
        """
            Get all available tagged data in reverse chronological order.

            GetChannelTaggedData take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Channel_Tagged_Data

            REQUEST
            :param channel : is the channel string (S)
            :param account : is the account ID (S) (O)
            :param includeData : is true to include data (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return data : (A) is an array of tagged data objects (refer to Get Tagged Data with hash omitted for details)
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
        self._channel = channel
        self._account = account
        self._includeData = includeData
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["channel"] = self.channel
        self.data["account"] = self.account
        self.data["includeData"] = self.includeData

        super(GetChannelTaggedData, self).__init__(rt = "getChannelTaggedData", data=self.data, rb=self.rb)

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def includeData(self):
        return self._includeData

    @includeData.setter
    def includeData(self, value):
        self._includeData = value

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
        super(GetChannelTaggedData, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetChannelTaggedData, self).getData(key)    # calls 'BaseGet.getData()'