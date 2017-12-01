from base.IsOverflow import Is_Overflow

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

        print(m)
        x.printAll()

        ld = 0,
        ud = 0
        t = None # Long;
        #ld = (Is_Overflow(x)?1:0) - ((x._9 < 0)?1:0);
        ld = (1 if Is_Overflow(x) else 0) - (1 if (x._9 < 0) else 0)
        print(ld)
        ud = ld * -(P25+1)
        ld *= 19
        print(ld)
        print(ud)

        t = ld + x._0 + (x._1 << 26)
        print(t)
        print((x._1 << 26))

        m[ 0] = t
        m[ 1] = (t >> 8)
        m[ 2] = (t >> 16)
        m[ 3] = (t >> 24)
        t = (t >> 32) + (x._2 << 19)
        m[ 4] = t
        m[ 5] = (t >> 8)
        m[ 6] = (t >> 16)
        m[ 7] = (t >> 24)
        t = (t >> 32) + (x._3 << 13)
        m[ 8] = t
        m[ 9] = (t >> 8)
        m[10] = (t >> 16)
        m[11] = (t >> 24)
        t = (t >> 32) + (x._4 <<  6)
        m[12] = t
        m[13] = (t >> 8)
        m[14] = (t >> 16)
        m[15] = (t >> 24)
        t = (t >> 32) + x._5 + (x._6 << 25)
        m[16] = t
        m[17] = (t >> 8)
        m[18] = (t >> 16)
        m[19] = (t >> 24)
        t = (t >> 32) + (x._7 << 19)
        m[20] = t
        m[21] = (t >> 8)
        m[22] = (t >> 16)
        m[23] = (t >> 24)
        t = (t >> 32) + (x._8 << 12)
        m[24] = t
        m[25] = (t >> 8)
        m[26] = (t >> 16)
        m[27] = (t >> 24)
        t = (t >> 32) + ((x._9 + ud) << 6)
        m[28] = t
        m[29] = (t >> 8)
        m[30] = (t >> 16)
        m[31] = (t >> 24)