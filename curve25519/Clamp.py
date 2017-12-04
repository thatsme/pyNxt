

class Clamp(object):

    def __init__(self, k):
        """

        :param k: list[]
        """

        k[31] &= 0x7F
        k[31] |= 0x40
        k[0] &= 0xF8
