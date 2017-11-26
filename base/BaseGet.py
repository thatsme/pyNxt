import requests
import json

class BaseGet(object):

    def __init__(self, rt, data, phasing = None, message=None):

        # self.account = "NXT-XWQY-C2MJ-JPL8-F4BW2"
        self.url = "http://localhost:6876/nxt"
        self.headers = {"Accept": "application/json"}
        self.dataDict = []
        self.response = None
        self.requestType = rt
        #self.data = {"requestType": self.requestType, "account": self.account}

        self.data = data
        self.phasing = phasing
        self.message = message

        # print(self.data)
        self._mergeRequestType()
        self._mergePhasingParams()
        self._mergeMessageParams()

        self.errorCode = None
        self.errorDescription = None

    def param(self):
        pass

    def _mergeRequestType(self):
        if self.requestType:
            if "requestType" not in self.data:
                self.data["requestType"] = self.requestType

    def _mergePhasingParams(self):
        if self.phasing:
            self.data = {**self.data, **self.phasing}

    def _mergeMessageParams(self):
        if self.message:
            self.data = {**self.data, **self.message}

    def run(self):
        self.response = requests.get(self.url, params=self.data, headers=self.headers)
        self.dataDict = json.loads(self.response.text)
        if "errorCode" in self.dataDict:
            self.errorCode = self.dataDict["errorCode"]
            self.errorDescription = self.dataDict["errorDescription"]

    def getData(self, key=None):
        if key in self.dataDict:
            return self.dataDict[key]
        else:
            return self.dataDict

    def getKeysValues(self):
        for key, value in self.dataDict.items():
            print(key, value)

    def getKeys(self):
        for key in self.dataDict:
            print(key)

    def getRequestType(self):
        if self.requestType:
            return self.requestType
        else:
            if self.data["requestType"]:
                return self.data["requestType"]
            else:
                return None

    def getErrorCode(self):
        return self.errorCode

    def getErrorDescription(self):
        return self.errorDescription

    def auth(self, authObject):
        pass