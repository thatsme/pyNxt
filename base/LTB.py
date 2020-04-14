from binascii import unhexlify

class LTB(object):
    def __init__(self, val, endianness='little'):
        """
        Use :ref:`string formatting` and :func:`~binascii.unhexlify` to
        convert ``val``, a :func:`long`, to a byte :func:`str`.

        :param long val: The value to pack

        :param str endianness: The endianness of the result. ``'big'`` for
          big-endian, ``'little'`` for little-endian.

        If you want byte- and word-ordering to differ, you're on your own.


        Using :ref:`string formatting` lets us use Python's C innards.
        """

        self.val = val
        self.endianness = endianness

        self.run()

    def run(self):
        # one (1) hex digit per four (4) bits
        width = self.val.bit_length()

        # unhexlify wants an even multiple of eight (8) bits, but we don't
        # want more digits than we need (hence the ternary-ish 'or')
        width += 8 - ((width % 8) or 8)

        # format width specifier: four (4) bits per hex digit
        fmt = '%%0%dx' % (width // 4)

        # prepend zero (0) to the width, to zero-pad the output
        s = unhexlify(fmt % self.val)

        print(s)
        if self.endianness == 'little':
            # see http://stackoverflow.com/a/931095/309233
            s = s[::-1]

        return int(s)