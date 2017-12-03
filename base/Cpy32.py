
class Cpy32(object):

    def __init__(self, d, s):
        """

        :param d: byte[]
        :param s: byte[]
        """

        i = 0
        for i in range(32):
            d[i] = s[i]