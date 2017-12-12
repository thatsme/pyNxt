from curve25519.Packl_ctypes import Packl_ctypes as packl_ctypes

class Clamp(object):

    def __init__(self, k):
        """

        :param k: list[]
        """
        #print(k[0], k[31])

        k[31] &= 0x7F
        k[31] |= 0x40
        k[0] &= 0xF8

        k[0] = packl_ctypes(k[0]).value
        k[31] = packl_ctypes(k[31]).value
        #print(k[0], k[31])
