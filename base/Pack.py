from base.IsOverflow import Is_Overflow
import struct
import ctypes

PyLong_AsByteArray = ctypes.pythonapi._PyLong_AsByteArray
PyLong_AsByteArray.argtypes = [ctypes.py_object,
                               ctypes.c_char_p,
                               ctypes.c_size_t,
                               ctypes.c_int,
                               ctypes.c_int]

def packl_ctypes(lnum):
    a = ctypes.create_string_buffer(lnum.bit_length()//8 + 1)
    PyLong_AsByteArray(lnum, a, len(a), 0, 1)
    #for a1 in a:
    #    print(struct.unpack('b', a1))
    print(struct.unpack('b', a[-1]))
    b = struct.unpack('b', a[-1])
    return b[0]

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
        notskip = True

        ld = 0,
        ud = 0
        t = None # Long;
        #ld = (Is_Overflow(x)?1:0) - ((x._9 < 0)?1:0);
        ld = (1 if Is_Overflow(x) else 0) - (1 if (x._9 < 0) else 0)
        print("ld -->",ld)
        ud = ld * -(P25+1)
        ld *= 19
        print("ld -->",ld)
        print("ud -->",ud)
        print("x._9",x._9)

        t = ld + x._0 + (x._1 << 26)

        print(" x._1 ----->",x._1)
        print(" << 26 ----->",(x._1 << 26))
        print(" x._1 ----->",x._1)
        print(">>8",(t >> 8))
        #print( struct.pack("N", t))
        #m[0] = it.to_bytes(4, 'big')
        #m[0] = int(struct.pack('b', mybytes(t)))
        m[0] = packl_ctypes(t)
        m[1] = packl_ctypes(t >> 8)
        m[2] = packl_ctypes(t >> 16)
        m[3] = packl_ctypes(t >> 24)
        t = (t >> 32) + (x._2 << 19)
        m[4] = packl_ctypes(t)
        m[5] = packl_ctypes(t >> 8)
        m[6] = packl_ctypes(t >> 16)
        m[7] = packl_ctypes(t >> 24)
        t = (t >> 32) + (x._3 << 13)
        m[8] = packl_ctypes(t)
        m[9] = packl_ctypes(t >> 8)
        m[10] = packl_ctypes(t >> 16)
        m[11] = packl_ctypes(t >> 24)
        t = (t >> 32) + (x._4 <<  6)
        m[12] = packl_ctypes(t)
        m[13] = packl_ctypes(t >> 8)
        m[14] = packl_ctypes(t >> 16)
        m[15] = packl_ctypes(t >> 24)
        t = (t >> 32) + x._5 + (x._6 << 25)
        m[16] = packl_ctypes(t)
        m[17] = packl_ctypes(t >> 8)
        m[18] = packl_ctypes(t >> 16)
        m[19] = packl_ctypes(t >> 24)
        t = (t >> 32) + (x._7 << 19)
        m[20] = packl_ctypes(t)
        m[21] = packl_ctypes(t >> 8)
        m[22] = packl_ctypes(t >> 16)
        m[23] = packl_ctypes(t >> 24)
        t = (t >> 32) + (x._8 << 12)
        m[24] = packl_ctypes(t)
        m[25] = packl_ctypes(t >> 8)
        m[26] = packl_ctypes(t >> 16)
        m[27] = packl_ctypes(t >> 24)
        t = (t >> 32) + ((x._9 + ud) << 6)
        m[28] = packl_ctypes(t)
        m[29] = packl_ctypes(t >> 8)
        m[30] = packl_ctypes(t >> 16)
        m[31] = packl_ctypes(t >> 24)