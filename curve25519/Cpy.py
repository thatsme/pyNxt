from curve25519.Long10 import Long10 as Long10

class Cpy(object):

    def __init__(self, outp, inp):

        if isinstance(inp, Long10) and isinstance(outp, Long10):

            outp._0 = inp._0
            outp._1 = inp._1
            outp._2 = inp._2
            outp._3 = inp._3
            outp._4 = inp._4
            outp._5 = inp._5
            outp._6 = inp._6
            outp._7 = inp._7
            outp._8 = inp._8
            outp._9 = inp._9