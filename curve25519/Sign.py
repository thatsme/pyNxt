import curve25519.Cpy32 as cpy32
import curve25519.Divmod as divmod
import curve25519.Mula_Small as mula_small
import curve25519.Mula32 as mula32
import curve25519.Packl_ctypes as packl_ctypes

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

        ORDER = [] * 32
        ORDER.append(packl_ctypes(237))
        ORDER.append(packl_ctypes(211))
        ORDER.append(packl_ctypes(245))
        ORDER.append(packl_ctypes(92))
        ORDER.append(packl_ctypes(26))
        ORDER.append(packl_ctypes(99))
        ORDER.append(packl_ctypes(18))
        ORDER.append(packl_ctypes(88))
        ORDER.append(packl_ctypes(214))
        ORDER.append(packl_ctypes(156))
        ORDER.append(packl_ctypes(247))
        ORDER.append(packl_ctypes(162))
        ORDER.append(packl_ctypes(222))
        ORDER.append(packl_ctypes(249))
        ORDER.append(packl_ctypes(222))
        ORDER.append(packl_ctypes(20))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(0))
        ORDER.append(packl_ctypes(16))

        self.h1 = [0] * 32
        self.x1 = [0] * 32
        self.tmp3 = [0] * 32

        self.tmp1 = [0] * 64
        self.tmp2 = [0] * 64

        self.run()

    def run(self):
        
        cpy32(self.h1, self.h)
        cpy32(self.x1, self.x)


        divmod(self.tmp3, self.h1, 32, self.ORDER, 32)
        divmod(self.tmp3, self.x1, 32, self.ORDER, 32)

        mula_small(self.v, self.x1, 0, self.h1, 32, -1, False);
        mula_small(self.v, self.v , 0, self.ORDER, 32, 1, False);

        #// tmp1 = (x-h)*s mod q
        mula32(self.tmp1, self.v, self.s, 32, 1, False);
        divmod(self.tmp2, self.tmp1, 64, self.ORDER, 32);

        w = 0
        for i in range(32):
            self.v[i] = self.tmp1[i]
            w |= self.v[i]

        return w != 0