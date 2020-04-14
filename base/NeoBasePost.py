# -*- coding: utf-8 -*-
import requests
import json
import base64

class NeoBasePost(object):

    def __init__(self, nt):

        self.dataDict = []
        self.authDict = []
        self.response = None
        self.nodeType = nt
        self.DEBUG = False
        self.crd = None
        self.session = requests.Session()
        # self.data = {"requestType": self.requestType, "accounts": self.accounts}
        #self.data = None

        self.errorCode = None
        self.errorDescription = None

    def setCredential(self, crd):
        self.crd = crd

    def connect(self):
        try:
            self.response = self.session.get(self.crd.authurl, headers=self.crd.headers)
            if self.response.status_code == 503:
                self.response.raise_for_status()
        except requests.exceptions.HTTPError:
            print("oops something unexpected happened!")

        self.authDict = json.loads(self.response.text)

    def run(self, data):
        """

        :param data: Data for POST REST API
        :return:
        """
        try:
            self.response = self.session.post(self.crd.url, data=data, headers=self.crd.headers)
            if self.response.status_code == 503:
                self.response.raise_for_status()
        except requests.exceptions.HTTPError:
            print("oops something unexpected happened!")

        self.dataDict = json.loads(self.response.text)
        if self.DEBUG:
            print(self.dataDict)
            #print(self.dataDict["data"][0][0]["metadata"]["id"])

    def getData(self, key=None):
        if key in self.dataDict:
            return self.dataDict[key]
        else:
            if key is None:
                return self.dataDict
            else:
                return "No Key "+key

    def getId(self):
        if len(self.dataDict["data"]) != 0:
            return self.dataDict["data"][0][0]["metadata"]["id"]
        else:
            return None

    def getAuth(self, key=None):
        if key in self.authDict:
            return self.authDict[key]
        else:
            if key is None:
                return self.authDict
            else:
                return "No Key "+key

    def getKeysValues(self):
        for key, value in self.dataDict.items():
            print(key, value)

    def getKeys(self):
        for key in self.dataDict.items():
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