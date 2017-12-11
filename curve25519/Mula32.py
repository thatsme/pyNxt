from curve25519.Mula_Small import Mula_Small as mula_small
from curve25519.Packl_ctypes import Packl_ctypes as packl_ctypes
from curve25519.ToHexString import ToHexString as ToHexString

class Mula32(object):

    def __init__(self, p, x, y, t, z, MDEBUG = False):
        """

        :param p: list[]
        :param x: list[]
        :param y: list[]
        :param t: int
        :param z: int
        :return:
        """
        n = 31
        w = 0
        i = 0
        zy = None

        self.value = 0

        for i in range(t):
            zy = z * (y[i] & 0xFF)
            w += mula_small(p, p, i, x, n, zy, False).value + (p[i+n] & 0xFF) + zy * (x[n] & 0xFF)
            ## print("w, and packl_ctypes w ", w, packl_ctypes(w).value, type(w), type(packl_ctypes(w).value))
            p[i+n] = packl_ctypes(w).value
            w >>= 8

        ## Porc .... fck java
        i += 1
        ##
        p[i + n] = packl_ctypes((w + (p[i + n] & 0xFF))).value
        if MDEBUG:
            print(i,t,"               |_|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|_|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")
            print(i,t," msma --> (p) ", ToHexString(p).getString())

        self.value = w >> 8

        # print("Mula32 w", self.value)

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)
