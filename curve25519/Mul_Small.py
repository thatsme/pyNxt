from curve25519.Long10 import Long10 as Long10

class Mul_Small(object):

    def __init__(self, xy, x, y):
        """
        Multiply a number by a small integer in range -185861411 .. 185861411.
        The output is in reduced form, the input x need not be.  x and xy may point
        to the same buffer.
        :param xy: Long10
        :param x: Long10
        :param y: long
        """
        if isinstance(xy, Long10):

            t = (x._8 * y)
            xy._8 = (t & ((1 << 26) - 1))
            t = (t >> 26) + (x._9 * y)
            xy._9 = (t & ((1 << 25) - 1))
            t = 19 * (t >> 25) + (x._0 * y)
            xy._0 = (t & ((1 << 26) - 1))
            t = (t >> 26) + (x._1 * y)
            xy._1 = (t & ((1 << 25) - 1))
            t = (t >> 25) + (x._2 * y)
            xy._2 = (t & ((1 << 26) - 1))
            t = (t >> 26) + (x._3 * y)
            xy._3 = (t & ((1 << 25) - 1))
            t = (t >> 25) + (x._4 * y)
            xy._4 = (t & ((1 << 26) - 1))
            t = (t >> 26) + (x._5 * y)
            xy._5 = (t & ((1 << 25) - 1))
            t = (t >> 25) + (x._6 * y)
            xy._6 = (t & ((1 << 26) - 1))
            t = (t >> 26) + (x._7 * y)
            xy._7 = (t & ((1 << 25) - 1))
            t = (t >> 25) + xy._8
            xy._8 = (t & ((1 << 26) - 1))
            xy._9 += (t >> 26)

