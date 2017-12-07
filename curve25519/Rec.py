# -*- coding: utf-8 -*-
class Rec(object):

    def __init__(self, ecBlockId=None, ecBlockHeight=None):

        self.rec = {}

        if ecBlockId:
            self.rec["ecBlockId"] = ecBlockId
        if ecBlockHeight:
            self.rec["ecBlockHeight"] = ecBlockHeight

        self._buildDict()

    def _buildDict(self):

        for x in [x for x in self.rec.keys() if self.rec[x] == None]:
            self.rec.pop(x)

    def getParam(self):
        return self.rec