from neo.createNodeWithParameters import CreateNodeWithParameters as Parent
import json

class CreateUsersFromTransaction(Parent):


    def __init__(self, nodeType="User", transactionId=None):
        """
        :param query:
        :param properties:
        """

        self.transactionId = transactionId
        self.query = None
        self.properties = None
        self.props = None
        self.dataj_sender = None
        self.dataj_recipient = None
        # Initialize dictionary
        self.data = {}
        self.nodeType = None
        self.sender = None
        self.senderRS = None
        self.recipient = None
        self.recipientRS = None

        super(CreateUsersFromTransaction, self).__init__(nodeType = nodeType)

    def addSender(self, sender, senderRS):
        self.sender = sender
        self.senderRS = senderRS

    def addRecipient(self, recipient, recipientRS):
        self.recipient = recipient
        self.recipientRS = recipientRS

    def setQuery(self, query):
        super(CreateUsersFromTransaction, self).setQuery(query)

    def setProperties(self, properties):
        if "sender" in self.nodeType:
            self.properties = {"userid": self.sender, "useridRS": self.senderRS}
            self.props = {}
            self.props["props"] = self.properties
        if "recipient" in self.nodeType:
            self.properties = {"userid": self.recipient, "useridRS": self.recipientRS}
            self.props = {}
            self.props["props"] = self.properties

    def setNodeType(self, nt):
        self.nodeType = nt

    def buildPayload(self):
        if "sender" in self.nodeType:
            self.query["query"] = self.int_val.format("User")
            self.query["params"] = self.props
            self.dataj = json.dumps(self.query, ensure_ascii=False)
        if "recipient" in self.nodeType:
            self.query["query"] = self.int_val.format("User")
            self.query["params"] = self.props
            self.dataj = json.dumps(self.query, ensure_ascii=False)

    def setCredentials(self, username=None, password=None):
        super(CreateUsersFromTransaction, self).setCredentials(username, password)       # calls 'BaseGet.run()'

    def run(self):
        super(CreateUsersFromTransaction, self).run()                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(CreateUsersFromTransaction, self).getData(key)             # calls 'BaseGet.getData()'

    def getId(self):
        return super(CreateUsersFromTransaction, self).getId()             # calls 'BaseGet.getData()'

