import codecs
import curve25519.Curve25519 as curve
from hashlib import sha256

class SignTransactionOffline(object):
    def __init__(self, secretPhrase=None, transaction = None):
        self.secretPhrase = secretPhrase
        #self.transaction = transaction

        self.transaction = sha256(transaction).digest()
        self.secret = sha256(self.secretPhrase).digest()

        self.myCurve = curve.Curve25519()
        self.verification_key = None
        self.signing_key = None
        self.secret_clamped = None

        self.verification_key, self.signing_key, self.secret_clamped = self.myCurve.curve25519_eckcdsa_keygen(self.secret)
        self.signature = None
        self.verified = None
    def run(self):

        self.signature = self.myCurve.kcdsa_sign(self.transaction, self.secret)
        self.verified = self.myCurve.kcdsa_verify(self.signature, self.transaction, self.verification_key)

    def getSignature(self):
        return codecs.encode(self.signature,'hex_codec')
        #return self.signature

    def getSigningKey(self):
        return codecs.encode(self.signing_key,'hex_codec')

    def getVerificationKey(self):
        return codecs.encode(self.verification_key,'hex_codec')

    def getVerified(self):
        return self.verified
