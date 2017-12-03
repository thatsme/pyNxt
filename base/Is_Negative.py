from base.IsOverflow import Is_Overflow as is_overflow

class Is_Negative(object):

    def __init__(self, x):
        """

        :param x: Long10
        """
        self.x = x
        self.value = (is_overflow(self.x).value or (1 if (self.x._9 < 0) else 0) ^ (self.x._0 & 1))

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)
