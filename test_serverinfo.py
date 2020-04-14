# -*- coding: utf-8 -*-

## Base  package
import base.Rb as rb
import base.Ri as ri
import base.Message as msg
import base.Phasing as pha
import base.Credentials as credentials

## Aliases package
import serverinfo.getConstants as gc

import json
#from hashlib import sha256
#import codecs
#import pprint

genesisBlock = " 2680262203532249785"

action = [1]

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

cr = credentials.Credentials("http://localhost:6876/nxt", me, None)

if 1 in action:

    myConstant = gc.GetConstants()

    myConstant.setCredentials(cr)
    myConstant.run()

    myObject = myConstant.getObject()


    print(myObject.apiTags.ACCOUNTS)
    print(myObject.apiTags.ACCOUNTS.enabled)
    print(myObject.apiTags.ACCOUNTS.name)
    print(myObject.shufflingStages)
    print(myObject.genesisBlockId)
