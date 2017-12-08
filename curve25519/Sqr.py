from curve25519.Long10 import Long10 as Long10


class Sqr(object):

    def __init__(self, x2, x):

        """
        Square a number.  Optimization of  mul25519(x2, x, x)

        :param x2:
        :param x:
        """
        if isinstance(x2, Long10):

            x_0 = x._0
            x_1 = x._1
            x_2 = x._2
            x_3 = x._3
            x_4 = x._4
            x_5 = x._5
            x_6 = x._6
            x_7 = x._7
            x_8 = x._8
            x_9 = x._9

            t = 0

            t = (x_4 * x_4) + 2 * ((x_0 * x_8) + (x_2 * x_6)) + 38 * (x_9 * x_9) + 4 * ((x_1 * x_7) + (x_3 * x_5))
            x2._8 = (t & ((1 << 26) - 1))

            t = (t >> 26) + 2 * ((x_0 * x_9) + (x_1 * x_8) + (x_2 * x_7) + (x_3 * x_6) + (x_4 * x_5))
            x2._9 = (t & ((1 << 25) - 1))

            t = 19 * (t >> 25) + (x_0 * x_0) + 38 * ((x_2 * x_8) + (x_4 * x_6) + (x_5 * x_5)) + 76 * ((x_1 * x_9) + (x_3 * x_7))
            x2._0 = (t & ((1 << 26) - 1))

            t = (t >> 26) + 2 * (x_0 * x_1) + 38 * ((x_2 * x_9) + (x_3 * x_8) + (x_4 * x_7) + (x_5 * x_6))
            x2._1 = (t & ((1 << 25) - 1))

            t = (t >> 25) + 19 * (x_6 * x_6) + 2 * ((x_0 * x_2) + (x_1 * x_1)) + 38 * (x_4 * x_8) + 76 * ((x_3 * x_9) + (x_5 * x_7))
            x2._2 = (t & ((1 << 26) - 1))

            t = (t >> 26) + 2 * ((x_0 * x_3) + (x_1 * x_2)) + 38 * ((x_4 * x_9) + (x_5 * x_8) + (x_6 * x_7))
            x2._3 = (t & ((1 << 25) - 1))

            t = (t >> 25) + (x_2 * x_2) + 2 * (x_0 * x_4) + 38 * ((x_6 * x_8) + (x_7 * x_7)) + 4 * (x_1 * x_3) + 76 * (x_5 * x_9)
            x2._4 = (t & ((1 << 26) - 1))

            t = (t >> 26) + 2 * ((x_0 * x_5) + (x_1 * x_4) + (x_2 * x_3)) + 38 * ((x_6 * x_9) + (x_7 * x_8))
            x2._5 = (t & ((1 << 25) - 1))

            t = (t >> 25) + 19 * (x_8 * x_8) + 2 * ((x_0 * x_6) + (x_2 * x_4) + (x_3 * x_3)) + 4 * (x_1 * x_5) + 76 * (x_7 * x_9)
            x2._6 = (t & ((1 << 26) - 1))

            t = (t >> 26) + 2 * ((x_0 * x_7) + (x_1 * x_6) + (x_2 * x_5) + (x_3 * x_4)) + 38 * (x_8 * x_9)
            x2._7 = (t & ((1 << 25) - 1))

            t = (t >> 25) + x2._8
            x2._8 = (t & ((1 << 26) - 1))
            x2._9 += (t >> 26)
