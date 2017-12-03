from base.Long10 import Long10
from base.Unpack import Unpack as unpack
from base.Set import MSet as mset
from base.Cpy import Cpy as cpy
from base.Mont_Prep import Mont_Prep as mont_prep
from base.Mont_Dbl import Mont_Dbl as mont_dbl
from base.Mont_Add import Mont_Add as mont_add
from base.Recip import Recip as recip
from base.Mul import Mul as mul
from base.Pack import Pack as pack
from base.X_to_Y2 import X_to_Y2 as x_to_y2
from base.Add import Add as add
from base.Sqr import Sqr as sqr
from base.Sub import Sub as sub
from base.Mula_Small import Mula_Small as mula_small
from base.Cpy32 import Cpy32 as cpy32
from base.Is_Negative import Is_Negative as is_negative
from base.Egcd32 import Egcd32 as egcd32
#from base.PackTest import PackTest as pack
class Core(object):

    def __init__(self, Px, s, k, Gx):

        """

        :param Px: bite[]
        :param s: bite[]
        :param k: bite[]
        :param Gx: bite[]


        """
        bit0 = None
        bit1 = None

        BASE_2Y = Long10(39999547, 18689728, 59995525, 1648697, 57546132,24010086, 19059592, 5425144, 63499247, 16420658)
        BASE_R2Y = Long10(5744, 8160848, 4790893, 13779497, 35730846,12541209, 49101323, 30047407, 40071253, 6226132)

        ORDER_TIMES_8 = bytearray()
        ORDER_TIMES_8.append(104)
        ORDER_TIMES_8.append(159)
        ORDER_TIMES_8.append(174)
        ORDER_TIMES_8.append(231)
        ORDER_TIMES_8.append(210)
        ORDER_TIMES_8.append(24)
        ORDER_TIMES_8.append(147)
        ORDER_TIMES_8.append(192)
        ORDER_TIMES_8.append(178)
        ORDER_TIMES_8.append(230)
        ORDER_TIMES_8.append(188)
        ORDER_TIMES_8.append(23)
        ORDER_TIMES_8.append(245)
        ORDER_TIMES_8.append(206)
        ORDER_TIMES_8.append(247)
        ORDER_TIMES_8.append(166)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(0)
        ORDER_TIMES_8.append(128)

        ORDER = bytearray()
        ORDER.append(237)
        ORDER.append(211)
        ORDER.append(245)
        ORDER.append(92)
        ORDER.append(26)
        ORDER.append(99)
        ORDER.append(18)
        ORDER.append(88)
        ORDER.append(214)
        ORDER.append(156)
        ORDER.append(247)
        ORDER.append(162)
        ORDER.append(222)
        ORDER.append(249)
        ORDER.append(222)
        ORDER.append(20)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(0)
        ORDER.append(16)


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

        print("dx._0",dx._0)
        print("x[1]._0",x[1]._0)

        #range(10, 0, -1)
        for i in range(31, -1, -1):
            if (i == 0):
                i=0
            for j in range(7,-1,-1):
                # swap arguments depending on bit * /
                bit1 = (k[i] & 0xFF) >> j & 1
                bit0 = ~(k[i] & 0xFF) >> j & 1
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

        if s != None:
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
            if is_negative(t1) != 0:               # sign is 1, so just copy
                cpy32(s, k)
            else:                                   # sign is -1, so negate *
                mula_small(s, ORDER_TIMES_8, 0, k, 32, -1)

            # reduce s mod q
            # ( is this needed?  do it just in case, it's fast anyway) */
            #// divmod((dstptr) t1, s, 32, order25519, 32);

            # take reciprocal of s mod q
            temp1 = bytearray()
            temp2 = bytearray()
            temp3 = bytearray()

            for i in range(32):
                temp1.append(0x00)

            for i in range(64):
                temp2.append(0x00)
                temp3.append(0x00)

            cpy32(temp1, ORDER);
            print("temp1-->", temp1)
            cpy32(s, egcd32(temp2, temp3, s, temp1))
            if (s[31] & 0x80) != 0:
                mula_small(s, s, 0, ORDER, 32, 1)

