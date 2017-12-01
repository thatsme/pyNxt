import base.Mula32 as mula32
import base.Numsize as numsize
import base.Divmod as divmod

class Egcd32(object):

    def __init__(self, x, y, a, b):
        """

        :param x: bite[]
        :param y: bite[]
        :param a: bite[]
        :param b: bite[]
        """

        an, bn = 32
        qn, i = 0

        for i in range(32):
            x[i] = y[i] = 0;


        x[0] = 1
        an = numsize(a, 32);

        if an is 0:
            return y;               #division by zero * /

        temp = bytes([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
        while (True):
            qn = bn - an + 1
            divmod(temp, b, bn, a, an)
            bn = numsize(b, bn)
            if bn == 0:
                return x

            mula32(y, x, temp, qn, -1)

            qn = an - bn + 1
            divmod(temp, a, an, b, bn)
            an = numsize(a, an)

            if an == 0:
                return y

            mula32(x, y, temp, qn, -1)



