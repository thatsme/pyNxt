# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetMyInfo(Parent):

    def __init__(self):
        """
            GetMyInfo get hostname and address of the requesting node.
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_My_Info

            REQUEST

            RESPONSE
            :return host : (S) is the node hostname
            :return address : (S) is the node address
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
                (O) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        # Initialize dictionary
        self.data = {}


        super(GetMyInfo, self).__init__(rt = "getMyInfo", data=self.data)

    def run(self):
        super(GetMyInfo, self).run()                                 # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetMyInfo, self).getData(key)                   # calls 'BaseGet.getData()'