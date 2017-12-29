# -*- coding: utf-8 -*-
import requests
import json
from base import Phasing
from base import Message
from base import Rec
from base.TnkMap import tokenMap

class BasePost(object):

    def __init__(self, rt, data, phasing = None, message=None, rec=None):

        self.account = "NXT-XWQY-C2MJ-JPL8-F4BW2"
        self.url = "http://localhost:6876/nxt"
        self.headers = {"Accept": "application/json"}
        self.dataDict = []
        self.response = None
        self.requestType = rt
        self.credentials = None

        # self.data = {"requestType": self.requestType, "accounts": self.accounts}
        self.data = data
        self.phasing = phasing
        self.message = message
        self.rec = rec

        # print(self.data)
        self._mergeRequestType()
        self._mergePhasingParams()
        self._mergeMessageParams()
        self._mergeRecParams()

        self.errorCode = None
        self.errorDescription = None
        self.mObj = object

    def setCredentials(self, credentials):
        self.credentials = credentials

    def _checkAccountFormat(self, value):
        if value[:4] == "NXT-" and value[8:9] == "-" and  value[13:14] == "-" and value[18:19] == "-":
            return True

    def _mergeRequestType(self):
        if self.requestType:
            if "requestType" not in self.data:
                self.data["requestType"] = self.requestType

    def _mergePhasingParams(self):
        if self.phasing and isinstance(self.phasing, Phasing):
            self.data = {**self.data, **self.phasing}

    def _mergeMessageParams(self):
        if self.message and isinstance(self.message, Message):
            self.data = {**self.data, **self.message}

    def _mergeRecParams(self):
        if self.rec and isinstance(self.rec, Rec):
            self.data = {**self.data, **self.rec}

    def _checkAccountFormat(self, value):
        if value[:4] == "NXT-" and value[8:9] == "-" and  value[13:14] == "-" and value[18:19] == "-":
            return True

    def run(self):
        if self.credentials is not None:
            self.response = requests.post(self.credentials.url, data=self.data, headers=self.headers)
        else:
            self.response = requests.post(self.url, data=self.data, headers=self.headers)

        self.dataDict = json.loads(self.response.text)
        self.mObj = tokenMap(**self.dataDict)

        if "errorCode" in self.dataDict:
            self.errorCode = self.dataDict["errorCode"]
            self.errorDescription = self.dataDict["errorDescription"]

    def getData(self, key=None):
        if key in self.dataDict:
            return self.dataDict[key]
        else:
            if key is None:
                return self.dataDict
            else:
                return None

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