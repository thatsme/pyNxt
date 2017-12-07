from curve25519.Long10 import Long10 as Long10

class Sub(object):

    def __init__(self, xy,x,y):
        """
        
        :param xy:
        :param x:
        :param y:
        """
        if isinstance(x, Long10) and isinstance(y, Long10) and isinstance(xy, Long10):
            xy._0 = x._0 - y._0
            xy._1 = x._1 - y._1
            xy._2 = x._2 - y._2
            xy._3 = x._3 - y._3
            xy._4 = x._4 - y._4
            xy._5 = x._5 - y._5
            xy._6 = x._6 - y._6
            xy._7 = x._7 - y._7
            xy._8 = x._8 - y._8
            xy._9 = x._9 - y._9
