from curve25519.Long10 import Long10
from curve25519.Unpack import Unpack as unpack
from curve25519.Set import MSet as mset
from curve25519.Cpy import Cpy as cpy
from curve25519.Mont_Prep import Mont_Prep as mont_prep
from curve25519.Mont_Dbl import Mont_Dbl as mont_dbl
from curve25519.Mont_Add import Mont_Add as mont_add
from curve25519.Recip import Recip as recip
from curve25519.Mul import Mul as mul
from curve25519.Pack import Pack as pack
from curve25519.X_to_Y2 import X_to_Y2 as x_to_y2
from curve25519.Add import Add as add
from curve25519.Sqr import Sqr as sqr
from curve25519.Sub import Sub as sub
from curve25519.Mula_Small import Mula_Small as mula_small
from curve25519.Cpy32 import Cpy32 as cpy32
from curve25519.Is_Negative import Is_Negative as is_negative
from curve25519.Egcd32 import Egcd32 as egcd32
from curve25519.ListIsEmpty import ListIsEmpty
from curve25519.Packl_ctypes import Packl_ctypes as packl_ctypes
from curve25519.ToHexString import ToHexString

#from base.PackTest import PackTest as pack


class Core(object):

    def __init__(self, Px, s, k, Gx):

        """

        :param Px:  list[]
        :param s:   list[]
        :param k:   list[]
        :param Gx:  list[]


        """
        bit0 = None
        bit1 = None

        BASE_R2Y = Long10(5744, 8160848, 4790893, 13779497, 35730846,12541209, 49101323, 30047407, 40071253, 6226132)

        ORDER_TIMES_8 = [] * 32
        ORDER_TIMES_8.append(packl_ctypes(104).value)
        ORDER_TIMES_8.append(packl_ctypes(159).value)
        ORDER_TIMES_8.append(packl_ctypes(174).value)
        ORDER_TIMES_8.append(packl_ctypes(231).value)
        ORDER_TIMES_8.append(packl_ctypes(210).value)
        ORDER_TIMES_8.append(packl_ctypes(24).value)
        ORDER_TIMES_8.append(packl_ctypes(147).value)
        ORDER_TIMES_8.append(packl_ctypes(192).value)
        ORDER_TIMES_8.append(packl_ctypes(178).value)
        ORDER_TIMES_8.append(packl_ctypes(230).value)
        ORDER_TIMES_8.append(packl_ctypes(188).value)
        ORDER_TIMES_8.append(packl_ctypes(23).value)
        ORDER_TIMES_8.append(packl_ctypes(245).value)
        ORDER_TIMES_8.append(packl_ctypes(206).value)
        ORDER_TIMES_8.append(packl_ctypes(247).value)
        ORDER_TIMES_8.append(packl_ctypes(166).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(0).value)
        ORDER_TIMES_8.append(packl_ctypes(128).value)

        ORDER = [] * 32
        ORDER.append(packl_ctypes(237).value)
        ORDER.append(packl_ctypes(211).value)
        ORDER.append(packl_ctypes(245).value)
        ORDER.append(packl_ctypes(92).value)
        ORDER.append(packl_ctypes(26).value)
        ORDER.append(packl_ctypes(99).value)
        ORDER.append(packl_ctypes(18).value)
        ORDER.append(packl_ctypes(88).value)
        ORDER.append(packl_ctypes(214).value)
        ORDER.append(packl_ctypes(156).value)
        ORDER.append(packl_ctypes(247).value)
        ORDER.append(packl_ctypes(162).value)
        ORDER.append(packl_ctypes(222).value)
        ORDER.append(packl_ctypes(249).value)
        ORDER.append(packl_ctypes(222).value)
        ORDER.append(packl_ctypes(20).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(0).value)
        ORDER.append(packl_ctypes(16).value)

        #print("ORDER ", ToHexString(ORDER).getString())

        dx = Long10()
        t1 = Long10()
        t2 = Long10()
        t3 = Long10()
        t4 = Long10()


        x = [Long10(), Long10()]
        z = [Long10(), Long10()]

        i=32
        j=0

        # unpack the base
        if (Gx != None):
            unpack(dx, Gx)
        else:
            mset(dx, 9)

        # 0G = point-at-infinity
        mset(x[0], 1)
        mset(z[0], 0)

        # 1G = G
        cpy(x[1], dx)
        mset(z[1], 1)

        #range(10, 0, -1)
        for i in range(31, -1, -1):
            if (i == 0):
                i=0
            for j in range(7,-1,-1):
                # swap arguments depending on bit * /
                bit1 = int((k[i] & 0xFF) >> j & 1)
                bit0 = int(~(k[i] & 0xFF) >> j & 1)
                ax = x[bit0]
                az = z[bit0]
                bx = x[bit1]
                bz = z[bit1]
                # a' = a + b	*/
                # b' = 2 b	*/
                mont_prep(t1, t2, ax, az)
                mont_prep(t3, t4, bx, bz)
                mont_add(t1, t2, t3, t4, ax, az, dx)
                mont_dbl(t1, t2, t3, t4, bx, bz)



        recip(t1, z[0], 0)
        mul(dx, x[0], t1)
        pack(dx, Px)

        if s is not None:
            x_to_y2(t2, t1, dx)                     # t1 = Py ^ 2
            recip(t3, z[1], 0)                      # where Q=P+G...
            mul(t2, x[1], t3)                       # t2 = Qx
            add(t2, t2, dx)                         # t2 = Qx + Px
            t2._0 += 9 + 486662                     # t2 = Qx + Px + Gx + 486662
            dx._0 -= 9                              # dx = Px - Gx
            sqr(t3, dx)                             # t3 = (Px - Gx) ^ 2
            mul(dx, t2, t3)                         # dx = t2 (Px - Gx) ^ 2
            sub(dx, dx, t1)                         # dx = t2 (Px - Gx) ^ 2 - Py ^ 2
            dx._0 -= 39420360                       # dx = t2 (Px - Gx) ^ 2 - Py ^ 2 - Gy ^ 2
            mul(t1, dx, BASE_R2Y)                   # t1 = -Py
            if is_negative(t1).value != 0:          # sign is 1, so just copy
                cpy32(s, k)
            else:                                   # sign is -1, so negate *
                mula_small(s, ORDER_TIMES_8, 0, k, 32, -1)

            # reduce s mod q
            # ( is this needed?  do it just in case, it's fast anyway) */
            #// divmod((dstptr) t1, s, 32, order25519, 32);

            # take reciprocal of s mod q
            ## Ok dobbiamo modificarli in liste
            ## in quanto all'interno

            #temp1 = bytearray()
            #temp2 = bytearray()
            #temp3 = bytearray()
            temp1 = [0] * 32
            temp2 = [0] * 64
            temp3 = [0] * 64

            #for i in range(32):
            #    temp1.append(0x00)

            #for i in range(64):
            #    temp2.append(0x00)
            #    temp3.append(0x00)

            cpy32(temp1, ORDER)
            vediamo = egcd32(temp2, temp3, s, temp1).value
            cpy32(s, vediamo)
            if s[31] & 0x80 != 0:
                mula_small(s, s, 0, ORDER, 32, 1)

        else:
            print("CORE S  --> IS NULL !!!!")