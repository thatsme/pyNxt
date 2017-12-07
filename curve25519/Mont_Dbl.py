from curve25519.Sqr import Sqr as sqr
from curve25519.Mul import Mul as mul
from curve25519.Sub import Sub as sub
from curve25519.Mul_Small import Mul_Small as mul_small
from curve25519.Add import Add as add
from curve25519.Long10 import Long10 as Long10

class Mont_Dbl(object):

    def __init__(self, t1, t2, t3, t4, bx, bz):

        """
        B = 2 * Q   where
        X(B) = bx/bz
        X(Q) = (t3+t4)/(t3-t4)
        clobbers t1 and t2, preserves t3 and t4

        :param t1: Long10
        :param t2: Long10
        :param t3: Long10
        :param t4: Long10
        :param bx: Long10
        :param bz: Long10
        """
        #print("Mont_Dbl")
        if isinstance(t1, Long10) and isinstance(t2, Long10) and isinstance(t3, Long10) and isinstance(t4, Long10) and isinstance(bx, Long10) and isinstance(bz, Long10):

            sqr(t1, t3)
            sqr(t2, t4)
            mul(bx, t1, t2)
            sub(t2, t1, t2)
            mul_small(bz, t2, 121665)
            add(t1, t1, bz)
            mul(bz, t1, t2)

