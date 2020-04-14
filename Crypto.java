/*
 * Copyright 2014 Ronald Hoffman.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package alessiotest;

import java.io.UnsupportedEncodingException;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

/**
 * Cryptographic functions using Curve25519
 *
 * Based on the Nxt reference software (NRS)
 */
public class Crypto {

    /** Crypto lock */
    private static final Object lock = new Object();

    /** Strong random number generator */
    private static final SecureRandom secureRandom = new SecureRandom();

    /** Instance of a SHA-256 digest which we will use as needed */
    private static final MessageDigest digest;
    static {
        try {
            digest = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);      // Never happen.
        }
    }

    /**
     * Calculate the SHA-256 hash of a string
     *
     * @param       input           Data to be hashed
     * @return                      The hash digest
     */
    public static byte[] singleDigest(String input) {
        byte[] bytes;
        try {
            bytes = singleDigest(input.getBytes("UTF-8"));
            System.out.println("bytes"+bytes);
            System.out.println("before singleDigest"+input);
        } catch (UnsupportedEncodingException exc) {
            bytes = null;
        }
        return bytes;
    }

    /**
     * Calculate the SHA-256 hash of a byte array
     *
     * @param       input           Data to be hashed
     * @return                      The hash digest
     */
    public static byte[] singleDigest(byte[] input) {
        byte[] bytes;
        synchronized (digest) {
            digest.reset();
            System.out.println("second function --> bytes"+input);
            bytes = digest.digest(input);
            System.out.println("second function after digest --> bytes"+bytes);

            StringBuffer sb = new StringBuffer();
            for (int i = 0; i < bytes.length; i++) {
                System.out.println(bytes[i]);
                sb.append(String.format("%02x", bytes[i] & 0xFF));
            }
            System.out.println(sb.toString());
        }
        return bytes;
    }

    /**
     * Calculate the hash of two byte arrays
     *
     * @param       input1          First byte array
     * @param       input2          Second byte array
     * @return                      The hash digest
     */
    public static byte[] singleDigest(byte[] input1, byte[] input2) {
        byte[] bytes;
        System.out.println("ma passaqua ???");
        synchronized (digest) {
            digest.reset();
            digest.update(input1);
            bytes = digest.digest(input2);
        }
        return bytes;
    }

    /**
     * Return the public key for the supplied secret phrase
     *
     * @param       secretPhrase        Account secret phrase
     * @return                          Public key
     * @throws      KeyException        Public key is not canonical
     */
    public static byte[] getPublicKey(String secretPhrase)  {
        byte[] publicKey = new byte[32];
        Curve25519.keygen(publicKey, null, singleDigest(secretPhrase));
        if (!Curve25519.isCanonicalPublicKey(publicKey))
            System.out.println("Public key is not canonical");
            /* throw new KeyException("Public key is not canonical"); */
        return publicKey;
    }

    /**
     * Sign a message
     *
     * @param       message             The message to be signed
     * @param       secretPhrase        Private key phrase
     * @return                          The signed message
     * @throws      KeyException        Unable to sign message
     */
    public static byte[] sign(byte[] message, String secretPhrase) {
        byte[] signature = new byte[64];
        try {
            synchronized(digest) {
                digest.reset();
                byte[] P = new byte[32];
                byte[] s = new byte[32];
                Curve25519.keygen(P, s, digest.digest(secretPhrase.getBytes("UTF-8")));

                System.out.println("sign --> (P) "+P+" "+toHexString(P));

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
            }
        } catch (RuntimeException|UnsupportedEncodingException e) {
            // Never happen
        }
        return signature;
    }

static final String HEXES = "0123456789abcdef";
private static final char[] hexChars = { '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f' };

public static String getHex( byte [] raw ) {
    if ( raw == null ) {
      return null;
    }
    final StringBuilder hex = new StringBuilder( 2 * raw.length );
    for ( final byte b : raw ) {
      hex.append(HEXES.charAt((b & 0xF0) >> 4))
         .append(HEXES.charAt((b & 0x0F)));
    }
    return hex.toString();
}

  /**
     * Parse a hex string and return the decoded bytes
     *
     * @param       hex                     String to parse
     * @return                              Decoded bytes
     * @throws      NumberFormatException   String contains an invalid hex character
     */
public static byte[] parseHexString(String hex) {
            if ((hex.length()&0x01) == 1)
                throw new NumberFormatException("Hex string length is not a multiple of 2");
            byte[] bytes = new byte[hex.length() / 2];
            for (int i = 0; i < bytes.length; i++) {
                int char1 = hex.charAt(i * 2);
                // System.out.println(char1+" "+hex.charAt(i * 2) );
                char1 = char1 > 0x60 ? char1 - 0x57 : char1 - 0x30;
                int char2 = hex.charAt(i * 2 + 1);
                // System.out.println(char2+" "+hex.charAt(i * 2 + 1));
                char2 = char2 > 0x60 ? char2 - 0x57 : char2 - 0x30;
                if (char1 < 0 || char2 < 0 || char1 > 15 || char2 > 15)
                    throw new NumberFormatException("Invalid hex number: " + hex);
                bytes[i] = (byte)((char1 << 4) + char2);
            }
            return bytes;
}

    /**
     * Convert a byte array to a hex string
     *
     * @param       bytes                   Bytes to encode
     * @return                              Hex string
     */
public static String toHexString(byte[] bytes) {
        char[] chars = new char[bytes.length * 2];
        for (int i = 0; i < bytes.length; i++) {
            chars[i * 2] = hexChars[((bytes[i] >> 4) & 0xF)];
            chars[i * 2 + 1] = hexChars[(bytes[i] & 0xF)];
        }
        return String.valueOf(chars);
}

}