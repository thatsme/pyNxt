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

    def param(self):
        pass

    def run(self):
        self.response = requests.post(self.url, data=self.data, headers=self.headers)
        self.dataDict = \
            json.loads(self.response.text)

    def getData(self, key=None):
        if key:
            return self.dataDict[key]
        else:
            return self.dataDict

    def auth(self, authObject):
        pass