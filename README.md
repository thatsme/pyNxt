# pyNxt
NXT Wrapper

Python wrapper for NXT Blockchain Api 

development version, not completed and usable yet.

# Synopsis
This is a simple python wrapper around NXT Blockchain Api ( rest )  
Reference : https://nxtwiki.org/wiki/Main_Page

# Code Example

Get Account API

    import account.getAccount as ga

    Ga = ga.GetAccount(account=<NXTADDRESS>, includeLessors=True, includeAssets=True, includeCurrencies=True, includeEffectiveBalance=True)
    Ga.run()
    print(myGa.getData("name"))
    print(myGa.getData())

Get PublicKey ( offline )
    
    from curve25519.Keygen import Keygen as ki
    from hashlib import sha256
    from curve25519.ToHexString import ToHexString
    from curve25519.ParseHexString import ParseHexString as ParseHexString

    sP = "this is a sample of secret pass phrase for test purpose"
    P = [0] * 32
    s = [0] * 32

    secret = sha256(sP.encode('utf-8')).hexdigest()
    hsecret = ParseHexString(secret).getData()

    pk = ki(P, s, hsecret).publicKey

    print("Public Key ", ToHexString(pk).getString())


# Motivation


# Installation
tbd

# API Reference
tbd

# Tests
tbd

# Contributors


# License
MIT License
  
