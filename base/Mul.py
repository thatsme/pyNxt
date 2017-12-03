

class Mul(object):

    def __init__(self, xy, x,  y):
        """
        Multiply two numbers.  The output is in reduced form, the inputs need not be.

        :param xy:
        :param x:
        :param y:
        """
        self.xy = xy
        self.x = x
        self.y = y

        self.x_0 =x._0
        self.x_1 =x._1
        self.x_2 =x._2
        self.x_3 =x._3
        self.x_4 =x._4
        self.x_5 =x._5
        self.x_6 =x._6
        self.x_7 =x._7
        self.x_8 =x._8
        self.x_9 =x._9
        self.y_0 =y._0
        self.y_1 =y._1
        self.y_2 =y._2
        self.y_3 =y._3
        self.y_4 =y._4
        self.y_5 =y._5
        self.y_6 =y._6
        self.y_7 =y._7
        self.y_8 =y._8
        self.y_9 =y._9

        self.t = 0

        self.t = (self.x_0 * self.y_8) + (self.x_2 * self.y_6) + (self.x_4 * self.y_4) + (self.x_6 * self.y_2) + (self.x_8 * self.y_0) + 2 * ((self.x_1 * self.y_7) + (self.x_3 * self.y_5) + (self.x_5 * self.y_3) + (self.x_7 * self.y_1)) + 38 * (self.x_9 * self.y_9)
        xy._8 = (self.t & ((1 << 26) - 1))

        self.t = (self.t >> 26) + (self.x_0 * self.y_9) + (self.x_1 * self.y_8) + (self.x_2 * self.y_7) + (self.x_3 * self.y_6) + (self.x_4 * self.y_5) + (self.x_5 * self.y_4) + (self.x_6 * self.y_3) + (self.x_7 * self.y_2) + (self.x_8 * self.y_1) + (self.x_9 * self.y_0)
        xy._9 = (self.t & ((1 << 25) - 1))

        self.t = (self.x_0 * self.y_0) + 19 * ((self.t >> 25) + (self.x_2 * self.y_8) + (self.x_4 * self.y_6) + (self.x_6 * self.y_4) + (self.x_8 * self.y_2)) + 38 * ((self.x_1 * self.y_9) + (self.x_3 * self.y_7) + (self.x_5 * self.y_5) + (self.x_7 * self.y_3) + (self.x_9 * self.y_1))
        xy._0 = (self.t & ((1 << 26) - 1))

        self.t = (self.t >> 26) + (self.x_0 * self.y_1) + (self.x_1 * self.y_0) + 19 * ((self.x_2 * self.y_9) + (self.x_3 * self.y_8) + (self.x_4 * self.y_7) + (self.x_5 * self.y_6) + (self.x_6 * self.y_5) + (self.x_7 * self.y_4) + (self.x_8 * self.y_3) + (self.x_9 * self.y_2))
        xy._1 = (self.t & ((1 << 25) - 1))

        self.t = (self.t >> 25) + (self.x_0 * self.y_2) + (self.x_2 * self.y_0) + 19 * ((self.x_4 * self.y_8) + (self.x_6 * self.y_6) + (self.x_8 * self.y_4)) + 2 * (self.x_1 * self.y_1) + 38 * ((self.x_3 * self.y_9) + (self.x_5 * self.y_7) + (self.x_7 * self.y_5) + (self.x_9 * self.y_3))
        xy._2 = (self.t & ((1 << 26) - 1))

        self.t = (self.t >> 26) + (self.x_0 * self.y_3) + (self.x_1 * self.y_2) + (self.x_2 * self.y_1) + (self.x_3 * self.y_0) + 19 * ((self.x_4 * self.y_9) + (self.x_5 * self.y_8) + (self.x_6 * self.y_7) + (self.x_7 * self.y_6) + (self.x_8 * self.y_5) + (self.x_9 * self.y_4))
        xy._3 = (self.t & ((1 << 25) - 1))

        self.t = (self.t >> 25) + (self.x_0 * self.y_4) + (self.x_2 * self.y_2) + (self.x_4 * self.y_0) + 19 * ((self.x_6 * self.y_8) + (self.x_8 * self.y_6)) + 2 * ((self.x_1 * self.y_3) +(self.x_3 * self.y_1)) + 38 * ((self.x_5 * self.y_9) + (self.x_7 * self.y_7) + (self.x_9 * self.y_5))
        xy._4 = (self.t & ((1 << 26) - 1))

        self.t = (self.t >> 26) + (self.x_0 * self.y_5) + (self.x_1 * self.y_4) + (self.x_2 * self.y_3) + (self.x_3 * self.y_2) + (self.x_4 * self.y_1) + (self.x_5 * self.y_0) + 19 * ((self.x_6 * self.y_9) + (self.x_7 * self.y_8) + (self.x_8 * self.y_7) + (self.x_9 * self.y_6))
        xy._5 = (self.t & ((1 << 25) - 1))

        self.t = (self.t >> 25) + (self.x_0 * self.y_6) + (self.x_2 * self.y_4) + (self.x_4 * self.y_2) + (self.x_6 * self.y_0) + 19 * (self.x_8 * self.y_8) + 2 * ((self.x_1 * self.y_5) + (self.x_3 * self.y_3) + (self.x_5 * self.y_1)) + 38 * ((self.x_7 * self.y_9) + (self.x_9 * self.y_7))
        xy._6 = (self.t & ((1 << 26) - 1))

        self.t = (self.t >> 26) + (self.x_0 * self.y_7) + (self.x_1 * self.y_6) + (self.x_2 * self.y_5) + (self.x_3 * self.y_4) + (self.x_4 * self.y_3) + (self.x_5 * self.y_2) + (self.x_6 * self.y_1) + (self.x_7 * self.y_0) + 19 * ((self.x_8 * self.y_9) + (self.x_9 * self.y_8))
        xy._7 = (self.t & ((1 << 25) - 1))

        self.t = (self.t >> 25) + xy._8
        xy._8 = (self.t & ((1 << 26) - 1))
        xy._9 += (self.t >> 26)

        #return xy