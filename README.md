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
    me = <my RS address>
    
    ## Testnet 
    cr = credentials.Credentials("http://localhost:6876/nxt", me, None)
    
    Ga = ga.GetAccount(account=<NXTADDRESS>, includeLessors=True, includeAssets=True, includeCurrencies=True, includeEffectiveBalance=True)
    Ga.setCredentials(cr)
    Ga.run()
    print(myGa.getData("name"))
    print(myGa.getData())

Get Constants API 

    import serverinfo.getConstants as gc
    me = <my RS address>
    
    ## Testnet 
    cr = credentials.Credentials("http://localhost:6876/nxt", me, None)

    GC = gc.getConstants()
    GC.setCredentials(cr)
    GC.run()
    
    ## Object access
    myObject = GC.getObject()
    
    print(print(myObject.apiTags.ACCOUNTS.name)
    print(print(myObject.apiTags.ACCOUNTS.enabled)
    print(print(myObject.genesisBlockId)
    
    ....
    ## For list of all constants, check this page : 
    ## https://nxtwiki.org/wiki/The_Nxt_API_Examples#Get_Constants
    
    ## Dictionary access
    gcDict = GC.getData()
    

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

Signing unsignedTransactionBytes ( offline ) 

    import transactions.signTransactionOffline as sto
    sP = "this is a sample of secret pass phrase for test purpose"
    unsignedTransactionBytes = "011aa3e9910701006282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19def20e27502271d0000000000000000000e1f505000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004c11700c89063d23db6c15e010574657374310676616c756531"

    stt = sto.SignTransactionOffline(sP, unsignedTransactionBytes)

    stt.run()

    print("Signature ", stt.getSignature())

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
  
