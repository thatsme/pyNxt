# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class RsConvert(Parent):

    def __init__(self, account=None ):
        """
            Get both the Reed-Solomon account address and the account number given an account ID.

            RsConvert take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Currencies_By_Issuer

            REQUEST
            account : is an account ID (either RS address or number)

            RESPONSE
            accountRS : is the Reed-Solomon address of the account (S)
            account : is the account number (S)
            requestProcessingTime : is the API request processing time (N) (in millisec)

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

        self.account = account

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = account

        super(RsConvert, self).__init__(rt = "rsConvert", data=self.data)

    def run(self):
        super(RsConvert, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(RsConvert, self).getData(key)    # calls 'BaseGet.getData()'