# -*- coding: utf-8 -*-
import sys
from hashlib import sha256
import codecs
from ecdsa.numbertheory import square_root_mod_prime, SquareRootError, inverse_mod

class Curve25519(object):

    def __init__(self):
        """
        # a pedagogical implementation of curve25519 with ec-kcdsa
        # coded by doctorevil to validate nxt's port of Matthijs van Duin's implementation
        # warning: this implementation is not timing attack resistant
        # ec arithmetic equations from http://hyperelliptic.org/EFD/g1p/auto-montgom.html

        *    s is the private key for signing
        *    P is the corresponding public key
        *    Z is the context data (signer public key or certificate, etc)
        *
        * signing:
        *
        *    m = hash(Z, message)
        *    x = hash(m, s)
        *    keygen25519(Y, NULL, x);
        *    r = hash(Y);
        *    h = m XOR r
        *    sign25519(v, h, x, s);
        *
        *    output (v,r) as the signature
        *
        * verification:
        *
        *    m = hash(Z, message);
        *    h = m XOR r
        *    verify25519(Y, v, h, P)
        *
        *    confirm  r == hash(Y)
        """
        self.CURVE_P = 2 ** 255 - 19
        self.CURVE_A = 486662
        self.CURVE_ORDER = 7237005577332262213973186563042994240857116359379907606001950938285454250989
        self.CURVE_G_X = 9
        self.CURVE_G_Y = 14781619447589544791020593568409986887264606134616475288964881837755586237401

    def _le32(self, n):  # to little endian
        # return ('%064x' % n).decode('hex')[::-1]
        #print(('%064x' % n))
        #print(codecs.decode(('%064x' % n),'hex_codec')[::-1])
        return codecs.decode(('%064x' % n),'hex_codec')[::-1]

    def _from_le32(self, s):
        # return int(s[::-1].encode('hex'), 16)
        #print(int(codecs.encode(s[::-1],'hex_codec'), 16))
        return int(codecs.encode(s[::-1],'hex_codec'), 16)

    def _curve25519_x_to_y(self, x):
        t = (x ** 3 + self.CURVE_A * x ** 2 + x) % self.CURVE_P
        try:
            return square_root_mod_prime( t, self.CURVE_P)
        except SquareRootError:
            return None

    def _curve25519_affine_add(self, x1, y1, x2, y2):
        if (x1, y1) == (1, 0):
            return x2, y2
        if (x2, y2) == (1, 0):
            return x1, y1
        if x1 == x2 and y1 != y2:
            return (1, 0)
        if x1 == x2 and y1 == y2:
            return self._curve25519_affine_double(x1, y1)

        t1 = (y2 - y1) ** 2 % self.CURVE_P
        t2 = (x2 - x1) ** 2 % self.CURVE_P
        x3 = (t1 * inverse_mod(t2, self.CURVE_P) - 486662 - x1 - x2) % self.CURVE_P
        t1 = (2 * x1 + x2 + 486662) % self.CURVE_P
        t2 = (y2 - y1) % self.CURVE_P
        t3 = (x2 - x1) % self.CURVE_P

        y3 = t1 * (y2 - y1) * inverse_mod((x2 - x1) % self.CURVE_P, self.CURVE_P) - \
             t2 ** 3 * inverse_mod(t3 ** 3 % self.CURVE_P, self.CURVE_P) - y1
        y3 = y3 % self.CURVE_P
        return x3, y3

    def _curve25519_affine_double(self, x1, y1):
        if (x1, y1) == (1, 0):
            return (1, 0)

        x2 = (3 * x1 ** 2 + 2 * self.CURVE_A * x1 + 1) ** 2 * inverse_mod((2 * y1) ** 2, self.CURVE_P) - self.CURVE_A - x1 - x1
        y2 = (2 * x1 + x1 + self.CURVE_A) * (3 * x1 ** 2 + 2 * self.CURVE_A * x1 + 1) * inverse_mod(2 * y1, self.CURVE_P) - \
             (3 * x1 ** 2 + 2 * self.CURVE_A * x1 + 1) ** 3 * inverse_mod((2 * y1) ** 3, self.CURVE_P) - y1
        return x2 % self.CURVE_P, y2 % self.CURVE_P

    def _curve25519_affine_mult(self, n, x1, y1):
        tx, ty = 1, 0
        for bit in map(int, bin(n)[2:]):
            tx, ty = self._curve25519_affine_double(tx, ty)
            if bit:
                tx, ty = self._curve25519_affine_add(tx, ty, x1, y1)
        return tx, ty

    def _clamp(self, secret):
        a = ord(secret[0])
        #a = secret[0]
        a &= 248
        b = ord(secret[31])
        #b = secret[31]
        b &= 127
        b |= 64
        return bytes(chr(a),'utf-8') + secret[1:-1] + bytes(chr(b),'utf-8')

    def _is_negative(self, x):
        return x & 1

    def curve25519_eckcdsa_keygen(self, secret):
        # print(secret)
        s = self._from_le32(self._clamp(secret))
        x, y = self._curve25519_affine_mult(s, self.CURVE_G_X, self.CURVE_G_Y)
        signing_key = inverse_mod(s if self._is_negative(y) else -s, self.CURVE_ORDER)
        return self._le32(x), self._le32(signing_key), self._le32(s)

    def kcdsa_sign(self, message, secret):

        verification_key, signing_key, ignored = self.curve25519_eckcdsa_keygen(secret)

        m = sha256(message).digest()
        k = sha256(m + signing_key).digest()
        k_Gx, ignored, k_clamped = self.curve25519_eckcdsa_keygen(k)
        r = sha256(m + k_Gx).digest()
        print("m", m)
        print("k", k)

        s = (self._from_le32(k_clamped) - self._from_le32(r)) * self._from_le32(signing_key) % self.CURVE_ORDER
        print("r", codecs.encode(r,'hex_codec'))
        print("s", s)
        print("le_s", codecs.encode(self._le32(s),'hex_codec'))

        print("le_s",self._le32(s))
        return self._le32(s) + r

    def kcdsa_sign2(self, message, secret):
        """
        digest.reset();
        byte[] P = new byte[32];
        byte[] s = new byte[32];
        Curve25519.keygen(P, s, digest.digest(secretPhrase.getBytes("UTF-8")));

        byte[] m = digest.digest(message);

        digest.update(m);
        byte[] x = digest.digest(s);

        byte[] Y = new byte[32];
        Curve25519.keygen(Y, null, x);

        digest.update(m);
        byte[] h = digest.digest(Y);

        byte[] v = new byte[32];
        Curve25519.sign(v, h, x, s);

        System.arraycopy(v, 0, signature, 0, 32);
        System.arraycopy(h, 0, signature, 32, 32);
        """
        verification_key, signing_key, ignored = self.curve25519_eckcdsa_keygen(secret)
        ciapilo = sha256()
        m.update(message)
        m.digest()
        m.update(signing_key)

        m = sha256(message).digest()
        k = sha256(m + signing_key).digest()
        k_Gx, ignored, k_clamped = self.curve25519_eckcdsa_keygen(k)
        r = sha256(m + k_Gx).digest()
        print("m", m)
        print("k", k)

        s = (self._from_le32(k_clamped) - self._from_le32(r)) * self._from_le32(signing_key) % self.CURVE_ORDER
        print("r", r)
        print("s", s)
        print("le_s",self._le32(s))
        return self._le32(s) + r

    def kcdsa_verify(self, signature, message, public_key):
        if len(signature) != 64:
            return False

        s = self._from_le32(signature[:32])
        r = self._from_le32(signature[32:64])

        px = self._from_le32(public_key)
        py = self._curve25519_x_to_y(px)
        if py is None:  # pubkey is bogus; bail
            return False

        tx1, ty1 = self._curve25519_affine_mult(s, px, py)
        tx2, ty2 = self._curve25519_affine_mult(r, self.CURVE_G_X, self.CURVE_G_Y)
        if not self._is_negative(py):
            ty2 = -ty2
        k_Gx, k_Gy = self._curve25519_affine_add(tx1, ty1, tx2, ty2)

        m = sha256(message).digest()
        return self._le32(r) == sha256(m + self._le32(k_Gx)).digest()

