from curve25519.IsOverflow import Is_Overflow as is_overflow
from curve25519.Long10 import Long10

class Is_Negative(object):

    def __init__(self, x):
        """

        :param x: Long10
        """
        if isinstance(self.x, Long10):
            self.isinoverflow = is_overflow(x).value
            #print("Is_negative before ", x._0)
            self.value = (self.isinoverflow or (1 if (x._9 < 0) else 0) ^ (x._0 & 1))
            #print("Is_negative after ", x._0)

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)
