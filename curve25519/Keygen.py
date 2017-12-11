from curve25519.Clamp import Clamp as clamp
from curve25519.Core import Core as core
from curve25519.ToHexString import ToHexString
from curve25519.ParseHexString import ParseHexString as ParseHexString

class Keygen(object):

    def __init__(self, P,  s,  k):

        """

        :param P: byte[]
        :param s: byte[]
        :param k: byte[]
        """
        #k1 = bytearray(k,"utf-8")
        #P1 = bytearray(P,"utf-8")
        self.debug = True

        self.publicKey = P
        self.s = None
        if self.debug:
            print()
            print("Python Keygen secret key before clamp ", ToHexString(k).getString())
        clamp(k)
        if self.debug:
            print("Python Keygen secret key after clamp  ", ToHexString(k).getString())
            print()

        core(P, s, k, None)

        self.s = s

        if self.debug:
            print("Python Keygen Public key after core   ", ToHexString(P).getString())
            print()


    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
