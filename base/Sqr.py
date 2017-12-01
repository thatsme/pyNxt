

class Sqr(object):

    def __init__(self, x2, x):

        """
        Square a number.  Optimization of  mul25519(x2, x, x)

        :param x2:
        :param x:
        """
        self.x_0 = x._0
        self.x_1 = x._1
        self.x_2 = x._2
        self.x_3 = x._3
        self.x_4 = x._4
        self.x_5 = x._5
        self.x_6 = x._6
        self.x_7 = x._7
        self.x_8 = x._8
        self.x_9 = x._9

        self.x2 = x2
        self.t = 0
        self.run()
        
    def run(self):
        self.t = (self.x_4 * self.x_4) + 2 * ((self.x_0 * self.x_8) + (self.x_2 * self.x_6)) + 38 * (self.x_9 * self.x_9) + 4 * ((self.x_1 * self.x_7) + (self.x_3 * self.x_5))
        self.x2._8 = (self.t & ((1 << 26) - 1))

        self.t = (self.t >> 26) + 2 * ((self.x_0 * self.x_9) + (self.x_1 * self.x_8) + (self.x_2 * self.x_7) + (self.x_3 * self.x_6) + (self.x_4 * self.x_5))
        self.x2._9 = (self.t & ((1 << 25) - 1))

        self.t = 19 * (self.t >> 25) + (self.x_0 * self.x_0) + 38 * ((self.x_2 * self.x_8) + (self.x_4 * self.x_6) + (self.x_5 * self.x_5)) + 76 * ((self.x_1 * self.x_9) + (self.x_3 * self.x_7))
        self.x2._0 = (self.t & ((1 << 26) - 1))

        self.t = (self.t >> 26) + 2 * (self.x_0 * self.x_1) + 38 * ((self.x_2 * self.x_9) + (self.x_3 * self.x_8) + (self.x_4 * self.x_7) + (self.x_5 * self.x_6))
        self.x2._1 = (self.t & ((1 << 25) - 1))

        self.t = (self.t >> 25) + 19 * (self.x_6 * self.x_6) + 2 * ((self.x_0 * self.x_2) + (self.x_1 * self.x_1)) + 38 * (self.x_4 * self.x_8) + 76 * ((self.x_3 * self.x_9) + (self.x_5 * self.x_7))
        self.x2._2 = (self.t & ((1 << 26) - 1))

        self.t = (self.t >> 26) + 2 * ((self.x_0 * self.x_3) + (self.x_1 * self.x_2)) + 38 * ((self.x_4 * self.x_9) + (self.x_5 * self.x_8) + (self.x_6 * self.x_7))
        self.x2._3 = (self.t & ((1 << 25) - 1))

        self.t = (self.t >> 25) + (self.x_2 * self.x_2) + 2 * (self.x_0 * self.x_4) + 38 * ((self.x_6 * self.x_8) + (self.x_7 * self.x_7)) + 4 * (self.x_1 * self.x_3) + 76 * (self.x_5 * self.x_9)
        self.x2._4 = (self.t & ((1 << 26) - 1))

        self.t = (self.t >> 26) + 2 * ((self.x_0 * self.x_5) + (self.x_1 * self.x_4) + (self.x_2 * self.x_3)) + 38 * ((self.x_6 * self.x_9) + (self.x_7 * self.x_8))
        self.x2._5 = (self.t & ((1 << 25) - 1))

        self.t = (self.t >> 25) + 19 * (self.x_8 * self.x_8) + 2 * ((self.x_0 * self.x_6) + (self.x_2 * self.x_4) + (self.x_3 * self.x_3)) + 4 * (self.x_1 * self.x_5) + 76 * (self.x_7 * self.x_9)
        self.x2._6 = (self.t & ((1 << 26) - 1))

        self.t = (self.t >> 26) + 2 * ((self.x_0 * self.x_7) + (self.x_1 * self.x_6) + (self.x_2 * self.x_5) + (self.x_3 * self.x_4)) + 38 * (self.x_8 * self.x_9)
        self.x2._7 = (self.t & ((1 << 25) - 1))

        self.t = (self.t >> 25) + self.x2._8
        self.x2._8 = (self.t & ((1 << 26) - 1))
        self.x2._9 += (self.t >> 26)

        return self.x2