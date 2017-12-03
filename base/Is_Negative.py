import base.IsOverflow as is_overflow

class Is_Negative(object):

    def __init__(self, x):
        """

        :param x: Long10
        """

        return (is_overflow(x) or (1 if (x._9 < 0) else 0) ^ (x._0 & 1))

