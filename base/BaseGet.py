# -*- coding: utf-8 -*-
import requests
import json
from base import Phasing
from base import Message
from base import Rb
from base import Ri

class BaseGet(object):

    def __init__(self, rt, data, phasing = None, message=None, rb = None, ri = None):

        # self.accounts = "NXT-XWQY-C2MJ-JPL8-F4BW2"
        self.url = "http://localhost:6876/nxt"
        self.headers = {"Accept": "application/json"}
        self.dataDict = []
        self.response = None
        self.requestType = rt
        #self.data = {"requestType": self.requestType, "accounts": self.accounts}

        self.data = data
        self.phasing = phasing
        self.message = message
        self.rb = rb
        self.ri = ri

        # print(self.data)
        self._mergeRequestType()
        self._mergePhasingParams()
        self._mergeMessageParams()
        self._mergeRbParams()
        self._mergeRiParams()

        self.errorCode = None
        self.errorDescription = None

    def param(self):
        pass

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

    def _mergeRbParams(self):
        if self.rb and isinstance(self.rb, Rb):
            self.data = {**self.data, **self.rb}

    def _mergeRiParams(self):
        if self.ri and isinstance(self.phasing, Ri):
            self.data = {**self.data, **self.ri}

    def run(self):
        self.response = requests.get(self.url, params=self.data, headers=self.headers)
        self.dataDict = json.loads(self.response.text)
        if "errorCode" in self.dataDict:
            self.errorCode = self.dataDict["errorCode"]
            self.errorDescription = self.dataDict["errorDescription"]

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        if key in self.dataDict:
            return self.dataDict[key]
        else:
            if key is None:
                return self.dataDict
            else:
                return "No Key"

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