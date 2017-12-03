from base.Long10 import Long10 as Long10
from base.Mul import Mul as mul
from base.Sqr import Sqr as sqr

class Recip(object):

    def __init__(self, y, x, sqrtassist):
        """
        Calculates a reciprocal.  The output is in reduced form, the inputs need notbe.
        Simply calculates  y = x^(p-2)  so it's not too fast.
        When sqrtassist is true, it instead calculates y = x^((p-5)/8)

        :param y: Long10
        :param x: Long10
        :param sqrtassist: int

        """
        print("Recip")

        t0 = Long10()
        t1 = Long10()
        t2 = Long10()
        t3 = Long10()
        t4 = Long10()
        i = 0

        """/ *the chain for x ^ (2 ^ 255 - 21) is straight from djb's implementation */ """
        temp = t1
        sqr(t1, x)                          # 2 == 2 * 1
        print(temp == t1)
        sqr(t2, t1)                         # 4 == 2 * 2
        sqr(t0, t2)                         # 8 == 2 * 4
        mul(t2, t0, x)                      # 9 == 8 + 1
        mul(t0, t2, t1)                     # 11 == 9 + 2
        sqr(t1, t0)                         # 22 == 2 * 11
        mul(t3, t1, t2)                     # 31 == 22 + 9 == 2 ^ 5 - 2 ^ 0

        sqr(t1, t3)                         # 2 ^ 6 - 2 ^ 1
        sqr(t2, t1)                         # 2 ^ 7 - 2 ^ 2 * /
        sqr(t1, t2)                         # 2 ^ 8 - 2 ^ 3 * /
        sqr(t2, t1)                         # 2 ^ 9 - 2 ^ 4 * /
        sqr(t1, t2)                         # 2 ^ 10 - 2 ^ 5 * /
        mul(t2, t1, t3)                     # 2 ^ 10 - 2 ^ 0 * /
        sqr(t1, t2)                         # 2 ^ 11 - 2 ^ 1 * /
        sqr(t3, t1)                         # 2 ^ 12 - 2 ^ 2 * /

        for i in range(5):
            sqr(t1, t3)
            sqr(t3, t1)
                                            # t3 * / / * 2 ^ 20  - 2 ^ 10

        mul(t1, t3, t2)                     # 2 ^ 20 - 2 ^ 0
        sqr(t3, t1)                         # 2 ^ 21 - 2 ^ 1
        sqr(t4, t3)                         # 2 ^ 22 - 2 ^ 2

        for i in range(10):
            sqr(t3, t4)
            sqr(t4, t3)
                                            # t4 * / / * 2 ^ 40  - 2 ^ 20

        mul(t3, t4, t1)                     # 2 ^ 40 - 2 ^ 0

        for i in range(5):
            sqr(t1, t3)
            sqr(t3, t1)
                                            # t3 * / / * 2 ^ 50  - 2 ^ 10

        mul(t1, t3, t2)                     # 2 ^ 50 - 2 ^ 0
        sqr(t2, t1)                         # 2 ^ 51 - 2 ^ 1
        sqr(t3, t2)                         # 2 ^ 52 - 2 ^ 2

        for i in range(25):
            sqr(t2, t3)
            sqr(t3, t2)
                                            # t3 * / / * 2 ^ 100 - 2 ^ 50

        mul(t2, t3, t1)                     # 2 ^ 100 - 2 ^ 0
        sqr(t3, t2)                         # 2 ^ 101 - 2 ^ 1
        sqr(t4, t3)                         # 2 ^ 102 - 2 ^ 2

        for i in range(50):
            sqr(t3, t4)
            sqr(t4, t3)
                                            # t4 * / / * 2 ^ 200 - 2 ^ 100

        mul(t3, t4, t2)                     # 2 ^ 200 - 2 ^ 0

        for i in range(25):
            sqr(t4, t3)
            sqr(t3, t4)
                                            # t3 * / / * 2 ^ 250 - 2 ^ 50

        mul(t2, t3, t1)                     # 2 ^ 250 - 2 ^ 0
        sqr(t1, t2)                         # 2 ^ 251 - 2 ^ 1
        sqr(t2, t1)                         # 2 ^ 252 - 2 ^ 2

        if (sqrtassist != 0):
            mul(y, x, t2)                   # 2 ^ 252 - 3
        else:
            sqr(t1, t2)                     # 2 ^ 253 - 2 ^ 3
            sqr(t2, t1)                     # 2 ^ 254 - 2 ^ 4
            sqr(t1, t2)                     # 2 ^ 255 - 2 ^ 5
            mul(y, t1, t0)                  # 2 ^ 255 - 21


