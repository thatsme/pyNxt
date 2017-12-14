# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class GetBlockchainStatus(Parent):
    def __init__(self):
        """
            Get the blockchain status.

            GetBlockchainStatus take a default 1 parameter as explained in NXT API Documentation

            API is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Get_Blockchain_Status

            REQUEST
            none

            RESPONSE
            :return currentMinRollbackHeight : is the current minimum rollback height (N)
            :return numberOfBlocks : is the number of blocks in the blockchain (height + 1) (N)
            :return isTestnet : is true if the node is connected to testnet, false otherwise (B)
            :return includeExpiredPrunable : is the value of the nxt.includeExpiredPrunable property (B)
            :return version : is the application version (S)
            :return maxRollback : is the value of the nxt.maxRollback property (N)
            :return lastBlock : is the last block ID on the blockchain (S)
            :return application : is application name, typically NRS (S)
            :return isScanning : is true if the blockchain is being scanned by the application, false otherwise (B)
            :return isDownloading : is true if a download is in progress, false otherwise; true when a batch of more than
                            10 blocks at once has been downloaded from a peer, reset to false when an attempt
                            to download more blocks from a peer does not result in any new blocks (B)

            :return cumulativeDifficulty : is the cumulative difficulty (S)
            :return lastBlockchainFeederHeight : is the height of the last blockchain of greatest cumulative difficulty obtained from a peer (N)
            :return maxPrunableLifetime : is the maximum prunable lifetime (in seconds) (N)
            :return time : is the current timestamp (in seconds since the genesis block) (N)
            :return lastBlockchainFeeder : is the address or announced address of the peer providing the last blockchain of greatest cumulative difficulty (S)
            :return blockchainState : Current state of this node's blockchain (UP_TO_DATE or DOWNLOADING) (S)
            :return requestProcessingTime : is the API request processing time (in millisec) (N)

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

        super(GetBlockchainStatus, self).__init__(rt="getBlockchainStatus", data=self.data)

    def run(self):
        super(GetBlockchainStatus, self).run()                                         # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetBlockchainStatus, self).getData(key)                           # calls 'BaseGet.getData()'
