"""

The unsigned transaction of setAccount Property (test1, value1):

{
    "transactionJSON": {
        "senderPublicKey": "6282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19",
        "feeNQT": "100000000",
        "type": 1,
        "version": 1,
        "phased": false,
        "ecBlockId": "6827938886709383368",
        "attachment": {
            "property": "test1",
            "value": "value1",
            "version.AccountProperty": 1
        },
        "senderRS": "NXT-XWQY-C2MJ-JPL8-F4BW2",
        "subtype": 10,
        "amountNQT": "0",
        "sender": "15019823959905333982",
        "recipientRS": "NXT-XWQY-C2MJ-JPL8-F4BW2",
        "recipient": "15019823959905333982",
        "ecBlockHeight": 1556740,
        "deadline": 1,
        "timestamp": 127003043,
        "height": 2147483647
    },
    "unsignedTransactionBytes": "011aa3e9910701006282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19def20e27502271d0000000000000000000e1f505000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004c11700c89063d23db6c15e010574657374310676616c756531",
    "broadcasted": false,
    "requestProcessingTime": 10
}


{
    "signatureHash": "4892f9904048c1a2ddd3125340b4e068255c284ff52e5f462d8527fa213559c3",
    "transactionJSON": {
        "senderPublicKey": "6282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19",
        "signature": "2719adcbd0bb05831a2450bf3c4890e27a6560baa2323273260199f6ba8bb0099d2ea4e9225c6f02dbf8a882dbc92283f56de247189d3c2f9ee1082bd243f526",
        "feeNQT": "100000000",
        "type": 1,
        "fullHash": "9338130cf38d7055f25d8c2eeb5bafc3dcc9bd6f9ac224956fc45ff70314da23",
        "version": 1,
        "phased": false,
        "ecBlockId": "6827938886709383368",
        "signatureHash": "4892f9904048c1a2ddd3125340b4e068255c284ff52e5f462d8527fa213559c3",
        "attachment": {
            "property": "test1",
            "value": "value1",
            "version.AccountProperty": 1
        },
        "senderRS": "NXT-XWQY-C2MJ-JPL8-F4BW2",
        "subtype": 10,
        "amountNQT": "0",
        "sender": "15019823959905333982",
        "recipientRS": "NXT-XWQY-C2MJ-JPL8-F4BW2",
        "recipient": "15019823959905333982",
        "ecBlockHeight": 1556740,
        "deadline": 1,
        "transaction": "6156576765634623635",
        "timestamp": 127003043,
        "height": 2147483647
    },
    "verify": true,
    "requestProcessingTime": 12,
    "transactionBytes": "011aa3e9910701006282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19def20e27502271d0000000000000000000e1f5050000000000000000000000000000000000000000000000000000000000000000000000002719adcbd0bb05831a2450bf3c4890e27a6560baa2323273260199f6ba8bb0099d2ea4e9225c6f02dbf8a882dbc92283f56de247189d3c2f9ee1082bd243f5260000000004c11700c89063d23db6c15e010574657374310676616c756531",
    "fullHash": "9338130cf38d7055f25d8c2eeb5bafc3dcc9bd6f9ac224956fc45ff70314da23",
    "transaction": "6156576765634623635"
}

Java sequence for signing :

    digest.reset();
    byte[] P = new byte[32];
    byte[] s = new byte[32];
    Curve25519.keygen(P, s, digest.digest(secretPhrase.getBytes("UTF-8")));

    byte[] m = digest.digest(message);
    System.out.println("sign --> (m) "+m+" "+toHexString(m));

    digest.update(m);
    byte[] x = digest.digest(s);
    System.out.println("sign --> (x) digest(s) "+x+" "+toHexString(x));

    byte[] Y = new byte[32];
    Curve25519.keygen(Y, null, x);

    digest.update(m);
    byte[] h = digest.digest(Y);
    System.out.println("sign --> (h) digest(Y) "+h+" "+toHexString(h));

    byte[] v = new byte[32];
    Curve25519.sign(v, h, x, s);

    System.out.println("sign --> (v) sign(v, h, x, s) "+v+" "+toHexString(v));
    System.out.println("sign --> (h) sign(v, h, x, s) "+h+" "+toHexString(h));

    System.arraycopy(v, 0, signature, 0, 32);
    System.arraycopy(h, 0, signature, 32, 32);

    System.out.println("sign --> (signature) arraycopy( .. v, h) "+signature+" "+toHexString(signature));

    if (!Curve25519.isCanonicalSignature(signature)) {
        System.out.println("Signature is not canonical");
    }



"""
from curve25519.Sign import Sign as si
from curve25519.Keygen import Keygen as ki
from hashlib import sha256
from curve25519.ToHexString import ToHexString
from curve25519.ParseHexString import ParseHexString as ParseHexString

## My First Account
me = "NXT-XWQY-C2MJ-JPL8-F4BW2"
# sP = "pass dig enough trace frighten foul beaten explain knowledge yeah approach spider"
sP = "this is a sample of secret pass phrase for test purpose"
pK="6282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19"
unsignedTransactionBytes = "011aa3e9910701006282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19def20e27502271d0000000000000000000e1f505000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004c11700c89063d23db6c15e010574657374310676616c756531"

# Ok, prepariamoci a fare il sign della variabile unsignedTransactionBytes

## Ok con il bytearray abbiamo problemi legati al range 0 - 256, invece che -128 - +128
## quindi proviamo a sostituire con una lista
# P = bytearray(32)
P = [0] * 32
# s = bytearray(32)
s = [0] * 32

secret = sha256(sP.encode('utf-8')).hexdigest()
sct = ParseHexString(secret).getData()

pk = ki(P, s, sct).publicKey

print("Public Key ", ToHexString(pk).getString())

print("P ", P)







