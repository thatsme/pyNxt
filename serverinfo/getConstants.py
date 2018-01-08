# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetConstants(Parent):
    def __init__(self):
        """
            Get all defined constants.

            GetConstants take a default no parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Approve_Transaction

            REQUEST

            RESPONSE
            :return maxBlockPayloadLength (N) is the maximum block payload length (in bytes)
            :return maxArbitraryMessageLength (N) is the maximum length (in bytes) of an arbitrary message
            :return maxPrunableMessageLength (N) is the maximum length (in bytes) of a prunable message
            :return maxTaggedDataDataLength (N) is the maximum length (in bytes) of tagged data
            :return maxPhasingDuration (N) is the maximum allowed phasing duration in block height
            :return epochBeginning (N) is the time in milliseconds when genesis block was created
            :return genesisAccountId (S) is the genesis account number
            :return genesisBlockId (S) is the genesis block ID
            :return transactionTypes (A) is an array of defined transaction types and subtypes (refer to the example below)
            :return transactionSubTypes (A) is an array of defined transaction subtypes and subtypes (refer to the example below)
            :return peerStates (A) is an array of defined peer states (refer to the example below)
            :return currencyTypes (A) is an array of defined currency types (refer to the example below)
            :return disabledAPIs (A) is an array of configured disabled apis (refer to the example below)
            :return apiTags (A) is an array of defined api tags (refer to the example below)
            :return disabledAPITags (A) is an array of configured disabled api tags (refer to the example below)
            :return votingModels (A) is an array of defined voting models (refer to the example below)
            :return holdingTypes (A) is an array of defined holding types (refer to the example below)
            :return minBalanceModels (A) is an array of defined minimum balance models (refer to the example below)
            :return shufflingStages (A) is an array of defined shuffling stages (refer to the example below)
            :return shufflingParticipantStates (A) is an array of defined shuffling participant states (refer to the example below)
            :return hashAlgorithms (A) is an array of defined hash algorithms (refer to the example below)
            :return mintingHashAlgorithms (A) is an array of defined minting hash algorithms (refer to the example below)
            :return phasingHashAlgorithms (A) is an array of defined phasing hash algorithms (refer to the example below)
            :return requestTypes (A) is an array of decined request types (refer to the example below)

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


        # Initialize dictionary
        self.data = {}

        super(GetConstants, self).__init__(rt="getConstants", data=self.data)


    def run(self):
        super(GetConstants, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(GetConstants, self).getData(key)  # calls 'BasePost.getData()'

