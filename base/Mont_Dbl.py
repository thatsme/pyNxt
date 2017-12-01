import base.Sqr as sqr
import base.Mul as mul
import base.Sub as sub
import base.Mul_Small as mul_small
import base.Add as add

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

        sqr(t1, t3);
        sqr(t2, t4);
        mul(bx, t1, t2);
        sub(t2, t1, t2);
        mul_small(bz, t2, 121665);
        add(t1, t1, bz);
        mul(bz, t1, t2);

