from base.Sqr import Sqr as sqr
from base.Mul_Small import Mul_Small as mul_small
from base.Add import Add as add
from base.Mul import Mul as mul

class X_to_Y2(object):

    def __init__(self, t, y2, x):
        """
        Y^2 = X^3 + 486662 X^2 + X
        t is a temporary

        :param t: Long10
        :param y2: Long10
        :param x: Long10
        """

        sqr(t, x)
        mul_small(y2, x, 486662)
        add(t, t, y2)
        #print("before",t._0)
        t._0 = t._0 + 1
        #print("after",t._0)
        mul(y2, t, x)

