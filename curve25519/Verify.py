from curve25519.Long10 import Long10
from curve25519.Unpack import Unpack as unpack
from curve25519.X_to_Y2 import X_to_Y2 as x_to_y2
from curve25519.Sqrt import Sqrt as sqrt
from curve25519.Mul import Mul as mul
from curve25519.Sub import Sub as sub
from curve25519.Add import Add as add
from curve25519.Cpy import Cpy as cpy
from curve25519.Is_Negative import Is_Negative as is_negative
from curve25519.Sqr import Sqr as sqr
from curve25519.Recip import Recip as recip
from curve25519.Mul_Small import Mul_Small as mul_small
from curve25519.Mont_Prep import Mont_Prep as mont_prep
from curve25519.Mont_Add import Mont_Add as mont_add
from curve25519.Mont_Dbl import Mont_Dbl as mont_dbl
from curve25519.Pack import Pack as pack
from curve25519.Packl_ctypes import Packl_ctypes as packl_ctypes

class Verify(object):

    def __init__(self,Y, v,  h,  P):
        """

        :param Y:  list[]
        :param v:   list[]
        :param h:   list[]
        :param P:  list[]
        """

        BASE_2Y = Long10(39999547, 18689728, 59995525, 1648697, 57546132,24010086, 19059592, 5425144, 63499247, 16420658)

        # Y = v abs(P) + h G
        d = [] * 32
        p = Long10(Long10(), Long10())
        s = Long10(Long10(), Long10())
        yx = Long10(Long10(), Long10(), Long10())
        yz = Long10(Long10(), Long10(), Long10())
        t1 = Long10(Long10(), Long10(), Long10())
        t2 = Long10(Long10(), Long10(), Long10())

        vi = 0
        hi = 0
        di = 0
        nvh=0
        i = None
        j = None
        k = None

        # set p[0] to G and p[1] to P

        set(p[0], 9)
        unpack(p[1], P)

        # set s[0] to P+G and s[1] to P-G

        # s[0] = (Py^2 + Gy^2 - 2 Py Gy)/(Px - Gx)^2 - Px - Gx - 486662
        # s[1] = (Py^2 + Gy^2 + 2 Py Gy)/(Px - Gx)^2 - Px - Gx - 486662

        x_to_y2(t1[0], t2[0], p[1])	                # t2[0] = Py^2
        sqrt(t1[0], t2[0])	                        # t1[0] = Py or -Py
        j = is_negative(t1[0])		                #      ... check which
        t2[0]._0 += 39420360		                # t2[0] = Py^2 + Gy^2
        mul(t2[1], BASE_2Y, t1[0])                  # t2[1] = 2 Py Gy or -2 Py Gy
        sub(t1[j], t2[0], t2[1])	                # t1[0] = Py^2 + Gy^2 - 2 Py Gy
        add(t1[1-j], t2[0], t2[1])                  # t1[1] = Py^2 + Gy^2 + 2 Py Gy
        cpy(t2[0], p[1])		                    # t2[0] = Px
        t2[0]._0 -= 9;			                    # t2[0] = Px - Gx
        sqr(t2[1], t2[0])		                    # t2[1] = (Px - Gx)^2
        recip(t2[0], t2[1], 0)	                    # t2[0] = 1/(Px - Gx)^2
        mul(s[0], t1[0], t2[0])	                    # s[0] = t1[0]/(Px - Gx)^2
        sub(s[0], s[0], p[1])	                    # s[0] = t1[0]/(Px - Gx)^2 - Px
        s[0]._0 -= 9 + 486662		                # s[0] = X(P+G)
        mul(s[1], t1[1], t2[0])	                    # s[1] = t1[1]/(Px - Gx)^2
        sub(s[1], s[1], p[1])	                    # s[1] = t1[1]/(Px - Gx)^2 - Px
        s[1]._0 -= 9 + 486662		                # s[1] = X(P-G)
        mul_small(s[0], s[0], 1)	                # reduce s[0]
        mul_small(s[1], s[1], 1)	                # reduce s[1]


        # prepare the chain
        for i in range(32):
            vi = (vi >> 8) ^ (v[i] & 0xFF) ^ ((v[i] & 0xFF) << 1)
            hi = (hi >> 8) ^ (h[i] & 0xFF) ^ ((h[i] & 0xFF) << 1)
            nvh = ~(vi ^ hi)
            di = (nvh & (di & 0x80) >> 7) ^ vi
            di ^= nvh & (di & 0x01) << 1
            di ^= nvh & (di & 0x02) << 1
            di ^= nvh & (di & 0x04) << 1
            di ^= nvh & (di & 0x08) << 1
            di ^= nvh & (di & 0x10) << 1
            di ^= nvh & (di & 0x20) << 1
            di ^= nvh & (di & 0x40) << 1
            #d[i] = (byte)di
            d[i] = packl_ctypes(di)


        di = ((nvh & (di & 0x80) << 1) ^ vi) >> 8

        # initialize state
        set(yx[0], 1)
        cpy(yx[1], p[di])
        cpy(yx[2], s[0])
        set(yz[0], 0)
        set(yz[1], 1)
        set(yz[2], 1)

        """ 
        y[0] is (even)P + (even)G
            y[1] is (even)P + (odd)G  if current d-bit is 0
            y[1] is (odd)P + (even)G  if current d-bit is 1
            y[2] is (odd)P + (odd)G
        """

        vi = 0
        hi = 0

        # and go for it!
        for i in range(31, -1, -1):
            vi = (vi << 8) | (v[i] & 0xFF)
            hi = (hi << 8) | (h[i] & 0xFF)
            di = (di << 8) | (d[i] & 0xFF)

            for j in range(7,-1,-1):
                mont_prep(t1[0], t2[0], yx[0], yz[0])
                mont_prep(t1[1], t2[1], yx[1], yz[1])
                mont_prep(t1[2], t2[2], yx[2], yz[2])

                k = ((vi ^ vi >> 1) >> j & 1) + ((hi ^ hi >> 1) >> j & 1)
                mont_dbl(yx[2], yz[2], t1[k], t2[k], yx[0], yz[0])

                k = (di >> j & 2) ^ ((di >> j & 1) << 1)
                mont_add(t1[1], t2[1], t1[k], t2[k], yx[1], yz[1], p[di >> j & 1])

                mont_add(t1[2], t2[2], t1[0], t2[0], yx[2], yz[2], s[((vi ^ hi) >> j & 2) >> 1])

        k = (vi & 1) + (hi & 1)
        recip(t1[0], yz[k], 0)
        mul(t1[1], yx[k], t1[0])

        pack(t1[1], Y)
