from base.Long10 import Long10

class Is_Overflow(object):

    def __init__(self, x):
        P25 = 33554431
        P26 = 67108863

        if isinstance(x, Long10):
            return (((x._0 > P26-19)) && ((x._1 & x._3 & x._5 & x._7 & x._9) == P25) && ((x._2 & x._4 & x._6 & x._8) == P26)) || (x._9 > P25)