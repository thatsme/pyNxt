# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetShufflingPartecipants(Parent):

    def __init__(self, shuffling=None, includeHoldingInfo=False, rb=None ):
        """
            Retrieves info about a shuffling.

            GetShufflingPartecipants take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Shuffling_Partecipants

            REQUEST
            :param shuffling : is the shuffling ID
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :param participants : (A) array of partecipants
            > shuffling : (S) is the shuffling ID
            > account : (S) is the account ID
            > accountRS : (S) is the account Reed Solomong address
            > state : (N) is the state for the participant (For more info, see shufflingParticipantStates array in Get Constants)
            > nextAccount : (S) is the account ID of the next account in turn
            > nextAccountRS : (S) is the account Reed Solomon address of the next account in turn
            :param requestProcessingTime : (N) is the API request processing time (in millisec)


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

        self.shuffling = shuffling
        self.rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["shuffling"] = self.shuffling

        super(GetShufflingPartecipants, self).__init__(rt = "getShufflingPartecipants", data=self.data, rb=self.rb)

    def run(self):
        super(GetShufflingPartecipants, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetShufflingPartecipants, self).getData(key)               # calls 'BaseGet.getData()