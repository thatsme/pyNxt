# -*- coding: utf-8 -*-

#from accounts import *
## Base package
import base.Rb as rb
import base.Ri as ri
import base.Message as msg
import base.Phasing as pha

import assetexchange.cancelAskOrder as cao
import assetexchange.cancelBidOrder as cbo
import assetexchange.deleteAssetsShares as das
import assetexchange.dividendPayment as dvpa
import assetexchange.getAllAssets as galla
import assetexchange.getAllOpenAskOrders as gaoao
import assetexchange.getAllOpenBidOrders as gaobo
import assetexchange.getAllTrades as gatd
import assetexchange.getAskOrder as gako
import assetexchange.getAskOrderIds as gakoi
import assetexchange.getAskOrders as gakos
import assetexchange.getAsset as gat
import assetexchange.getAssetAccountCount as gasacc
import assetexchange.getAssetAccounts as gasas
import assetexchange.getAssetDeletes as gatds
import assetexchange.getAssetDividends as gatdis
import assetexchange.getAssetIds as gatids
import assetexchange.getAssetPhasedTransactions as gapt
import assetexchange.getAssets as gatt
import assetexchange.getAssetTransfers as gattrf
import assetexchange.getBidOrder as gbo
import assetexchange.getBidOrderIds as gboi
import assetexchange.getBidOrders as gbos
import assetexchange.getExpectedAskOrders as geakos
import assetexchange.getExpectedAssetDeletes as geads
import assetexchange.getExpectedAssetTransfers as gestrf
import assetexchange.getExpectedBidOrders as gebios
import assetexchange.getExpectedOrderCancellations as geodca
import assetexchange.getLastTrades as gltd
import assetexchange.getOrderTrades as godtr
import assetexchange.getTrades as gtrades
import assetexchange.issueAsset as issa
import assetexchange.placeAskOrder as plaako
import assetexchange.placeBidOrder as plabio
import assetexchange.searchAssets as searcha
import assetexchange.transferAsset as trfa

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
