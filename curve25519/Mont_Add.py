from curve25519.Mul import Mul as mul
from curve25519.Add import Add as add
from curve25519.Sub import Sub as sub
from curve25519.Sqr import Sqr as sqr
from curve25519.Long10 import Long10 as Long10

class Mont_Add(object):

    def __init__(self, t1, t2, t3, t4, ax, az, dx):

        """
        A = P + Q   where
        X(A) = ax/az
        X(P) = (t1+t2)/(t1-t2)
        X(Q) = (t3+t4)/(t3-t4)
        X(P-Q) = dx
        clobbers t1 and t2, preserves t3 and t4  */

        :param t1: Long10
        :param t2: Long10
        :param t3: Long10
        :param t4: Long10
        :param ax: Long10
        :param az: Long10
        :param dx: Long10
        """
        #print("Mont_Add")
        if isinstance(t1, Long10) and isinstance(t2, Long10) and isinstance(t3, Long10) and isinstance(t4, Long10) and isinstance(ax, Long10) and isinstance(az, Long10) and isinstance(dx, Long10):

            mul(ax, t2, t3)
            mul(az, t1, t4)
            add(t1, ax, az)
            sub(t2, ax, az)
            sqr(ax, t1)
            sqr(t1, t2)
            mul(az, t1, dx)

