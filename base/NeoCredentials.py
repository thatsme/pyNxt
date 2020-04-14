# -*- coding: utf-8 -*-
import base64

class NeoCredentials(object):

    def __init__(self, url, authurl, username, password):
        """

        :param host: Host of blockchain
        :param account: account in RS format
        :param passphrase: your passphrase
        """
        self.url = url
        self.authurl = authurl
        self.username = username
        self.password = password
        self.encodedAuth = base64.b64encode(bytes(self.username.encode("utf-8")+":".encode("utf-8")+self.password.encode("utf-8")))
        self.headers = {"Accept": "application/json", "Authorization": "Basic "+self.encodedAuth.decode("utf-8")}

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except KeyError:
            return None