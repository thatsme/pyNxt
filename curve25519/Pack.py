from curve25519.IsOverflow import Is_Overflow
from curve25519.Packl_ctypes import Packl_ctypes as packl_ctypes

class Pack(object):

    def __init__(self, x, m):
        """
        Convert from internal format to little-endian byte format.  The
        number must be in a reduced form which is output by the following ops:
             unpack, mul, sqr
             set --  if input in range 0 .. P25
        If you're unsure if the number is reduced, first multiply it by 1.  */
        """

        P25 = 33554431
        P26 = 67108863

        ld = 0
        ud = 0
        t = None

        # ld = (Is_Overflow(x)?1:0) - ((x._9 < 0)?1:0)
        ld = (1 if Is_Overflow(x).value else 0) - (1 if (x._9 < 0) else 0)
        ud = ld * -(P25+1)
        ld *= 19

        t = ld + x._0 + (x._1 << 26)

        m[0] = packl_ctypes(t).value
        m[1] = packl_ctypes(t >> 8).value
        m[2] = packl_ctypes(t >> 16).value
        m[3] = packl_ctypes(t >> 24).value
        t = (t >> 32) + (x._2 << 19)
        m[4] = packl_ctypes(t).value
        m[5] = packl_ctypes(t >> 8).value
        m[6] = packl_ctypes(t >> 16).value
        m[7] = packl_ctypes(t >> 24).value
        t = (t >> 32) + (x._3 << 13)
        m[8] = packl_ctypes(t).value
        m[9] = packl_ctypes(t >> 8).value
        m[10] = packl_ctypes(t >> 16).value
        m[11] = packl_ctypes(t >> 24).value
        t = (t >> 32) + (x._4 <<  6)
        m[12] = packl_ctypes(t).value
        m[13] = packl_ctypes(t >> 8).value
        m[14] = packl_ctypes(t >> 16).value
        m[15] = packl_ctypes(t >> 24).value
        t = (t >> 32) + x._5 + (x._6 << 25)
        m[16] = packl_ctypes(t).value
        m[17] = packl_ctypes(t >> 8).value
        m[18] = packl_ctypes(t >> 16).value
        m[19] = packl_ctypes(t >> 24).value
        t = (t >> 32) + (x._7 << 19)
        m[20] = packl_ctypes(t).value
        m[21] = packl_ctypes(t >> 8).value
        m[22] = packl_ctypes(t >> 16).value
        m[23] = packl_ctypes(t >> 24).value
        t = (t >> 32) + (x._8 << 12)
        m[24] = packl_ctypes(t).value
        m[25] = packl_ctypes(t >> 8).value
        m[26] = packl_ctypes(t >> 16).value
        m[27] = packl_ctypes(t >> 24).value
        t = (t >> 32) + ((x._9 + ud) << 6)
        m[28] = packl_ctypes(t).value
        m[29] = packl_ctypes(t >> 8).value
        m[30] = packl_ctypes(t >> 16).value
        m[31] = packl_ctypes(t >> 24).value