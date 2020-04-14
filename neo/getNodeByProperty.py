from base.NeoBasePost import NeoBasePost as Parent
import json

class GetNodeByProperty(Parent):

    def __init__(self, nodeType=None):
        """

        MATCH (n)
        WHERE n.name = 'Mark'
        RETURN n

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

        super(GetNodeByProperty, self).__init__(nt = nodeType)

    def setQuery(self, query):
        self.query = query
        val = query["query"]
        self.query["query"] = val.format(self.propertyname, self.propertyvalue)
        #self.query["params"] = self.props

    def setProperties(self, name, value):
        self.propertyname = name
        self.propertyvalue = value
        self.props = {}
        self.props["props"] = self.properties

    def buildPayload(self):
        self.dataj = json.dumps(self.query, ensure_ascii=False)

    def setCredentials(self, username=None, password=None):
        super(GetNodeByProperty, self).setCredentials(username, password)       # calls 'BaseGet.run()'

    def run(self):
        super(GetNodeByProperty, self).run(data = self.dataj)                           # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetNodeByProperty, self).getData(key)             # calls 'BaseGet.getData()'

    def getId(self):
        return super(GetNodeByProperty, self).getId()             # calls 'BaseGet.getData()'

        return self.dataDict["data"][0][0]["metadata"]["id"]