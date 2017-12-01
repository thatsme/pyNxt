import base.Long10 as Long10

class Add(object):

    def __init__(self, xy, x, y):
        """
        Add/subtract two numbers.  The inputs must be in reduced form, and the
        output isn't, so to do another addition or subtraction on the output,
        first multiply it by one to reduce it.

        :param xy: Type Long10
        :param x:  Type Long10
        :param y:  Type Long10

        """
        xy._0 = x._0 + y._0
        xy._1 = x._1 + y._1
        xy._2 = x._2 + y._2
        xy._3 = x._3 + y._3
        xy._4 = x._4 + y._4
        xy._5 = x._5 + y._5
        xy._6 = x._6 + y._6
        xy._7 = x._7 + y._7
        xy._8 = x._8 + y._8
        xy._9 = x._9 + y._9

