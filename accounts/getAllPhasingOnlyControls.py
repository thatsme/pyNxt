# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetAllPhasingOnlyControl(Parent):

    def __init__(self, ri=None, rb=None ):
        """
            Retrieve all accounts subject to phasing control with their respective restrictions.

            GetAllPhasingOnlyControl take a default 1 parameter as explained in NXT API Documentation
            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_All_Phasing_Only_Control

            REQUEST
            :param ri : ri object ( check base/Ri.py) (WP)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return phasingOnlyControls :is an array (A) with phasing only controls objects (Refer to Get Phasing Only Control for details)
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

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary

        super(GetAllPhasingOnlyControl, self).__init__(rt = "getAllPhasingOnlyControl", data=self.data, ri=self.ri, rb=self.rb)

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
        super(GetAllPhasingOnlyControl, self).run()                     # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetAllPhasingOnlyControl, self).getData(key)       # calls 'BaseGet.getData()'
