from base.Long10 import Long10
import base.Unpack as unpack
import base.Set as set
import base.Cpy as cpy
import base.Mont_Prep as mont_prep
import base.Mont_Dbl as mont_dbl
import base.Mont_Add as mont_add
import base.Recip as recip
import base.Mul as mul
import base.Pack as pack
import base.X_to_Y2 as x_to_y2
import base.Add as add
import base.Sqr as sqr
import base.Sub as sub
import base.Mula_Small as mula_small
import base.Cpy32 as cpy32

class Core(object):

    def __init__(self, Px, s, k, Gx):

        """

        :param Px: bite[]
        :param s: bite[]
        :param k: bite[]
        :param Gx: bite[]


        """
        dx = Long10()
        t1 = Long10()
        t2 = Long10()
        t3 = Long10()
        t4 = Long10()


        x = [Long10(),Long10()]
        z = [Long10(),Long10()]

        i=0
        j=0

        # unpack the base
        if (Gx != None):
            unpack(dx, Gx)
        else:
            set(dx, 9)

        # 0G = point-at-infinity
        set(x[0], 1)
        set(z[0], 0)

        # 1G = G
        cpy(x[1], dx)
        set(z[1], 1)

        range(10, 0, -1)

        for i in range(32, 0, -1):
            if (i == 0):
                i=0;

            for j in range(8,0,-1):
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
            byte[] temp1=new byte[32];
            byte[] temp2=new byte[64];
            byte[] temp3=new byte[64];
            cpy32(temp1, ORDER);
            cpy32(s, egcd32(temp2, temp3, s, temp1))
            if (s[31] & 0x80) != 0:
                mula_small(s, s, 0, ORDER, 32, 1)

