from curve25519.Mula32 import Mula32 as mula32
from curve25519.Numsize import Numsize as numsize
from curve25519.Divmod import Divmod as divmod

class Egcd32(object):

    def __init__(self, x, y, a, b):
        """

        :param x: list[]
        :param y: list[]
        :param a: list[]
        :param b: list[]
        """

        an = 0
        bn = 32
        qn = 0
        i = 0
        #self.x = x
        #self.y = y
        #self.a = a
        #self.b = b
        self.value = None

        for i in range(32):
            x[i] = 0
            y[i] = 0


        x[0] = 1
        an = numsize(a, 32).value

        if an is 0:
            self.value = y               #division by zero * /
        else:
            temp = [0] * 32
            while (True):
                # print("gira ....")
                qn = bn - an + 1
                divmod(temp, b, bn, a, an)
                bn = numsize(b, bn).value
                if bn == 0:
                    self.value = x
                    break
                    #return self.x

                mula32(y, x, temp, qn, -1)

                qn = an - bn + 1
                divmod(temp, a, an, b, bn)
                an = numsize(a, an).value

                if an == 0:
                    self.value = y
                    break
                    #return self.y

                mula32(x, y, temp, qn, -1)

            print("bhe .. ")

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)

