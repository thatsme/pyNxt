from base.IsOverflow import Is_Overflow as is_overflow

class Is_Negative(object):

    def __init__(self, x):
        """

        :param x: Long10
        """
        self.x = x
        self.run()

    def run(self):
        return (is_overflow(self.x) or (1 if (self.x._9 < 0) else 0) ^ (self.x._0 & 1))

