# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAccountProperties(Parent):


    def __init__(self, recipient=None, setter=None, pproperty=None, ri=None, rb=None):
        """
            Get the Account properties for a specific accounts or setter

            GetAccountProperties take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Account_Properties

            REQUEST
            :param recipient : is the accounts ID to which the property is attached to (S)
            :param setter : is the accounts ID who set the property (S) (optional if recipient provided)
            :param pproperty : is the property key (S) (O)
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return setterRS: is the Reed-Solomon address of the setter accounts (S) (only if setter is defined in the request)
            :return recipientRS: is the Reed-Solomon address of the recipient accounts (S) (only if recipient is defined in the request)
            :return recipient: is the accounts number of the recipient accounts (S) (only if recipient is defined in the request)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)
            :return setter: is the accounts number of the setter accounts (S) (only if setter is defined in the request)
            :return properties: is an array (A) of properties including the fields:
            > setterRS: (S) is the Reed-Solomon address of the setter accounts (only if setter is omitted in the request)
            > recipientRS: (S) is the Reed-Solomon address of the recipient accounts (only if recipient is omitted in the request)
            > recipient: (S) is the accounts number of the recipient accounts (only if recipient is omitted in the request)
            > property: (S) property name
            > setter: (S) is the accounts number of the setter accounts (only if setter is omitted in the request)
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
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        self._recipient = recipient
        self._setter = setter
        self._pproperty = pproperty
        self._ri = ri
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["recipient"] = self.recipient
        if self.setter:
            self.data["setter"] = self.setter
        if self.pproperty:
            self.data["property"] = self.pproperty

        super(GetAccountProperties, self).__init__(rt = "getAccountProperties", data=self.data, ri=self.ri, rb=self.rb)

    @property
    def recipient(self):
        return self._recipient

    @recipient.setter
    def recipient(self, value):
        self._recipient = value

    @property
    def setter(self):
        return self._setter

    @setter.setter
    def setter(self, value):
        self._setter = value

    @property
    def pproperty(self):
        return self._pproperty

    @pproperty.setter
    def pproperty(self, value):
        self._pproperty = value

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
        super(GetAccountProperties, self).run()                               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAccountProperties, self).getData(key)                 # calls 'BaseGet.getData()'


