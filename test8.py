import codecs
from binascii import unhexlify

def long_to_bytes (val, endianness='big'):
    """
    Use :ref:`string formatting` and :func:`~binascii.unhexlify` to
    convert ``val``, a :func:`long`, to a byte :func:`str`.

    :param long val: The value to pack

    :param str endianness: The endianness of the result. ``'big'`` for
      big-endian, ``'little'`` for little-endian.

    If you want byte- and word-ordering to differ, you're on your own.

    Using :ref:`string formatting` lets us use Python's C innards.
    """

    # one (1) hex digit per four (4) bits
    width = val.bit_length()

    # unhexlify wants an even multiple of eight (8) bits, but we don't
    # want more digits than we need (hence the ternary-ish 'or')
    width += 8 - ((width % 8) or 8)

    # format width specifier: four (4) bits per hex digit
    fmt = '%%0%dx' % (width // 4)

    # prepend zero (0) to the width, to zero-pad the output
    s = unhexlify(fmt % val)

    if endianness == 'little':
        # see http://stackoverflow.com/a/931095/309233
        s = s[::-1]

    return s

def int2bytes(i):
    hex_value = '{0:x}'.format(i)
    # make length of hex_value a multiple of two
    hex_value = '0' * (len(hex_value) % 2) + hex_value
    return codecs.decode(hex_value, 'hex_codec')

def mybytes( long_int ):
    bytes = []
    while long_int != 0:
        b = long_int%256
        bytes.insert( 0, b )
        long_int //= 256

    print("bytes from mybytes ", bytes)
    return bytes


list = [1106596071855577,4322640905685, 16885316037, 65958265, 28991179976305, 113246796782  ]


for a in list:

    print("long from mybytes ", a)
    mybytes(a)
    #print(long_to_bytes(a))
    print("Pack Ctypes ", packl_ctypes(a).value)
    print("================================================================")

#mylistb = struct.pack(str(len(list)) + 'f', *list)
#print("Huuuu ", mylistb)
#for a2 in mylistb:
    #print(type(a2))
#    print(a2)
    #print(int.from_bytes(a2, byteorder='big'))