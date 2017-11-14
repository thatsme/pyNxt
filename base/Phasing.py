
class Phasing(object):

    def __init__(self, phased=None, phasingFinishHeight = None, phasingVotingModel = None, phasingQuorum = None, \
                    phasingMinBalance = None, phasingHolding=None, phasingMinBalanceModel=None, phasingWhitelisted=None, \
                    phasingLinkedFullHash=None, phasingHashedSecret=None, phasingHashedSecretAlgorithm=None)

        self.phasing = {}
        self.phasing["phased"] = phased
        self.phasing["phasingFinishHeight"] = phasingFinishHeight
        self.phasing["phasingVotingModel"] = phasingVotingModel
        self.phasing["phasingQuorum"] = phasingQuorum
        self.phasing["phasingMinBalance"] = phasingMinBalance
        self.phasing["phasingHolding"] = phasingHolding
        self.phasing["phasingMinBalanceModel"] = phasingMinBalanceModel
        if len(phasingWhitelisted) == 1 or not phasingWhitelisted:
            self.phasing["phasingWhitelisted"] = phasingWhitelisted                 # 3 elements in api
        else:
            pass
        if len(phasingLinkedFullHash) == 1 or not phasingLinkedFullHash:
            self.phasing["phasingLinkedFullHash"] = phasingLinkedFullHash           # 3 elements in api
        else:
            pass
        self.phasing["phasingHashedSecret"] = phasingHashedSecret
        self.phasing["phasingHashedSecretAlgorithm"] = phasingHashedSecretAlgorithm


        self._buildDict()

    def _buildDict(self):

        for x in [x for x in self.phasing.keys() if self.phasing[x] == None]:
            self.phasing.pop(x)

    def getParam(self):
        return self.phasing