from curve25519.Packl_ctypes import Packl_ctypes as packl_ctypes

class Mula_Small(object):

    def __init__(self, p, q, m,  x, n, z):

        """

        :param p: list[]
        :param q: list[]
        :param m: int
        :param x: list[]
        :param n: int
        :param z: int
        """
        self.value = 0
        v = 0
        for i in range(n):
            v+= (q[i+m] & 0xFF) + (z * (x[i] & 0xFF))

            ## Magari dobbiamo paccarlo ???
            p[i+m] = packl_ctypes(v).value
            v >>= 8

        # print("Mula_small, v", v)
        self.value =  v

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)

