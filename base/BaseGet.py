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

    def run(self):
        data = {"requestType": self.requestType, "account": self.account}
        self.response = requests.get(self.url, params=data, headers=self.headers)
        self.dataDict = json.loads(self.response.text)
        print(self.response)
        print(self.response.text)

        print(self.dataDict)

    def getData(self):
        return self.dataDict