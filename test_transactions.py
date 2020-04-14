# -*- coding: utf-8 -*-

#from accounts import *
## Base package
import base.Rb as rb
import base.Ri as ri
import base.Message as msg
import base.Phasing as pha

import transactions.signTransactionOffline as STO
import transactions.signTransaction as STL
import transactions.broadcastTransaction as BTC
import accounts.getBlockchainTransactions as GBTC

import json
from hashlib import sha256
import codecs
import pprint

genesisBlock = " 2680262203532249785"

action = [1]
#action = [4]
#action = [12, 13, 14, 15]
#action = [10, 16]
#action = [18, 19]
#action = [39]                                      # Set an alias
#action = [44]                                      # Delete an alias
#action = [333]                                     # OffLine signing and verifing
#action = [45]                                       # GetForgeing


myMsg = msg.Message(message="pyNXT API Test - v2")
myPha = pha.Phasing(phased=False)

#message = "pyNXT API Test"

goodGuy = "NXT-AMPQ-B6ZZ-S8TL-EFDBH"
ggpK = "dc7b03d7dd03fe316bb3321c65683c7e528dbed6bdedd67d5aeae2e3dd170126"

amount = 100000000

badaccount = "NXT-XWQEY-Ce2MJ-JPL8-F4BW2"

## My First Account
me = "NXT-XWQY-C2MJ-JPL8-F4BW2"
sP = "pass dig enough trace frighten foul beaten explain knowledge yeah approach spider"
pK="6282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19"

## My Second Account
me2 = "NXT-XPSH-6XA6-S2J3-95P2B"
sP2 = "coward cheek abuse fear content advice make quietly shown snow jeans rich"
pK2 = "ff106f1a3c9cb3061031c89f18f3a9d0ba9f32b87825fe894dbf16547d5a2d72"


#for i  in myAc.get():
#    print(i, myAc.get()[i])

# print(myAc.get()["name"])

if 1 in action:
    print()
    ##

myTransactions = GBTC.GetBlockchainTransactions(account=goodGuy, timestamp=0,type=None,subtype=None,numberOfConfirmations=0,withMessage=False,phasedOnly=False,nonPhasedOnly=False,includeExpiredPrunable=False,includePhasingResult=False,executeOnly=False,ri=None,rb=None)

myTransactions.run()

oo = myTransactions.getObject()

#print(myTransactions.getData())

#a = iter(myTransactions)
#for i in a:
#    print(i)
#    next(a)

#for iterator in myTransactions:
#    print(iterator)

print(oo.transactions_0000)

if hasattr(oo, 'transactions_0023'):
    print(oo.transactions_0023.signature)

print(oo.transactions_0029.amountNQT)


#print(myTransactions.next())
#print(myTransactions.next())
#print(myTransactions.next())
#print(myTransactions.next())
#print(myTransactions.next())
