import requests
import json

class BasePost(object):

    def __init__(self, rt, data):

        self.account = "NXT-XWQY-C2MJ-JPL8-F4BW2"
        self.url = "http://localhost:6876/nxt"
        self.headers = {"Accept": "application/json"}
        self.dataDict = []
        self.response = None
        self.requestType = rt
        # self.data = {"requestType": self.requestType, "account": self.account}
        self.data = data
        # print(self.data)
        self._mergeRequestType()

    def _mergeRequestType(self):
        if self.requestType:
            if not self.data["requestType"]:
                self.data["requestType"] = self.requestType

    def run(self):
        self.response = requests.post(self.url, data=self.data, headers=self.headers)
        self.dataDict = json.loads(self.response.text)

    def getData(self, key=None):
        if key:
            return self.dataDict[key]
        else:
            return self.dataDict

    def getRequestType(self):
        if self.requestType:
            return self.requestType
        else:
            if self.data["requestType"]:
                return self.data["requestType"]
            else:
                return None

    def auth(self, authObject):
        pass