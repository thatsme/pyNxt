import base.Core as core

class Curve(object):

    def __init__(self, Z, k, P):

        """

        :param Z: byte[]
        :param k: byte[]
        :param P: byte[]
        """
        core(Z, None, k, P);