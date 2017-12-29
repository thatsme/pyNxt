# -*- coding: utf-8 -*-

class Credentials(object):

    def __init__(self, url, account, passphrase):
        """

        :param host: Host of blockchain
        :param account: account in RS format
        :param passphrase: your passphrase
        """
        self.url = url
        self.account = account
        self.passphrase = passphrase

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except KeyError:
            return None