# -*- coding: utf-8 -*-

## Base  package
import base.Rb as rb
import base.Ri as ri
import base.Message as msg
import base.Phasing as pha

## Aliases package
import aliases.buyAlias as ba
import aliases.deleteAlias as da
import aliases.getAlias as gas
import aliases.getAliasCount as gasc
import aliases.getAliases as gases
import aliases.getAliasesLike as gasesl
import aliases.sellAlias as sla
import aliases.setAlias as sta

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


if 1 in action:

    myBa = ba.BuyAlias(aliasName="myaliasname",amountNQT=100000000, secretPhrase=sP,)

    myBa.run()

    if myBa.getErrorCode():
        print("Error description : ", myBa.getErrorDescription(), myBa.getErrorCode())
    else:
        output = myBa.getData()

        print(json.dumps(output, indent=4))

if 2 in action:

    ## For setting an alias the minimum fee required is 200000000
    ## so we set it here
    #mySta = sta.SetAlias(aliasName="securtel",aliasURI="http://www.securtel.net",secretPhrase=sP, feeNQT=200000000,deadline=0)
    mySta = sta.SetAlias(aliasName="test66",aliasURI="http://www.test.net",secretPhrase=sP, feeNQT=200000000,deadline=0)

    mySta.run()

    if mySta.getErrorCode():
        print("Error description : ", mySta.getErrorDescription(), mySta.getErrorCode())
    else:
        output = mySta.getData()
        print(json.dumps(output, indent=4))

if 3 in action:

    myGas = gas.GetAlias(aliasName="securtel")
    myGas.run()

    if myGas.getErrorCode():
        print("Error description : ", myGas.getErrorDescription(), myGas.getErrorCode())
    else:
        output = myGas.getData()
        print(json.dumps(output, indent=4))

if 4 in action:

    myGasc = gasc.GetAliasCount(account=me)
    myGasc.run()

    if myGasc.getErrorCode():
        print("Error description : ", myGasc.getErrorDescription(), myGasc.getErrorCode())
    else:
        output = myGasc.getData()
        print(json.dumps(output, indent=4))

if 5 in action:

    myGases = gases.GetAliases(account=me)
    myGases.run()

    if myGases.getErrorCode():
        print("Error description : ", myGases.getErrorDescription(), myGases.getErrorCode())
    else:
        output = myGases.getData()
        print(json.dumps(output, indent=4))

if 6 in action:

    myGasesl = gasesl.GetAliasesLike(aliasPrefix="se")
    myGasesl.run()

    if myGasesl.getErrorCode():
        print("Error description : ", myGasesl.getErrorDescription(), myGasesl.getErrorCode())
    else:
        output = myGasesl.getData()
        print(json.dumps(output, indent=4))

if 7 in action:

    myDa = da.DeleteAlias(aliasName="test66",secretPhrase=sP,feeNQT=0)
    myDa.run()

    if myDa.getErrorCode():
        print("Error description : ", myDa.getErrorDescription(), myDa.getErrorCode())
    else:
        output = myDa.getData()
        print(json.dumps(output, indent=4))

