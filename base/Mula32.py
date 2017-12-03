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
        n = 31
        w = 0
        i = 0
        zy = None

        self.value = 0

        for i in range(t):
            zy = z * (y[i] & 0xFF)
            w += mula_small(p, p, i, x, n, zy).value + (p[i+n] & 0xFF) + zy * (x[n] & 0xFF)
            p[i+n] = w
            w >>= 8

        p[i + n] = (w + (p[i + n] & 0xFF))

        self.value = w >> 8

        print("Mula32 w", self.value)

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)
