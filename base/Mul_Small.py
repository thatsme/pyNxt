
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

        self.xy = xy
        self.x = x
        self.y = y
        self.t = None

        self.run()

    def run(self):
        self.t = (self.x._8 * self.y)
        self.xy._8 = (self.t & ((1 << 26) - 1))
        self.t = (self.t >> 26) + (self.x._9 * self.y)
        self.xy._9 = (self.t & ((1 << 25) - 1))
        self.t = 19 * (self.t >> 25) + (self.x._0 * self.y)
        self.xy._0 = (self.t & ((1 << 26) - 1))
        self.t = (self.t >> 26) + (self.x._1 * self.y)
        self.xy._1 = (self.t & ((1 << 25) - 1))
        self.t = (self.t >> 25) + (self.x._2 * self.y)
        self.xy._2 = (self.t & ((1 << 26) - 1))
        self.t = (self.t >> 26) + (self.x._3 * self.y)
        self.xy._3 = (self.t & ((1 << 25) - 1))
        self.t = (self.t >> 25) + (self.x._4 * self.y)
        self.xy._4 = (self.t & ((1 << 26) - 1))
        self.t = (self.t >> 26) + (self.x._5 * self.y)
        self.xy._5 = (self.t & ((1 << 25) - 1))
        self.t = (self.t >> 25) + (self.x._6 * self.y)
        self.xy._6 = (self.t & ((1 << 26) - 1))
        self.t = (self.t >> 26) + (self.x._7 * self.y)
        self.xy._7 = (self.t & ((1 << 25) - 1))
        self.t = (self.t >> 25) + self.xy._8
        self.xy._8 = (self.t & ((1 << 26) - 1))
        self.xy._9 += (self.t >> 26)

        return self.xy;