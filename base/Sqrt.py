from base.Long10 import Long10
import base.Add as add
import base.Recip as recip
import base.Sqr as sqr
import base.Mul as mul

class Sqrt(object):

    def __init_(self, x, u):
        """
        a square root

        :param x:
        :param u:
        :return:
        """

        v = Long10()
        t1 = Long10()
        t2 = Long10()
        add(t1, u, u)	            # t1 = 2u
        recip(v, t1, 1)	            # v = (2u)^((p-5)/8)
        sqr(x, v)		            # x = v^2
        mul(t2, t1, x)	            # t2 = 2uv^2
        t2._0 =- t2._0		        # t2 = 2uv^2-1
        mul(t1, v, t2)	            # t1 = v(2uv^2-1)
        mul(x, u, t1)	            # x = uv(2uv^2-1)
