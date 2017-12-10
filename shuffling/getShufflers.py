# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetShufflers(Parent):

    def __init__(self, account=None, shufflingFullHash=None, secretPhrase=None, adminPassword=None, includeParticipantState=False):
        """
            Retrieves info about active shufflers on the current node.

            GetShufflers take a default 1 parameter as explained in NXT API Documentation
            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Shufflers

            REQUEST
            :param account is account ID (O)
            :param shufflingFullHash is shuffling full hash (O)
            :param secretPhrase is secret phrase of the account doing the shuffling (required if adminPassword is not provided)
            :param adminPassword is the admin password (required if secretPhrase is not provided)
            :param includeParticipantState to include each shuffling participant's state (O)

            RESPONSE
            :return shufflers : (A) is an array containing all currently running shuffling processes on the node.
            > account : (S) is account ID
            > accountRS : (S) is the account Reed Solomon address
            > recipient : (S) is the recipient account ID to where the funds will be sent once the shuffling is completed
            > recipientRS : (S) is the recipient account Reed Solomon address to where the funds will be sent once the shuffling is completed
            > shuffling : (S) is the shuffling ID
            > shufflingFullHash : (S) is the shuffling full hash
            > participantState : (N) is the state for the participant (For more info, see shufflingParticipantStates array in Get Constants)
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

        self.account = account
        self.shufflingFullHash = shufflingFullHash
        self.secretPhrase = secretPhrase
        self.adminPassword = adminPassword
        self.includeParticipantState = includeParticipantState

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["account"] = self.account
        self.data["shufflingFullHash"] = self.shufflingFullHash
        self.data["includeParticipantState"] = self.includeParticipantState

        if self.secretPhrase:
            self.data["secretPhrase"] = self.secretPhrase
        if self.adminPassword:
            self.data["adminPassword"] = self.adminPassword

        super(GetShufflers, self).__init__(rt = "getShufflers", data=self.data)

    def run(self):
        super(GetShufflers, self).run()                             # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetShufflers, self).getData(key)               # calls 'BaseGet.getData()