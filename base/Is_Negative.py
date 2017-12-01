import base.IsOverflow as is_overflow

class Is_Negative(object)

    def __init__(self, x):
        """

        :param x: Long10
        """

        return (int)(((is_overflow(x) || (x._9 < 0))?1:0) ^ (x._0 & 1));

