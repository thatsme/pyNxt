
import base.Keygen as keygen
from hashlib import sha256
from curve25519.ToHexString import ToHexString as to
from curve25519.ParseHexString import ParseHexString as ph

import struct


def ByteToHex(byteStr):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """

    # Uses list comprehension which is a fractionally faster implementation than
    # the alternative, more readable, implementation below
    #
    #    hex = []
    #    for aChar in byteStr:
    #        hex.append( "%02X " % ord( aChar ) )
    #
    #    return ''.join( hex ).strip()

    return ''.join(["%02X " % ord(x) for x in byteStr]).strip()


# -------------------------------------------------------------------------------

def HexToByte(hexStr):
    """
    Convert a string hex byte values into a byte string. The Hex Byte values may
    or may not be space separated.
    """
    # The list comprehension implementation is fractionally slower in this case
    #
    #    hexStr = ''.join( hexStr.split(" ") )
    #    return ''.join( ["%c" % chr( int ( hexStr[i:i+2],16 ) ) \
    #                                   for i in range(0, len( hexStr ), 2) ] )

    bytes = []

    hexStr = ''.join(hexStr.split(" "))

    for i in range(0, len(hexStr), 2):
        bytes.append(chr(int(hexStr[i:i + 2], 16)))

    return ''.join(bytes)


## My First Account
me = "NXT-XWQY-C2MJ-JPL8-F4BW2"
sP = "pass dig enough trace frighten foul beaten explain knowledge yeah approach spider"
pK="6282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19"
message = "ciro benotti"

sP1 = "test"

secret = sha256(sP.encode('utf-8')).hexdigest()

print(type(secret))
print(secret)
#print(secret, end="")


#x = bytearray()
#m = bytearray()

x = list [0]
m = list [0]

m = sha256(message.encode('utf-8')).hexdigest()
print(type(m))
print(type(secret))

#x1 = sha256(m.encode('utf-8')+secret.encode('utf-8')).digest()
x1 = sha256(m.encode('utf-8')+secret.encode('utf-8')).hexdigest()

print(type(x1))
print("x1",x1)

for i in range(32):
    print("x1->",x1[i])


#x.extend(x1)

#for i in range(32):
#    x.append(x1[i])
    #print("x->",x[i])

#Y = bytearray()

Y = []
Y1 = bytearray()
for i in range(32):
    Y.append(0)

for i in range(32):
    Y1.append(0x00)

#print(x, type(x))

#x = bytearray(x1,'utf-8')

kg = keygen.Keygen(Y, None, x1)

roar = to(Y)

print("Firse bee .. lol ",Y)

print("Roar .. lol ",roar.getString())

bee = ph(roar.getString())

myBee = bee.getData()

print("Second Bee ..lol ", myBee)

roar1 = to(myBee)

print("Roar1 .. lol ",roar1.getString())

"""
tot = ""
for i in range(32):
    print("aada",type(Y[i]))
    #Y1.append(Y[i].to_bytes(10, byteorder='little', signed=True))
    print(Y[i].to_bytes(1, byteorder='little', signed=True))
    print(ByteToHex(Y))
    #Y1.append(struct.pack('b', Y[i]).decode('UTF-8'))


print(''.join('{:02x}'.format(x) for x in Y))

"""


