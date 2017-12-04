from curve25519.Mula_Small import Mula_Small as mula_small
from curve25519.Packl_ctypes import Packl_ctypes as packl_ctypes

class Mula32(object):

    def __init__(self, p, x, y, t, z):
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
            w += mula_small(p, p, i, x, n, zy).value + (p[i+n] & 0xFF) + zy * (x[n] & 0xFF)
            p[i+n] = packl_ctypes(w).value
            w >>= 8

        p[i + n] = packl_ctypes((w + (p[i + n] & 0xFF)))

        self.value = w >> 8

        # print("Mula32 w", self.value)

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)
