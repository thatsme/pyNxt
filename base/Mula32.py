import base.Mula_Small as mula_small

class Mula32(object):

    def __ini__(self, p, x, y, t, z):
        """

        :param p: bite[]
        :param x: bite[]
        :param y: bite[]
        :param t: int
        :param z: int
        :return:
        """
        self.n = 31
        self.w = 0
        self.i = 0
        self.p = p
        self.x = x
        self.y = y
        self.t = t
        self.z = z

    def run(self):
        for self.i in range(self.t):
            zy = self.z * (self.y[self.i] & 0xFF);
            self.w += mula_small(self.p, self.p, self.i, self.x, self.n, zy) + (self.p[self.i+self.n] & 0xFF) + zy * (self.x[self.n] & 0xFF)
            self.p[self.i+self.n] = self.w
            self.w >>= 8

        self.p[self.i + self.n] = (self.w + (self.p[self.i + sefl.n] & 0xFF))

        return self.w >> 8