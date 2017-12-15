# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetTransactionBytes(Parent):

    def __init__(self, transaction=None, rb=None ):
        """
            Get a transaction object given a transaction ID.

            GetTransactionBytes take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Transaction_Bytes

            REQUEST
            :param transaction : is the transaction ID (S)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return confirmations : (N) is the number of transaction confirmations
            :return transactionBytes : (S) are the bytes contained in the transaction
            :return unsignedTransactionBytes : (S) are the unsigned bytes contained in the transaction
            :return prunableAttachmentJSON : (O) is the prunable attachment JSON object, if applicable, because transactionBytes never includes prunable data
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

        self.transaction = transaction
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["transaction"]  = self.transaction
   
        super(GetTransactionBytes, self).__init__(rt = "getTransactionBytes", data=self.data, rb=self.rb)

    def run(self):
        super(GetTransactionBytes, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetTransactionBytes, self).getData(key)    # calls 'BaseGet.getData()'