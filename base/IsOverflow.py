from base.Long10 import Long10

class Is_Overflow(object):

    def __init__(self, x):
        self.P25 = 33554431
        self.P26 = 67108863
        self.x = x

        self.run()

    def run(self):
        if isinstance(self.x, Long10):
            print("isInstance of Long10")
            return (((self.x._0 > self.P26-19)) and ((self.x._1 & self.x._3 & self.x._5 & self.x._7 & self.x._9) == self.P25) and ((self.x._2 & self.x._4 & self.x._6 & self.x._8) == self.P26)) or (self.x._9 > self.P25)