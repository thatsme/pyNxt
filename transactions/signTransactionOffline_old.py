import codecs
from curve25519.Sign import Sign as sign
from curve25519.Keygen import Keygen as ki
#import drop.Curve25519 as curve
from hashlib import sha256
from curve25519.ToHexString import ToHexString
from curve25519.ParseHexString import ParseHexString as ParseHexString
import struct
from copy import deepcopy

class SignTransactionOffline(object):

    def __init__(self, secretPhrase=None, transaction = None):
        self.secretPhrase = secretPhrase
        #self.transaction = transaction

        # Ok, prepariamoci a fare il sign della variabile unsignedTransactionBytes

        ## Ok con il bytearray abbiamo problemi legati al range 0 - 256, invece che -128 - +128
        ## quindi proviamo a sostituire con una lista
        # P = bytearray(32)
        self.secretPhrase = secretPhrase
        self.transaction = ParseHexString(transaction).getData()
        self.P = [0] * 32
        self.h = [0] * 32
        self.m = [0] * 32
        self.v = [0] * 32
        self.sct = None
        self.pk_1 = None
        self.s_1 = [0] * 32
        self.pk_2 = None
        self.s_2 = [0] * 32
        self.first = sha256()
        self.all = sha256()
        self.xhash = sha256()
        self.hhash = sha256()

    def bytesToList(self, b):
        return list(struct.unpack('<32b', self.x))

    def twoscomplement_to_unsigned(self, i):
        return i % 256

    def run(self):
        secret = sha256(self.secretPhrase.encode('utf-8')).hexdigest()
        self.sct = ParseHexString(secret).getData()

        #####
        self.keygen = ki(self.P, self.s_1, self.sct)
        self.pk_1 = self.keygen.publicKey
        self.s_1 = self.keygen.s
        ####

        print("Secret Key first keygen ", ToHexString(self.pk_1).getString())
        print("self.s first keygen ", ToHexString(self.s_1).getString())

        mm = bytes(b % 256 for b in self.transaction)

        self.first.update(mm)
        self.m = self.first.digest()

        print("self.m bytes ", self.m)
        print("len of self.m bytes ", len(self.m))
        print("type of self.m bytes ", type(self.m))

        self.all.update(self.m)

        ss = bytes(b % 256 for b in self.s_1)
        self.all.update(ss)
        self.x = self.all.digest()

        print("self.x bytes ", self.x)
        print("len of self.x bytes ", len(self.x))
        print("type of self.x bytes ", type(self.x))

        xx = self.bytesToList(self.x)

        # New Keygen with  s at None
        Y = [0] * 32
        self.keygen2 = ki(Y, None, xx)
        self.pk_2 = self.keygen2.publicKey
        self.s_2 = self.keygen2.s


        print("Y  ", Y)
        print("xx bytes ", xx)
        #print("self.s second keygen ", ToHexString(self.s_2).getString())

        self.all.update(self.m)

        # Digest of self.Y in self.h
        YY = bytes(b % 256 for b in self.Y)
        #self.all.update(ToHexString(self.Y).getString().encode('utf-8'))
        self.all.update(YY)
        #self.h = self.all.hexdigest()
        self.h = self.all.digest()

        print("self.h bytes ", self.h)
        print("len self.h bytes ", len(self.h))
        print("type self.h bytes ", type(self.h))

        ## Finally the signature
        self.hh = self.bytesToList(self.h)
        self.xx = self.bytesToList(xx)
        mySign = sign(self.v, self.hh, self.xx, self.s_1)

        print("signed transaction self.v ", self.v)
        print("signed transaction self.hh ", ToHexString(self.hh).getString())

    def getSignature(self):
        return codecs.encode(self.signature,'hex_codec')
        #return self.signature

    def getSigningKey(self):
        return codecs.encode(self.signing_key,'hex_codec')

    def getVerificationKey(self):
        return codecs.encode(self.verification_key,'hex_codec')

    def getVerified(self):
        return self.verified
