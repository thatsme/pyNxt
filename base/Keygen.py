from base.Clamp import Clamp as clamp
from base.Core import Core as core

class Keygen(object):

    def __init__(self, P,  s,  k):

        """

        :param P: byte[]
        :param s: byte[]
        :param k: byte[]
        """
        k1 = bytearray(k,"utf-8")
        #P1 = bytearray(P,"utf-8")

        clamp(k1);

        core(P, s, k1, None);
