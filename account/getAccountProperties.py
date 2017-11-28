# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountProperties(Parent):


    def __init__(self, recipient=None, setter=None, property=None, firstIndex=None, lastIndex=None, requireBlock=None, requireLastBlock=None):
        """
            Get the Account properties for a specific account or setter

            GetAccountProperties take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Properties

            REQUEST
            recipient : is the account ID to which the property is attached to (S)
            setter : is the account ID who set the property (S) (optional if recipient provided)
            property : is the property key (S) (O)
            firstIndex : is a zero-based index to the first block to retrieve (N) (O)
            lastIndex : is a zero-based index to the last block to retrieve (N) (O)
            requireBlock : is the block ID of a block that must be present in the blockchain during execution (O)
            requireLastBlock : is the block ID of a block that must be last in the blockchain during execution (O)

            RESPONSE
            setterRS: is the Reed-Solomon address of the setter account (S) (only if setter is defined in the request)
            recipientRS: is the Reed-Solomon address of the recipient account (S) (only if recipient is defined in the request)
            recipient: is the account number of the recipient account (S) (only if recipient is defined in the request)
            requestProcessingTime : is the API request processing time (in millisec) (N)
            setter: is the account number of the setter account (S) (only if setter is defined in the request)
            properties: is an array (A) of properties including the fields:
            > setterRS: (S) is the Reed-Solomon address of the setter account (only if setter is omitted in the request)
            > recipientRS: (S) is the Reed-Solomon address of the recipient account (only if recipient is omitted in the request)
            > recipient: (S) is the account number of the recipient account (only if recipient is omitted in the request)
            > property: (S) property name
            > setter: (S) is the account number of the setter account (only if setter is omitted in the request)
            > value: (S) property value

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

        """

        self.recipient = recipient
        self.setter = setter
        self.property = property
        self.firstIndex = firstIndex
        self.lastIndex = lastIndex
        self.requireBlock = requireBlock
        self.requireLastBlock = requireLastBlock

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["recipient"] = self.recipient
        if self.setter:
            self.data["setter"] = self.setter
        if self.property:
            self.data["property"] = self.property
        if self.firstIndex:
            self.data["firstIndex"] = self.firstIndex
        if self.lastIndex:
            self.data["lastIndex"] = self.lastIndex
        if self.requireBlock:
            self.data["requireBlock"] = self.requireBlock
        if self.requireLastBlock:
            self.data["requireLastBlock"] = self.requireLastBlock

        super(GetAccountProperties, self).__init__(rt = "getAccountProperties", data=self.data)

    def run(self):
        super(GetAccountProperties, self).run()                               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountProperties, self).getData(key)                 # calls 'BaseGet.getData()'


