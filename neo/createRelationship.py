# -*- coding: utf-8 -*-
from base.NeoBasePost import NeoBasePost as Parent
import json

class CreateRelationship(Parent):

    def __init__(self, relationshipType=None):
        """
        a = Nodo nuovo
        b = Nodo precedente
        MATCH (a:Block),(b:Block)
        WHERE a.id = "{1}" AND b.id = "{2}"
        CREATE (a)-[r:FOLLOW]->(b)
        RETURN r
        """

        self.query = None
        self.properties = None
        self.props = None
        self.dataj = None
        # Initialize dictionary
        self.data = {}
        self.nodeType = None
        self.sourceNode = None
        self.targetNode = None
        self.relationshipType = relationshipType
        self.int_val = None

        super(CreateRelationship, self).__init__(nt = relationshipType)

    def reset(self):
        self.sourceNode = None
        self.targetNode = None
        self.relationshipType = None

    def setQuery(self, query):
        self.query = query
        self.int_val = self.query["query"]

    def setSourceNode(self, sn):
        self.sourceNode = sn

    def setTargetNode(self, tn):
        self.targetNode = tn

    def setNodeType(self, nt1, nt2):
        self.nodeType1 = nt1
        self.nodeType2 = nt2

    def setRelationshipName(self, rn):
        self.relationshipType = rn

    def buildPayload(self):
        #val = self.query["query"]
        #self.query["query"] = val.format(self.nodeType1, self.nodeType2 , self.sourceNode, self.targetNode, self.relationshipTyle)
        self.query["query"] = self.int_val.format(self.sourceNode, self.targetNode, self.relationshipType)
        # No params on this
        #self.query["params"] = self.props
        self.dataj = json.dumps(self.query, ensure_ascii=False)

    def setCredentials(self, username=None, password=None):
        super(CreateRelationship, self).setCredentials(username, password)       # calls 'BaseGet.run()'

    def run(self):
        super(CreateRelationship, self).run(data = self.dataj)                   # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(CreateRelationship, self).getData(key)             # calls 'BaseGet.getData()'