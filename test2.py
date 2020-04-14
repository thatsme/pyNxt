def _clamp(secret):
    type(secret)

    # a = ord(secret[0])
    a = secret[0]
    a &= 248
    # b = ord(secret[31])
    b = secret[31]
    b &= 127
    b |= 64
    return chr(a).encode('utf-8') + secret[1:-1] + chr(b).encode('utf-8')

ciccio = b'X\x1fr9H#}\x85\x15\xe0p\xa2\xca\x8e\xe7{\xee\x810dlp\xcc\xb0Q\x04\x8b{>@\x1b\x88'

print(_clamp(ciccio))

