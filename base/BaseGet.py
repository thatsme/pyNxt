import requests
import json

class BaseGet(object):

    def __init__(self):

        self.account = "NXT-XWQY-C2MJ-JPL8-F4BW2"
        self.url = "http://localhost:6876/nxt"
        self.headers = {"Accept": "application/json"}
        self.dataDict = []
        self.response = None
        self.requestType = None
        self.data = {"requestType": self.requestType, "account": self.account}


    def param(self):
        pass

    def run(self):
        self.response = requests.get(self.url, params=self.data, headers=self.headers)
        self.dataDict = json.loads(self.response.text)
        #print(self.response)
        #print(self.response.text)
        #print(self.dataDict)

    def getData(self):
        return self.dataDict

    def auth(self, autObject):
        pass