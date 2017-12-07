from curve25519.Long10 import Long10 as Long10

class Is_Overflow(object):

    def __init__(self, x):
        P25 = 33554431
        P26 = 67108863
        self.value = None

        if isinstance(self.x, Long10):
            #print("isInstance of Long10")
            self.value = (((x._0 > P26-19)) and ((x._1 & x._3 & x._5 & x._7 & x._9) == P25) and ((x._2 & x._4 & x._6 & x._8) == P26)) or (x._9 > P25)

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)
