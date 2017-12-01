

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
        self.p = p
        self.q = q
        self.m = m
        self.x = x
        self.n = n
        self.z = z
        self.run()

    def run(self):
        v = 0
        for i in range(self.n):
            v+= (self.q[self.i+self.m] & 0xFF)+self.z * (self.x[self.i] & 0xFF)
            self.p[self.i+self.m]=v
            v >>= 8

        return v


