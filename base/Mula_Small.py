

class Mula_Small(object):

    def __init__(self, p, q, m,  x, n, z):

        """

        :param p: bite[]
        :param q: bite[]
        :param m: int
        :param x: bite[]
        :param n: int
        :param z: int
        """
        self.value = 0
        v = 0
        for i in range(n):
            v+= (q[i+m] & 0xFF) + (z * (x[i] & 0xFF))
            p[i+m] = v
            v >>= 8

        # print("Mula_small, v", v)
        self.value =  v

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)

