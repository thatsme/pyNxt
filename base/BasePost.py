# -*- coding: utf-8 -*-
import requests
import json
from base import Phasing
from base import Message
from base import Rec
from base.TnkMap import tokenMap

class BasePost(object):

    def __init__(self, rt, data, phasing = None, message=None, rec=None):

        self.url = "http://localhost:6876/nxt"
        self.headers = {"Accept": "application/json"}
        self.dataDict = []
        self.response = None
        self.requestType = rt
        self.credentials = None

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
        self.DEBUG = False
        self.session = requests.Session()

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
        if self.phasing and isinstance(self.phasing, type(Phasing)):
            self.data = {**self.data, **self.phasing}

    def _mergeMessageParams(self):
        if self.message and isinstance(self.message, type(Message)):
            self.data = {**self.data, **self.message}

    def _mergeRecParams(self):
        if self.rec and isinstance(self.rec, type(Rec)):
            self.data = {**self.data, **self.rec}

    def run(self):
        if self.credentials is not None:
            try:
                self.response = self.session.post(self.credentials.url, data=self.data, headers=self.headers)
                if self.response.status_code == 503:
                    self.response.raise_for_status()
            except requests.exceptions.HTTPError:
                print("oops something unexpected happened!")

        else:
            try:
                self.response = self.session.post(self.url, data=self.data, headers=self.headers)
                if self.response.status_code == 503:
                    self.response.raise_for_status()
            except requests.exceptions.HTTPError:
                print("oops something unexpected happened!")

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