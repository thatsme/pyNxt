# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class BroadcastTransaction(Parent):
    def __init__(self, transactionBytes = None, transactionJSON=None, prunableAttachmentJSON= None,  phasing = None, message=None ):
        """
            BroadcastTransaction take a default 5 parameter as explained in NXT API Documentation

            Class is working with POST method only, and create a transaction, for more info about transactions please refer to

            https://nxtwiki.org/wiki/The_Nxt_API#Broadcast_Transaction

            REQUEST
            :param transactionBytes : is the bytecode of a signed transaction (optional)
            :param transactionJSON : is the transaction object (optional if transactionBytes provided)
            :param prunableAttachmentJSON : is the attachment object embedded in transactionJSON containing a prunable message
                            (required if transactionJSON not provided because transactionBytes never includes prunable data)

            RESPONSE (Create transaction response)
            :return requestProcessingTime (N) is the API request processing time (in millisec)
            :return fullHash (S) is the full hash of the signed transaction
            :return transaction (S) is the transaction ID

            Legenda
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
        self.transactionBytes = transactionBytes
        self.transactionJSON = transactionJSON
        self.prunableAttachmentJSON = prunableAttachmentJSON

        self.phasing = phasing
        self.message = message

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        if self.transactionBytes:
            self.data["transactionBytes"] = self.transactionBytes
        if self.transactionJSON:
            self.data["transactionJSON"] = self.transactionJSON
        if self.prunableAttachmentJSON:
            self.data["prunableAttachmentJSON"] = self.prunableAttachmentJSON


        super(BroadcastTransaction, self).__init__(rt="broadcastTransaction", data=self.data, phasing=self.phasing, message=self.message)

    def run(self):
        super(BroadcastTransaction, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        return super(BroadcastTransaction, self).getData(key)  # calls 'BasePost.getData()'
