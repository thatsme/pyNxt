from curve25519.Sign import Sign as sign
from curve25519.Keygen import Keygen as ki
from curve25519.ToHexString import ToHexString
from curve25519.ParseHexString import ParseHexString as ParseHexString
from hashlib import sha256
import struct
import codecs

class SignTransactionOffline(object):

    def __init__(self, secretPhrase=None, transaction = None):
        self._secretPhrase = secretPhrase
        #self._transaction = ParseHexString(transaction).getData()
        self._transaction = transaction
        self.P = [0] * 32
        self.h = [0] * 32
        self.m = [0] * 32
        self.v_list = [0] * 32
        self.sct = None
        self.pk_1 = None
        self.s_1 = [0] * 32
        self.pk_2 = None
        self.s_2 = [0] * 32
        self.hash_m = sha256()
        self.hash_h = sha256()
        self.hash_x = sha256()
        self.MDEBUG = False

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def transaction(self):
        return self.__transaction

    @transaction.setter
    def transaction(self, value):
        self._transaction = ParseHexString(value).getData()

    def bytesToList(self, b):
        return list(struct.unpack('=32b', b))

    def listToBytes(self, l):
        return bytes(b % 256 for b in l)

    def twoscomplement_to_unsigned(self, i):
        return i % 256

    def run(self):
        secret = sha256(self.secretPhrase.encode('utf-8')).hexdigest()
        self.sct = ParseHexString(secret).getData()

        #####
        self.keygen = ki(self.P, self.s_1, self.sct)
        self.pk_1 = self.keygen.publicKey
        ####

        if self.MDEBUG:
            print("Secret Key first keygen ", ToHexString(self.pk_1).getString())
            print("self.s first keygen ", ToHexString(self.s_1).getString())

        self.hash_m.update(self.listToBytes(self.transaction))
        self.m_bytes = self.hash_m.digest()

        if self.MDEBUG:
            print("self.m bytes ", self.m_bytes)
            print("len of self.m bytes ", len(self.m_bytes))

        self.hash_x.update(self.m_bytes)
        self.hash_x.update(self.listToBytes(self.s_1))
        self.x_bytes = self.hash_x.digest()
        self.x_list = self.bytesToList(self.x_bytes)

        if self.MDEBUG:
            print("self.x bytes ", self.x_bytes)
            print("self.x list ", self.x_list)
            print("len of self.x bytes ", len(self.x_bytes))

        # New Keygen with  s at None
        Y_list = [0] * 32
        self.keygen2 = ki(Y_list, None, self.x_list)

        if self.MDEBUG:
            print("Y list ", Y_list)
            print("xx list ", self.x_list)
            print("len of xx list ", len(self.x_list))

        Y_bytes = self.listToBytes(Y_list)

        self.hash_h.update(self.m_bytes)
        self.hash_h.update(Y_bytes)
        self.h_bytes = self.hash_h.digest()
        self.h_list = self.bytesToList(self.h_bytes)

        if self.MDEBUG:
            print("self.h bytes ", self.h_bytes)
            print("self.h list ", self.h_list)
            print("len self.h bytes ", len(self.h_bytes))

        mySign = sign(self.v_list, self.h_list, self.x_list, self.s_1)

        if self.MDEBUG:
            print("signed transaction self.v_list ", ToHexString(self.v_list).getString(), " ", self.v_list)
            print("signed transaction self.h_list ", ToHexString(self.h_list).getString(), " ", self.h_list)
            print("signed transaction self.x_list ", ToHexString(self.x_list).getString(), " ", self.x_list)
            print("signed transaction self.s_1 ls ", ToHexString(self.s_1).getString(), " ", self.s_1)
            print()

    def getSignature(self):
        self.signature = self.v_list+self.h_list
        return codecs.encode(self.listToBytes(self.signature),'hex_codec')

    def getSigningKey(self):
        return codecs.encode(self.listToBytes(self.self.v_list),'hex_codec')

    def getVerificationKey(self):
        return codecs.encode(self.listToBytes(self.self.h_list),'hex_codec')

    def getVerified(self):
        return None
