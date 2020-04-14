# -*- coding: utf-8 -*-

from blocks.getBlock import GetBlock
from neo.createNodeWithParameters import CreateNodeWithParameters
from neo.getNodeByProperty import GetNodeByProperty
from neo.createRelationship import CreateRelationship
from neo.createUsersFromTransaction import CreateUsersFromTransaction
from base.NeoCredentials import NeoCredentials
import json
import fire


"""
mm = {"query" : "CREATE (n:Person { props } ) RETURN n"}
mmp = {"params" : {"props" : {
      "position" : "Developer",
      "name" : "Michael",
      "awesome" : True,
      "children" : 3
    }
  }
}
"""


"""
ALL NEEDED INDEXES

CREATE INDEX ON :Transaction(transaction)
CREATE INDEX ON :User(userid)
CREATE INDEX ON :Block(blockid)


"""


class WorkTheBlocks(object):

    def __init__(self, name, password):

        genesisBlock = "2680262203532249785"

        self.block = genesisBlock

        mr = {"query": "START n = node({0}), m = node({1}) create(n) - [r:{2}]->(m)"}
        #mm = {"query": "CREATE (n:%s { props } ) RETURN n"}
        #mmt = {"query": "CREATE (n:%s { props } ) RETURN n"}
        mm = {"query": "CREATE (n:{0} {{ props }} ) RETURN n"}
        mmt = {"query": "CREATE (n:{0} {{ props }} ) RETURN n"}


        self.crd = NeoCredentials("http://localhost:7474/db/data/cypher","http://localhost:7474/user/neo4j", name, password)

        self.cn = CreateNodeWithParameters("Block")
        self.cn.setCredential(self.crd)
        self.cn.connect()
        self.cn.setQuery(mm)

        self.gn = GetNodeByProperty()
        self.gn.setCredential(self.crd)
        self.gn.connect()

        self.cr = CreateRelationship("IS_PREVIOUS")
        self.cr.setCredential(self.crd)
        self.cr.connect()
        self.cr.setQuery(mr)

        self.ct = CreateNodeWithParameters("Transaction")
        self.ct.setCredential(self.crd)
        self.ct.connect()
        self.ct.setQuery(mm)

        self.cu = CreateUsersFromTransaction("User",None)
        self.cu.setCredential(self.crd)
        self.cu.connect()
        self.cu.setQuery(mm)

        #self.run()

    def run(self):

        for a in range(500):

            gb = GetBlock(block=self.block, includeTransactions=True)
            gb.run()

            ## Get the next Block ( pointer )
            next = gb.getData("nextBlock")
            previous = gb.getData("previousBlock")
            ttransaction = gb.getData("numberOfTransactions")
            transactions = gb.getData("transactions")
            print("========================================")
            print("Data --> ", previous, next, ttransaction)

            mmp = {"previous": previous, "next": next, "numTransactions": ttransaction, "blockid": gb.getData("block")}

            ## The node don't exist, so we create it
            if not self.cn.validateUniqueId("blockid", gb.getData("block")):

                self.cn.setNodeType("Block")
                self.cn.setProperties(mmp)
                self.cn.buildPayload()

                self.cn.run()
                currentId = self.cn.getId()

            ## If the node have a previous property filled ( this mean the block isn't a genesis block )
            ## we we get the id of previous node and then we create a relation
            ## the flow of creating a relation is :
            ## <relation object>.setSourceNode(<someid>)
            ## <relation object>.setTargetNode(<someid>)
            ## <relation object>.setRelationshipName(<name of relation>)
            ## <relation object>.setNodeType(<target type node>,<source type node>) ( or viceversa .. forgot )
            ## <relation object>.buildPayload()
            ## <relation object>.run()
            if previous:
                qn = {"query": "MATCH(n) WHERE n.{0} = '{1}' RETURN n"}
                self.gn.setProperties("blockid", previous)
                self.gn.setQuery(qn)
                self.gn.buildPayload()
                self.gn.run()
                previousId = self.gn.getId()
                print("Previous ID : ", self.gn.getId())

                ## Make a relation
                ## mm = {"query": "MATCH a, b WHERE a(...) AND b(...) CREATE UNIQUE a - [r: CONNECTED_TO]->b"}
                #mr = {"query": "MATCH(a:{0}),(b:{1}) WHERE HAS(a.id) AND HAS(b.id) AND a.id = {2} AND b.id = {3} CREATE(a) - [: {4}]->(b)"}
                ##mr = {"query": "MATCH(a:{0}),(b:{1}) WHERE a.id = {2} AND b.id = {3} CREATE(a) - [r: {4}]->(b)"}

                self.cr.setSourceNode(currentId)
                self.cr.setTargetNode(previousId)
                self.cr.setRelationshipName("IS_PREVIOUS")
                ## Deprecated --> setNodeType in CreateReleationship
                self.cr.setNodeType("Block","Block")
                # cr.setQuery(mr)
                self.cr.buildPayload()
                self.cr.run()


            ## After creation of current -> previous relationship
            ## we go check the number of transactions on current node,
            ## if is major then 0, we go to insert that transactions
            ##
            if ttransaction > 0:
                for tr in transactions:
                    print("Transaction index ", tr["transactionIndex"])
                    print("Sender --> ",tr["sender"])
                    print(tr["recipient"], "<-- Receiver")
                    print("Amount ",tr["amountNQT"])

                    ## Set properties for transaction Node
                    mmtp = {"transaction": tr["transaction"], "sender": tr["sender"], "recipient": tr["recipient"], "amount": tr["amountNQT"], "transactionindex": tr["transactionIndex"]}

                    ## ADD TRANSACTION NODE
                    ## The procedure is :
                    ## <transaction node>.reset()
                    ## <transaction node>.setNodeType(<type of node>)
                    ## <transaction node>.setProperties(<properties dictionary>)
                    ## <transaction node>.buildPayload()
                    ## <transaction node>.run()
                    ## ========================
                    ## <transaction node>.getId() <-- assigning newly created node id
                    self.ct.reset()
                    self.ct.setNodeType("Transaction")
                    self.ct.setProperties(mmtp)
                    #ct.setQuery(mmt)
                    #ct.setQuery(mm)
                    self.ct.buildPayload()
                    self.ct.run()
                    currentTransactionId = self.ct.getId()

                    ## ADD RELATIONSHIP NODE BACK TO CURRENT BLOCK NODE
                    ## The procedure is :
                    ## <relation object>.reset()
                    ## <relation object>.setSourceNode(<current block id node>)
                    ## <relation object>.setTargetNode(<transactio node just created>)
                    ## <relation object>.setRelationshipName(<name of relation>)
                    ## <relation object>.setNodeType(....) <-- Deprecated
                    ## <relation object>.buildPayload()
                    ## <relation object>.run()
                    self.cr.reset()
                    self.cr.setSourceNode(currentId)
                    self.cr.setTargetNode(currentTransactionId)
                    self.cr.setRelationshipName("HAS_TRANSACTION")
                    ## Deprecated --> setNodeType in CreateReleationship
                    self.cr.setNodeType("Block","Block")
                    # cr.setQuery(mr)
                    self.cr.buildPayload()
                    self.cr.run()

                    ## ADD USERS NODES
                    self.cu.reset()
                    self.cu.setNodeType("User")
                    currentUser = self.cu.validateUniqueId("userid", tr["sender"])
                    if currentUser is None:
                        self.cu.addSender(tr["sender"], tr["senderRS"])
                        ##
                        self.cu.setNodeType("sender")
                        self.cu.setProperties(None)
                        self.cu.buildPayload()
                        self.cu.run()
                        currentUser = self.cu.getId()
                    else:
                        print("User present ",currentUser)

                    ## ADD RELATIONSHIP NODE BACK TO TRANSACTION
                    self.cr.reset()
                    self.cr.setSourceNode(currentUser)
                    self.cr.setTargetNode(currentTransactionId)
                    self.cr.setRelationshipName("TRANSACTION_SENDER")
                    self.cr.setNodeType("Block","Block")
                    # cr.setQuery(mr)
                    self.cr.buildPayload()
                    self.cr.run()

                    currentUser = self.cu.validateUniqueId("userid", tr["recipient"])
                    if currentUser is None:
                        self.cu.addRecipient(tr["recipient"], tr["recipientRS"])

                        ##
                        self.cu.setNodeType("recipient")
                        self.cu.setProperties(None)
                        self.cu.buildPayload()
                        self.cu.run()
                        currentUser = self.cu.getId()
                    else:
                        print("User present ",currentUser)

                    ## ADD RELATIONSHIP NODE BACK TO TRANSACTION
                    self.cr.reset()
                    self.cr.setSourceNode(currentUser)
                    self.cr.setTargetNode(currentTransactionId)
                    self.cr.setRelationshipName("TRANSACTION_RECIPIENT")
                    self.cr.setNodeType("Block","Block")
                    # cr.setQuery(mr)
                    self.cr.buildPayload()
                    self.cr.run()


            self.block = next


if __name__ == '__main__':
  fire.Fire(WorkTheBlocks)