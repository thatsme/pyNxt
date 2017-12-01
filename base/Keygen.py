from base.Clamp import Clamp as clamp
from base.Core import Core as core

class Keygen(object):

    def __init__(self, P,  s,  k):

        """

        :param P: byte[]
        :param s: byte[]
        :param k: byte[]
        """

        clamp(k);
        core(P, s, k, None);
