import requests
import json

class BaseGet(object):

    def __init__(self, rt):

        self.account = "NXT-XWQY-C2MJ-JPL8-F4BW2"
        self.url = "http://localhost:6876/nxt"
        self.headers = {"Accept": "application/json"}
        self.dataDict = []
        self.response = None
        self.requestType = rt
        self.data = {"requestType": self.requestType, "account": self.account}


    def param(self):
        pass

    def run(self):
        self.response = requests.get(self.url, params=self.data, headers=self.headers)
        self.dataDict = json.loads(self.response.text)

    def getData(self, key=None):
        if key:
            return self.dataDict[key]
        else:
            return self.dataDict

    def getRequestType(self):
        return self.requestType

    def auth(self, authObject):
        pass