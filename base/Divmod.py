from base.Mula_Small import Mula_Small as mula_small

class Divmod(object):

    def __init__(self, q,  r,  n, d,  t):
        """

        :param q: bite[]
        :param r: bite[]
        :param n: int
        :param d:bite[]
        :param t: int
        """

        rn = 0
        dt = 0
        t1 = t-1
        t2 = t-2

        dt = ((d[t1] & 0xFF) << 8)

        if (t > 1):
            dt |= (d[(t2)] & 0xFF)


        for u in range(n, t, 1):
            print("gira divmod ...")
            z = (rn << 16) | ((r[u] & 0xFF) << 8)
            if (u > 0):
                z |= (r[u-1] & 0xFF)

            z /= dt;
            rn += mula_small(r, r, u-t+1, d, t, -z).value

            q[u-t+1] = ((z + rn) & 0xFF)             # rn is 0 or -1 (underflow)
            mula_small(r, r, u-t+1, d, t, -rn)
            rn = (r[u] & 0xFF)
            r[u] = 0


        r[t - 1] = rn

