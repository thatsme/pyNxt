
class Cpy32(object):

    def __init__(self, d, s):
        """

        :param d: list[]
        :param s: list[]
        """

        i = 0
        for i in range(32):
            d[i] = s[i]