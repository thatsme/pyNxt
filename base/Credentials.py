
class Credentials(object):

    def __init__(self, host, account, passphrase):

        self.host = host
        self.account = account
        self.passphrase = passphrase

    def __getattribute__(self, attr):
        try:
            return self.__dict__[attr]
        except KeyError:
            return None