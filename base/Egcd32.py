from base.Mula32 import Mula32 as mula32
from base.Numsize import Numsize as numsize
from base.Divmod import Divmod as divmod

class Egcd32(object):

    def __init__(self, x, y, a, b):
        """

        :param x: bite[]
        :param y: bite[]
        :param a: bite[]
        :param b: bite[]
        """

        self.an = 32
        self.bn = 32
        self.qn = 0
        self.i = 0
        self.x = x
        self.y = y
        self.a = a
        self.b = b

        self.run()

    def run(self):
        i = 0
        for i in range(32):
            self.x[i] = self.y[i] = 0;


        self.x[0] = 1
        self.an = numsize(self.a, 32);

        if self.an is 0:
            return self.y;               #division by zero * /

        temp = bytes([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
        while (True):
            print("gira ....")
            self.qn = self.bn - self.an + 1
            divmod(temp, self.b, self.bn, self.a, self.an)
            self.bn = numsize(self.b, self.bn)
            if self.bn == 0:
                return self.x

            mula32(self.y, self.x, temp, self.qn, -1)

            self.qn = self.an - self.bn + 1
            divmod(temp, self.a, self.an, self.b, self.bn)
            an = numsize(self.a, self.an)

            if self.an == 0:
                return self.y

            mula32(self.x, self.y, temp, self.qn, -1)



