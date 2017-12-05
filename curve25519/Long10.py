
class Long10(object):

    def __init__(self,i0=0,i1=0,i2=0,i3=0,i4=0,i5=0,i6=0,i7=0,i8=0,i9=0):
        self.v0 = i0
        self.v1 = i1
        self.v2 = i2
        self.v3 = i3
        self.v4 = i4
        self.v5 = i5
        self.v6 = i6
        self.v7 = i7
        self.v8 = i8
        self.v9 = i9

    def __str__(self):
        return "({0},{1},{2},{3},{4},{5},{6},{7},{8},{9})".format(self.v0,self.v1,self.v2,self.v3,self.v4,self.v5,self.v6,self.v7,self.v8,self.v9)

    @property
    def _0(self):
        return self.v0

    @_0.setter
    def _0(self, value):
        self.v0 = value

    @property
    def _1(self):
        return self.v1

    @_1.setter
    def _1(self, value):
        self.v1 = value

    @property
    def _2(self):
        return self.v2

    @_2.setter
    def _2(self, value):
        self.v2 = value

    @property
    def _3(self):
        return self.v3

    @_3.setter
    def _3(self, value):
        self.v3 = value

    @property
    def _4(self):
        return self.v4

    @_4.setter
    def _4(self, value):
        self.v4 = value

    @property
    def _5(self):
        return self.v5

    @_5.setter
    def _5(self, value):
        self.v5 = value

    @property
    def _6(self):
        return self.v6

    @_6.setter
    def _6(self, value):
        self.v6 = value

    @property
    def _7(self):
        return self.v7

    @_7.setter
    def _7(self, value):
        self.v7 = value

    @property
    def _8(self):
        return self.v8

    @_8.setter
    def _8(self, value):
        self.v8 = value

    @property
    def _9(self):
        return self.v9

    @_9.setter
    def _9(self, value):
        self.v9 = value
