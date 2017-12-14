# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAllPrunableMessages(Parent):

    def __init__(self, timestamp=None, ri=None, rb=None ):
        """
            Get all available prunable messages in reverse block timestamp order.

            GetAllPrunableMessages take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_All_Prunable_Messages

            REQUEST
            :param timestamp is the earliest message (in seconds since the genesis block) to retrieve (optional)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return prunableMessages : is an array (A) of prunable messages (refer to Get Prunable Message)
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

        self.timestamp = timestamp
        self.ri = ri
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["timestamp"] = self.timestamp

        super(GetAllPrunableMessages, self).__init__(rt = "getAllPrunableMessages", data=self.data, ri=self.ri, rb=self.rb)

    def run(self):
        super(GetAllPrunableMessages, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAllPrunableMessages, self).getData(key)             # calls 'BaseGet.getData()'