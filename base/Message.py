

class Message(object):

    def __init__(self, message=None, messageIsText = None, messageIsPrunable = None, messageToEncrypt = None, \
                    messageToEncryptIsText = None, encryptedMessageData=None, encryptedMessageNonce=None, encryptedMessageIsPrunable=None, \
                    compressMessageToEncrypt=None, messageToEncryptToSelf=None, messageToEncryptToSelfIsText=None, \
                    encryptToSelfMessageData=None, encryptToSelfMessageNonce=None, compressMessageToEncryptToSelf=None):

        self.message = {}
        self.message["message"] = message
        self.message["messageIsText"] = messageIsText
        self.message["messageIsPrunable"] = messageIsPrunable
        self.message["messageToEncrypt"] = messageToEncrypt
        self.message["messageToEncryptIsText"] = messageToEncryptIsText
        self.message["encryptedMessageData"] = encryptedMessageData
        self.message["encryptedMessageNonce"] = encryptedMessageNonce
        self.message["encryptedMessageIsPrunable"] = encryptedMessageIsPrunable
        self.message["compressMessageToEncrypt"] = compressMessageToEncrypt
        self.message["messageToEncryptToSelf"] = messageToEncryptToSelf
        self.message["messageToEncryptToSelfIsText"] = messageToEncryptToSelfIsText
        self.message["encryptToSelfMessageData"] = encryptToSelfMessageData
        self.message["encryptToSelfMessageNonce"] = encryptToSelfMessageNonce
        self.message["compressMessageToEncryptToSelf"] = compressMessageToEncryptToSelf


        self._buildDict()

    def _buildDict(self):

        for x in [x for x in self.message.keys() if self.message[x] == None]:
            self.message.pop(x)

    def getParam(self):
        return self.message