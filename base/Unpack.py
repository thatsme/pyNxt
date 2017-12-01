from base.Long10 import Long10

class Unpack(object):

    def __init__(self,x , m):
        """/* Convert to internal format from little-endian byte format */ """
        if isinstance(x, Long10):

            x._0 = ((m[0] & 0xFF))         | ((m[1] & 0xFF))<<8 | (m[2] & 0xFF)<<16      | ((m[3] & 0xFF)& 3)<<24
            x._1 = ((m[3] & 0xFF)&~ 3)>>2  | (m[4] & 0xFF)<<6 | (m[5] & 0xFF)<<14 | ((m[6] & 0xFF)& 7)<<22
            x._2 = ((m[6] & 0xFF)&~ 7)>>3  | (m[7] & 0xFF)<<5 |(m[8] & 0xFF)<<13 | ((m[9] & 0xFF)&31)<<21;
            x._3 = ((m[9] & 0xFF)&~31)>>5  | (m[10] & 0xFF)<<3 | (m[11] & 0xFF)<<11 | ((m[12] & 0xFF)&63)<<19;
            x._4 = ((m[12] & 0xFF)&~63)>>6 | (m[13] & 0xFF)<<2 |(m[14] & 0xFF)<<10 |  (m[15] & 0xFF)    <<18;
            x._5 = (m[16] & 0xFF)         | (m[17] & 0xFF)<<8 | (m[18] & 0xFF)<<16 | ((m[19] & 0xFF)& 1)<<24;
            x._6 = ((m[19] & 0xFF)&~ 1)>>1 | (m[20] & 0xFF)<<7 | (m[21] & 0xFF)<<15 | ((m[22] & 0xFF)& 7)<<23;
            x._7 = ((m[22] & 0xFF)&~ 7)>>3 | (m[23] & 0xFF)<<5 | (m[24] & 0xFF)<<13 | ((m[25] & 0xFF)&15)<<21;
            x._8 = ((m[25] & 0xFF)&~15)>>4 | (m[26] & 0xFF)<<4 |(m[27] & 0xFF)<<12 | ((m[28] & 0xFF)&63)<<20;
            x._9 = ((m[28] & 0xFF)&~63)>>6 | (m[29] & 0xFF)<<2 |(m[30] & 0xFF)<<10 |  (m[31] & 0xFF)    <<18;
