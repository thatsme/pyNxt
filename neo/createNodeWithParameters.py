from base.NeoBasePost import NeoBasePost as Parent
import json

class CreateNodeWithParameters(Parent):

    def __init__(self, nodeType=None):
        """
        :param query:
        :param properties:
        """

        self.query = None
        self.properties = None
        self.props = None
        self.dataj = None
        # Initialize dictionary
        self.data = {}
        self.nodeType = None
        self.int_val = None
        self.DEBUG = False

        super(CreateNodeWithParameters, self).__init__(nt = nodeType)

    def reset(self):
        self.nodeType = None
        self.props = None

    def validateUniqueId(self, field, value):
        q = "MATCH(a: {0} {{{1}: '{2}'}}) USING INDEX a: {0}({1}) RETURN a"
        self.query["query"] = q.format(self.nodeType,field,value)
        self.dataj = json.dumps(self.query, ensure_ascii=False)
        self.run()
        return self.getId()

    def setQuery(self, query):
        self.query = query
        self.int_val = self.query["query"]

    def setProperties(self, properties):
        self.properties = properties
        self.props = {}
        self.props["props"] = self.properties

    def setNodeType(self, nt):
        self.nodeType = nt

    def buildPayload(self):
        self.query["query"] = self.int_val.format(self.nodeType)
        self.query["params"] = self.props

        self.dataj = json.dumps(self.query, ensure_ascii=False)

    def setCredentials(self, username=None, password=None):
        super(CreateNodeWithParameters, self).setCredentials(username, password)       # calls 'BaseGet.run()'

    def run(self):
        super(CreateNodeWithParameters, self).run(data = self.dataj)                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(CreateNodeWithParameters, self).getData(key)             # calls 'BaseGet.getData()'

    def getId(self):
        return super(CreateNodeWithParameters, self).getId()             # calls 'BaseGet.getData()'

