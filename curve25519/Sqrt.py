from curve25519.Long10 import Long10 as Long10
from curve25519.Add import Add as add
from curve25519.Recip import Recip as recip
from curve25519.Sqr import Sqr as sqr
from curve25519.Mul import Mul as mul

class Sqrt(object):

    def __init__(self, x, u):
        """
        a square root

        :param x: Long10
        :param u: Long10
        :return:
        """

        v = Long10()
        t1 = Long10()
        t2 = Long10()

        add(t1, u, u)	            # t1 = 2u
        recip(v, t1, 1)	            # v = (2u)^((p-5)/8)
        sqr(x, v)		            # x = v^2
        mul(t2, t1, x)	            # t2 = 2uv^2
        print(t2.printAll())
        t2._0 = t2._0 -1 		    # t2 = 2uv^2-1
        print(t2.printAll())
        mul(t1, v, t2)	            # t1 = v(2uv^2-1)
        mul(x, u, t1)	            # x = uv(2uv^2-1)
