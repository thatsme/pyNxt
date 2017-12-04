import curve25519.Cpy32 as cpy32
import curve25519.Divmod as divmod
import curve25519.Mula_Small as mula_small
import curve25519.Mula32 as mula32

class Sign(object):

    def __init__(self,  v,  h,  x,  s):
        """

        :param v: byte[]
        :param h: byte[]
        :param x: byte[]
        :param s: byte[]
        """

        self.v = v
        self.h = h
        self.x = x
        self.x = x

        ORDER = bytearray()
        ORDER.append(bytes(237))
        ORDER.append(bytes(211))
        ORDER.append(bytes(245))
        ORDER.append(bytes(92))
        ORDER.append(bytes(26))
        ORDER.append(bytes(99))
        ORDER.append(bytes(18))
        ORDER.append(bytes(88))
        ORDER.append(bytes(214))
        ORDER.append(bytes(156))
        ORDER.append(bytes(247))
        ORDER.append(bytes(162))
        ORDER.append(bytes(222))
        ORDER.append(bytes(249))
        ORDER.append(bytes(222))
        ORDER.append(bytes(20))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(0))
        ORDER.append(bytes(16))

        self.h1 = bytearray()
        self.x1 = bytearray()
        self.tmp3 = bytearray()

        for i in range(32):
            self.h1.append(0x00)
            self.x1.append(0x00)
            self.tmp3.append(0x00)

        self.tmp1 = bytearray()
        self.tmp2 = bytearray()

        for i in range(64):
            self.tmp1.append(0x00)
            self.tmp2.append(0x00)

    def run(self):
        cpy32(self.h1, self.h)
        cpy32(self.x1, self.x)


        divmod(self.tmp3, self.h1, 32, self.ORDER, 32)
        divmod(self.tmp3, self.x1, 32, self.ORDER, 32)

        mula_small(self.v, self.x1, 0, self.h1, 32, -1);
        mula_small(self.v, self.v , 0, self.ORDER, 32, 1);

        #// tmp1 = (x-h)*s mod q
        mula32(self.tmp1, self.v, self.s, 32, 1);
        divmod(self.tmp2, self.tmp1, 64, self.ORDER, 32);

        w = 0
        for i in range(32):
            self.v[i] = self.tmp1[i]
            w |= self.v[i]

        return w != 0