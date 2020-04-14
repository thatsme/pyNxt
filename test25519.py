# -*- coding: utf-8 -*-
if __name__ == "__main__":
    import sys
    import codecs
    import drop.Curve25519 as curve
    from hashlib import sha256

    ## hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    sP = "pass dig enough trace frighten foul beaten explain knowledge yeah approach spider"
    message = "Tanto va la gatta al lardo che ci lascia lo zampino"

    m = bytes(message,'utf-8')

    myCurve = curve.Curve25519()
    secret = sha256(sP.encode('ascii')).digest()


    verification_key, signing_key, secret_clamped = myCurve.curve25519_eckcdsa_keygen(secret)

    #codecs.encode(s[::-1],'hex_codec')

    print('pubkey', codecs.encode(verification_key,'hex_codec'))
    print('signing key', codecs.encode(signing_key,'hex_codec'))

    signature = myCurve.kcdsa_sign(m, secret)
    print('signature', codecs.encode(signature,'hex_codec'))

    print("MESSAGE ", message)
    print("VERIFICATION KEY ", verification_key)
    assert myCurve.kcdsa_verify(signature, m, verification_key)
    print("verified ",myCurve.kcdsa_verify(signature, m, verification_key))
    #print(signature[::-1])
    #print("=============================================================")
    assert not myCurve.kcdsa_verify(signature[::-1], signature, verification_key)
    #print("verification key ",myCurve.kcdsa_verify(signature, message, verification_key))
